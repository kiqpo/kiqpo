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
</html>
    """

    return Html
