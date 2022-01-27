def Mode():
    return """ if(isInStandaloneMode()){
    var script = document.createElement("script");
    script.setAttribute("src", '/eel.js', 'type', 'text/javascript');
    document.getElementsByTagName("head")[0].appendChild(script);
    } """


def HTMLFile(Head, Body):
    Html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    {Head}
</head>
<body>
    {Body}
</body>
  <script src="./core.js"></script>
  <script src="/eel.js"></script>
</script>
</html>
    """

    return Html
