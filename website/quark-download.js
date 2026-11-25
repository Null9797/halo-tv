const copyQuarkLink = document.getElementById("copy-quark-link");
const quarkShareLink = document.getElementById("quark-share-link");
const quarkCopyStatus = document.getElementById("quark-copy-status");

if (navigator.clipboard && typeof navigator.clipboard.writeText === "function") {
  copyQuarkLink.hidden = false;
  copyQuarkLink.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(quarkShareLink.href);
      quarkCopyStatus.textContent = "已复制。请打开夸克网盘 App 查看并转存。";
    } catch {
      quarkCopyStatus.textContent = "可长按或右键「打开夸克网盘」，手动复制链接。";
    }
  });
}
