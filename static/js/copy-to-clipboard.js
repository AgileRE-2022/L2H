function copyTheme1ToClipboard() {
  let textarea = document.getElementById("html-code-theme1");
  textarea.select();
  document.execCommand("copy");
}

function copyTheme2ToClipboard() {
  let textarea = document.getElementById("html-code-theme2");
  textarea.select();
  document.execCommand("copy");
}