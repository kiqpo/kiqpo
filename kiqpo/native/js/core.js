let runningMood = "";
let os = "";
// app running mood

const isInStandaloneMode = () =>
  window.matchMedia("(display-mode: standalone)").matches ||
  window.navigator.standalone ||
  document.referrer.includes("android-app://");

if (isInStandaloneMode()) {
  console.log("webapp is installed");
  runningMood = "DESKTOP";
  window.addEventListener("contextmenu", (e) => e.preventDefault());

  // (function (proxied) {
  //   window.alert = function () {
  //     console.log(arguments[0]);
  //   };
  // })(window.alert);
} else {
  console.log("webapp is not installed");
  runningMood = "WEB";
}

// app running mood

// get os name

function getOS() {
  var userAgent = window.navigator.userAgent,
    platform = window.navigator.platform,
    macosPlatforms = ["Macintosh", "MacIntel", "MacPPC", "Mac68K"],
    windowsPlatforms = ["Win32", "Win64", "Windows", "WinCE"],
    iosPlatforms = ["iPhone", "iPad", "iPod"],
    os = null;

  if (macosPlatforms.indexOf(platform) !== -1) {
    os = "Mac OS";
  } else if (iosPlatforms.indexOf(platform) !== -1) {
    os = "iOS";
  } else if (windowsPlatforms.indexOf(platform) !== -1) {
    os = "Windows";
  } else if (/Android/.test(userAgent)) {
    os = "Android";
  } else if (!os && /Linux/.test(platform)) {
    os = "Linux";
  }

  return os;
}
// save os to localStorage
localStorage.setItem("os", getOS());
// save os to localStorage
// app running mood to localStorage
localStorage.setItem("runningMood", runningMood);
// save app running mood to localStorage



mdc.textField.MDCTextField.attachTo(document.querySelector(".mdc-text-field"));
