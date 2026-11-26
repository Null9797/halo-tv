const copyQuarkShare = document.getElementById("copy-quark-share");
const quarkShareContent = document.getElementById("quark-share-content");
const quarkCopyStatus = document.getElementById("quark-copy-status");

if (copyQuarkShare && quarkShareContent && navigator.clipboard && typeof navigator.clipboard.writeText === "function") {
  copyQuarkShare.hidden = false;
  copyQuarkShare.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(quarkShareContent.textContent);
      quarkCopyStatus.textContent = "已复制完整分享内容。请打开夸克 App 查看并转存。";
    } catch {
      quarkCopyStatus.textContent = "请选中或长按上方文字，手动复制整段分享内容。";
    }
  });
}
