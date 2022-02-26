from core.dev import conditionalOperator


stylePros = """
        document.documentElement.style.setProperty('--primary', '#0A84FF');
        document.documentElement.style.setProperty('--error', '#F44336');
        document.documentElement.style.setProperty('--secondary', '#F2F2F7');
        document.documentElement.style.setProperty('--background', '#ffffff');
        document.documentElement.style.setProperty('--textSecondary', '#212121');

        document.documentElement.style.setProperty('--mdc-theme-on-primary', '#F2F2F7');
        document.documentElement.style.setProperty('--mdc-theme-primary', '#0A84FF');
        document.documentElement.style.setProperty('--mdc-theme-error', '#F44336');
        """


def Mode():
    return """ if(isInStandaloneMode()){
    var script = document.createElement("script");
    script.setAttribute("src", '/eel.js', 'type', 'text/javascript');
    document.getElementsByTagName("head")[0].appendChild(script);
    } """


def HTMLFile(Head, Body, Topleavel, WindowswindowRender, Theme):
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
    {conditionalOperator.ConditionalOperator(Theme,"",stylePros)}
  </script>

</html>
    """
    return Html
