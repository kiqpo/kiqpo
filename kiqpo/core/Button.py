def Button(
        style="",
        label="",
        Id="0",
        onTap=""):
    if onTap == "":
        if style == "":
            return f"""<button style='background: var(--primary);' class="mdc-button mdc-button--raised" id='{Id}'><span class="mdc-button__label">{label}</span></button>"""
        else:
            return f"""<button style='{style}' class="mdc-button mdc-button--raised" id='{Id}'><span class="mdc-button__label">{label}</span></button>"""
    else:
        if style == "":
            return f"""<button style='background: var(--primary);' onclick='{onTap}'' class="mdc-button mdc-button--raised" id='{Id}'><span class="mdc-button__label">{label}</span></button>"""
        else:
            return f"""<button style='{style}' onclick='{onTap}' class="mdc-button mdc-button--raised" id='{Id}'><span class="mdc-button__label">{label}</span></button>"""
