def Mode():
    return """ if(isInStandaloneMode()){
    var script = document.createElement("script");
    script.setAttribute("src", '/eel.js', 'type', 'text/javascript');
    document.getElementsByTagName("head")[0].appendChild(script);
    } """


def HTMLFile(Head, Body, Topleavel,WindowswindowRender,Theme):
    Html = f"""<!DOCTYPE html>
<html lang="en">

<head>
    {Head}
</head>

<body>
    {Body}
</body>

  <script src="./js/material-components-web.js"></script>
  <script src="./js/core.js"></script>
  <script src="./js/navigate.js"></script>
  <script src="/eel.js"></script>

  <script>
    {Topleavel}
    eel.expose(say_hello_js)
  </script>

    <script>
    {WindowswindowRender}
    {Theme}
  </script>

</html>
    """

    return Html
