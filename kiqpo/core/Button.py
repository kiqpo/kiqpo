def Button(
        style="",
        text="",
        Id="0",
        onTap=""):
    if onTap == "":
        return f"""<button style='{style}' class="mdc-button mdc-button--raised" id={Id}><span class="mdc-button__label">{text}</span></button>"""
    else:
        return f"""<button class="mdc-button mdc-button--raised" id={Id} onclick='{onTap}'><span class="mdc-button__label">{text}</span></button>"""
