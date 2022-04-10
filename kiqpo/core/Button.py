def Button(
        style="",
        label="",
        Id="0",
        onTap=""):
    if onTap == "":
        if style == "":
            return f"""<button style='background: var(--primary);' class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" id='{Id}'><span class="mdc-button__label">{label}</span></button>"""
        else:
            return f"""<button style='{style}' class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" id='{Id}'><span class="mdc-button__label">{label}</span></button>"""
    else:
        if style == "":
            return f"""<button style='background: var(--primary);' onclick='{onTap}'' class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" id='{Id}'><span class="mdc-button__label">{label}</span></button>"""
        else:
            return f"""<button style='{style}' onclick='{onTap}' class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" id='{Id}'><span class="mdc-button__label">{label}</span></button>"""
