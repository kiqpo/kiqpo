window.onload = function () {
  console.clear();
  const isInStandaloneMode = () =>
    window.matchMedia("(display-mode: standalone)").matches ||
    window.navigator.standalone ||
    document.referrer.includes("android-app://");

  if (isInStandaloneMode()) {
    console.log("Running desktop app.");
  } else {
    console.log("Running in browser.");
  }

  if (isInStandaloneMode()) {
    document.getElementById("platform").innerText =
      "Running in kiqpo in desktop app";
  } else {
    document.getElementById("platform").innerText =
      "Running in kiqpo in browser";
  }
};

function popUp(Text = "", Info = "", ButtonText = "") {
  const card = document.createElement("div");
  const backdrop = document.createElement("div");
  backdrop.addEventListener("click", () => {
    removePopUp(card, backdrop, 0);
  });

  backdrop.className = "Bionic-backdrop";
  card.className = "Bionic-pop";
  const text = document.createElement("h1");
  text.innerText = Text;
  const info = document.createElement("p");
  info.className = "Bionic-pop-info";
  info.innerText = Info;
  const button = document.createElement("button");
  button.className = "Bionic-pop-btn";
  button.innerText = ButtonText;
  button.addEventListener("click", () => {
    removePopUp(card, backdrop, 0);
  });

  card.appendChild(text);
  card.appendChild(button);
  card.appendChild(info);

  removePopUp(card, backdrop, 200000);
  document.body.appendChild(card);
  document.body.appendChild(backdrop);
}

function removePopUp(card, backdrop, time) {
  setTimeout(() => {
    document.body.removeChild(card);
    document.body.removeChild(backdrop);
  }, time);
}
