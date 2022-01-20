def Button(
    classname="",
        id="button",
        text="",
        onTap=""):
    if onTap == "":
        return f"""<button id='{id}' class='{classname}'>{text}</button>"""
    else:
        return f"""<button onclick='{onTap}' id='{id}' class='{classname}'>{text}</button>"""
