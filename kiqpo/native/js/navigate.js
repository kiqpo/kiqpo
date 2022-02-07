let XPageData = {};
let windowLocation = window.location.href;
let windowClass = [];

document.querySelectorAll(".Navigate-kiqpo").forEach((item) => {
  item.addEventListener("click", (event) => {
    //handle click
    event.preventDefault();
  });
});

function Navigate(Path, NewWindow, Title, windowClassName) {
  const main = document.getElementsByTagName("main")[0];
  document.querySelector("." + windowClassName).remove();
  windowClass.push(windowClassName)

  XPageData = {
    path: Path,
    NewWindow: NewWindow,
    Title: Title,
  };

  main.insertAdjacentHTML("afterbegin", windowRenders[NewWindow]);
  console.log(windowLocation);
  windowLocation = window.location.href;
  history.pushState("none", Title, Path);
}

// window.history.pushState({page: 1}, "", "");

// window.onpopstate = function(event) {
//   // document.querySelector("." + windowClass).remove();
//   console.log(windowClass)
// }
