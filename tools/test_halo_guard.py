"""Offline CLI regressions. Every adb command is a local stub; no TV/network is used."""
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).with_name("halo-guard.sh").resolve()
PACKAGE = "app.halotv.launcher"
GUARD = PACKAGE + "/app.orchard.tv.guard.HomeGuardService"
LISTENER = PACKAGE + "/app.orchard.tv.guard.RevivalListener"
OTHER = "org.example.reader/.Reader"
OTHER_LISTENER = "org.example.notify/.Listener"

ADB_STUB = r'''#!/usr/bin/env python3
import json,os,shlex,sys
from pathlib import Path
raw=sys.argv[1:]; args=list(raw)
if args[:1]==['-s']:
 args=args[2:]
if args[:1]==['shell']:
 args=['shell']+shlex.split(args[1])
with open(os.environ['CALL_LOG'],'a') as out:
 out.write(json.dumps(args)+'\n')
p=Path(os.environ['MOCK_STATE']); state=json.loads(p.read_text())
if args[:1] in (['connect'],['devices']): state.setdefault('server_commands',[]).append(raw)
def finish(value='',code=0):
 p.write_text(json.dumps(state)); print(value); sys.exit(code)
if args[:1]==['connect']: finish('connected')
if args==['devices']: finish('List of devices attached\nexample.invalid:5555 device')
if args==['get-state']:
 finish(state.get('connection','device'),0 if state.get('connection','device')=='device' else 1)
if args[:1]!=['shell']: finish('unexpected adb command: '+str(args),99)
a=args[1:]; pkg='app.halotv.launcher'; guard=pkg+'/app.orchard.tv.guard.HomeGuardService'; listener=pkg+'/app.orchard.tv.guard.RevivalListener'
if a[:1]==['getprop']:
 finish({'ro.product.model':'Guard Test TV','ro.product.manufacturer':'Test Vendor','ro.build.version.sdk':str(state.get('sdk',33))}.get(a[1],''))
if a==['am','get-current-user']:
 if state.get('current_user_command_fails'): finish('Unknown command: get-current-user',1)
 finish(str(state.get('user',0)))
if a==['cmd','activity','get-current-user']:
 if 'fallback_user' in state: finish(str(state['fallback_user']))
 finish('Unknown command: get-current-user',1)
if a[:2]==['pm','path']:
 exists=state.get('installed',True) if a[2]==pkg else state.get('legacy',True)
 finish('package:/data/app/test/base.apk' if exists else '',0 if exists else 1)
if a[:2]==['dumpsys','package']:
 finish('versionCode=196 targetSdk=34\nversionName=3.1.1\nandroid.permission.WRITE_SECURE_SETTINGS: granted='+str(state.get('secure',False)).lower())
if a==['dumpsys','accessibility']:
 if state.get('unknown_bound'): finish('vendor accessibility status unavailable')
 bound='Service[label=Halo TV, id='+guard+']' if state.get('bound') else ''
 finish('User state[\n Bound services:{'+bound+'}\n Enabled services:{'+state['enabled']+'}\n Binding services:{}\n]')
if a[:3]==['settings','get','secure']:
 finish({'enabled_accessibility_services':state['enabled'],'accessibility_enabled':state.get('global','0'),'enabled_notification_listeners':state['listeners']}.get(a[3],'null'))
if a[:3]==['settings','put','secure']:
 if state.get('refuse_settings'): finish('SecurityException: denied by firmware',1)
 key={'enabled_accessibility_services':'enabled','accessibility_enabled':'global','enabled_notification_listeners':'listeners'}.get(a[3])
 if not key: finish('unexpected setting',99)
 state[key]=a[4]; finish()
if a[:2]==['pm','grant']:
 if a[2]!=pkg: finish('wrong package',99)
 if state.get('refuse_permission'): finish('SecurityException: permission not changeable',1)
 state['secure']=True; finish()
if a[:2]==['appops','get']:
 if a[2]!=pkg: finish('wrong package',99)
 op=a[3]
 if state.get('op_stdout_failure'): finish(state['op_stdout_failure'])
 if op not in state['ops']: finish('Error: Unknown operation string: '+op,1)
 finish(op+': '+state['ops'][op])
if a[:2]==['appops','set']:
 if a[2]!=pkg or a[3] not in state['ops']: finish('wrong/unsupported op',99)
 state['ops'][a[3]]=a[4]; finish()
if a[:3]==['cmd','notification','allow_listener']:
 if state.get('silent_notification'): finish()
 if state.get('unsupported_notification'): finish('Unknown command: notification',1)
 state['listeners'] += ':'+a[3]; finish()
if a[:3]==['cmd','package','resolve-activity']: finish('com.vendor.launcher/.Home')
if a[:2]==['am','start']:
 if a[-1]!=pkg+'/app.orchard.tv.MainActivity': finish('wrong activity identity',99)
 if not state.get('no_bind') and guard in state['enabled'] and state.get('global')=='1': state['bound']=True
 finish('Status: ok')
finish('unexpected adb command: '+str(args),99)
'''


class HaloGuardCliTest(unittest.TestCase):
    def run_cli(self, repair=False, **changes):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            log = root / "calls"
            state = {
                "enabled": OTHER, "listeners": OTHER_LISTENER, "sdk": 33,
                "ops": {"SYSTEM_ALERT_WINDOW": "default", "GET_USAGE_STATS": "default", "ACCESS_RESTRICTED_SETTINGS": "default"},
            }
            without_tv = changes.pop("without_tv", False)
            state.update(changes)
            (root / "state").write_text(json.dumps(state))
            adb = root / "adb"
            adb.write_text(ADB_STUB)
            adb.chmod(0o755)
            env = dict(os.environ, ADB=str(adb), CALL_LOG=str(log), MOCK_STATE=str(root / "state"), HALO_GUARD_WAIT_SECONDS="0")
            if without_tv:
                env.pop("TV", None)
            else:
                env["TV"] = "example.invalid"
            result = subprocess.run(["bash", str(SCRIPT)] + (["--repair"] if repair else []), env=env, capture_output=True, text=True, timeout=8)
            calls = [json.loads(line) for line in log.read_text().splitlines()] if log.exists() else []
            return result, calls, json.loads((root / "state").read_text())

    def mutations(self, calls):
        return [c for c in calls if c[:3] in (["shell", "pm", "grant"], ["shell", "appops", "set"], ["shell", "settings", "put"], ["shell", "am", "start"]) or c[:4] == ["shell", "cmd", "notification", "allow_listener"]]

    def test_default_is_read_only_and_detects_registered_but_not_bound(self):
        old = 'app.orchard.tv/.guard.HomeGuardService'
        result, calls, _ = self.run_cli(enabled=OTHER+':'+GUARD+':'+old, **{'global':'1'})
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.mutations(calls), [])
        self.assertIn("尚未绑定", result.stdout)
        self.assertIn("可能互相争抢", result.stdout)
        self.assertIn("versionName：3.1.1", result.stdout)
        self.assertNotIn("已实际绑定", result.stdout)

    def test_connect_is_server_command_without_premature_transport_selector(self):
        result, _, state = self.run_cli()
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(state['server_commands'],[['connect','example.invalid:5555']])

    def test_repair_targets_new_identity_and_preserves_other_services(self):
        result, calls, state = self.run_cli(repair=True)
        self.assertEqual(result.returncode, 0, result.stdout+result.stderr)
        self.assertEqual(state['enabled'], OTHER+':'+GUARD)
        self.assertEqual(state['listeners'], OTHER_LISTENER+':'+LISTENER)
        self.assertTrue(state['secure'])
        self.assertIn(["shell", "am", "start", "-W", "-n", PACKAGE+"/app.orchard.tv.MainActivity"], calls)
        self.assertIn("已确认独立版守护实际绑定", result.stdout)
        for call in self.mutations(calls):
            self.assertNotIn('app.orchard.tv', call)
            self.assertNotIn('reboot', call)
            self.assertNotIn('set-home-activity', call)
        self.assertFalse(any(c[:2] == ['shell', 'setprop'] or c[:1] in (['install'], ['uninstall'], ['tcpip']) for c in calls))

    def test_supported_vendor_appops_are_optional_and_not_blindly_written(self):
        result, calls, _ = self.run_cli(repair=True, sdk=30)
        self.assertEqual(result.returncode, 0, result.stdout+result.stderr)
        writes = [c for c in calls if c[:3] == ['shell','appops','set']]
        self.assertFalse(any(c[4] in ('APP_AUTO_START','APP_ASSOC_START','ASSOC_START','ACCESS_RESTRICTED_SETTINGS') for c in writes))
        self.assertIn('固件不支持此 AppOp', result.stdout)

    def test_api33_restricted_permission_alias_and_vendor_start_are_verified(self):
        ops = {'SYSTEM_ALERT_WINDOW':'allow','GET_USAGE_STATS':'allow','android:access_restricted_settings':'default','APP_AUTO_START':'default','ASSOC_START':'default'}
        result, calls, state = self.run_cli(repair=True, ops=ops)
        self.assertEqual(result.returncode, 0, result.stdout+result.stderr)
        self.assertEqual(state['ops']['android:access_restricted_settings'],'allow')
        self.assertEqual(state['ops']['APP_AUTO_START'],'allow')
        self.assertEqual(state['ops']['ASSOC_START'],'allow')
        self.assertNotIn(['shell','appops','set',PACKAGE,'SYSTEM_ALERT_WINDOW','allow'], calls)

    def test_rejected_secure_write_is_not_reported_as_success(self):
        result, calls, state = self.run_cli(repair=True, refuse_settings=True)
        self.assertEqual(result.returncode, 4)
        self.assertEqual(state['enabled'], OTHER)
        self.assertIn('SecurityException', result.stdout)
        self.assertIn('尚未确认守护实际绑定', result.stdout)

    def test_missing_independent_app_never_repairs_the_legacy_package(self):
        result, calls, _ = self.run_cli(repair=True, installed=False)
        self.assertEqual(result.returncode, 3)
        self.assertEqual(self.mutations(calls), [])
        self.assertIn('不会给旧包授权', result.stdout)

    def test_unauthorized_connection_stops_before_reading_or_mutating(self):
        result, calls, _ = self.run_cli(repair=True, connection='unauthorized')
        self.assertEqual(result.returncode, 2)
        self.assertIn('允许 USB 调试', result.stderr)
        self.assertEqual(self.mutations(calls), [])
        self.assertFalse(any(c[:1] == ['shell'] for c in calls))

    def test_incorrect_short_component_is_diagnosed_and_correct_one_is_added(self):
        wrong = PACKAGE+'/.guard.HomeGuardService'
        result, _, state = self.run_cli(repair=True, enabled=OTHER+':'+wrong)
        self.assertEqual(result.returncode, 0, result.stdout+result.stderr)
        self.assertIn(wrong, state['enabled'])
        self.assertTrue(state['enabled'].endswith(':'+GUARD))
        self.assertIn('错误的独立包短类名', result.stdout)

    def test_corrupted_list_is_not_replaced_or_interpreted_as_shell_code(self):
        bad = OTHER+':bad/$(echo injected)'
        result, calls, state = self.run_cli(repair=True, enabled=bad)
        self.assertEqual(result.returncode, 4)
        self.assertEqual(state['enabled'], bad)
        self.assertFalse(any(c[:5] == ['shell','settings','put','secure','enabled_accessibility_services'] for c in calls))
        self.assertIn('列表格式异常', result.stdout)

    def test_silent_notification_grant_falls_back_to_preserving_merged_list(self):
        result, calls, state = self.run_cli(repair=True, silent_notification=True)
        self.assertEqual(result.returncode, 0, result.stdout+result.stderr)
        self.assertEqual(state['listeners'], OTHER_LISTENER+':'+LISTENER)
        self.assertIn(['shell','settings','put','secure','enabled_notification_listeners',OTHER_LISTENER+':'+LISTENER], calls)

    def test_single_existing_adb_device_can_be_diagnosed_without_connect(self):
        result, calls, _ = self.run_cli(without_tv=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(any(c[:1] == ['connect'] for c in calls))
        self.assertEqual(self.mutations(calls), [])

    def test_unknown_dump_format_does_not_claim_guard_is_running(self):
        result, _, _ = self.run_cli(repair=True, unknown_bound=True)
        self.assertEqual(result.returncode, 4)
        self.assertIn('无法确认', result.stdout)
        self.assertNotIn('已确认独立版守护实际绑定', result.stdout)

    def test_non_owner_android_user_cannot_be_repaired(self):
        result,calls,_ = self.run_cli(repair=True,user=10)
        self.assertEqual(result.returncode,3,result.stdout+result.stderr)
        self.assertEqual(self.mutations(calls),[])
        self.assertIn('仅允许已确认的 Android 主用户 0',result.stdout)

    def test_unknown_android_user_cannot_be_repaired(self):
        result,calls,_ = self.run_cli(repair=True,current_user_command_fails=True)
        self.assertEqual(result.returncode,3,result.stdout+result.stderr)
        self.assertEqual(self.mutations(calls),[])
        self.assertIn('当前 Android 用户：无法确认',result.stdout)

    def test_android_user_lookup_has_compatible_fallback(self):
        result,calls,_ = self.run_cli(repair=True,current_user_command_fails=True,fallback_user=0)
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        self.assertIn(['shell','cmd','activity','get-current-user'],calls)

    def test_zero_exit_failure_stdout_does_not_authorize_unsupported_ops(self):
        for failure in ('Failed to resolve operation','Permission denial: appops unavailable','No UID for app.halotv.launcher'):
            with self.subTest(failure=failure):
                result,calls,_=self.run_cli(repair=True,op_stdout_failure=failure)
                self.assertEqual(result.returncode,0,result.stdout+result.stderr)
                self.assertFalse(any(c[:3]==['shell','appops','set'] for c in calls))


class BoundDumpTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location('halo_guard', SCRIPT.with_name('halo_guard.py'))
        cls.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.module)

    def test_enabled_list_does_not_masquerade_as_bound(self):
        dump = 'Bound services:{}\nEnabled services:{'+GUARD+'}\n'
        self.assertIs(self.module.bound_state(dump, GUARD),False)

    def test_nested_bound_container_and_unrelated_first_entry(self):
        dump = 'mBoundServices=[Service[id=other.pkg/.Reader], Service[id='+GUARD+']]\nmEnabledServices=['+GUARD+']'
        self.assertIs(self.module.bound_state(dump,GUARD),True)

    def test_invalid_independent_short_class_is_not_equal(self):
        self.assertIs(self.module.bound_state('Bound services:{id='+PACKAGE+'/.guard.HomeGuardService}',GUARD),False)

    def test_other_android_user_binding_does_not_claim_current_user_success(self):
        dump = 'User state[attributes:{id=0}\nBound services:{}\n]\nUser state[attributes:{id=10}\nBound services:{id='+GUARD+'}\n]'
        self.assertIsNone(self.module.bound_state(dump,GUARD))

    def test_vendor_labels_without_components_are_unknown(self):
        self.assertIsNone(self.module.bound_state('Bound services:{Service[label=Halo TV]}',GUARD))

    def test_unclosed_bound_container_does_not_swallow_enabled_services(self):
        dump='Bound services:{broken\nEnabled services:{'+GUARD+'}'
        self.assertIsNone(self.module.bound_state(dump,GUARD))

    def test_single_other_user_binding_does_not_claim_owner_success(self):
        dump='User state[attributes:{id=10}\nBound services:{'+GUARD+'}\n]'
        self.assertIsNone(self.module.bound_state(dump,GUARD,user=0))


if __name__ == '__main__':
    unittest.main()
