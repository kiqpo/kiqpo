def HTMLFile(Head, Body):
    Html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    {Head}
</head>
<body style='font-family: Arial, Helvetica, sans-serif;'>
    {Body}
</body>
</html>
    """

    return Html
