def IconButton(
        style="",
        text="",
        icon="",
        Id="0",
        onTap=""):


    if onTap == "":
        if style == "":
            return f"""<button style='background: var(--primary);' id={Id} class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent">
  <span class="mdc-button__ripple"></span>
  <i class="material-icons mdc-button__icon" aria-hidden="true">{icon}</i>
  <span class="mdc-button__label">{text}</span>
</button>"""
        else:
            return f"""<button style='{style}' id={Id} class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent">
  <span class="mdc-button__ripple"></span>
  <i class="material-icons mdc-button__icon" aria-hidden="true">{icon}</i>
  <span class="mdc-button__label">{text}</span>
</button>"""
    else:
        if style == "":
            return f"""<button style='background: var(--primary);' onclick='{onTap}' id={Id} class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent">
  <span class="mdc-button__ripple"></span>
  <i class="material-icons mdc-button__icon" aria-hidden="true">{icon}</i>
  <span class="mdc-button__label">{text}</span>
</button>"""
        else:
            return f"""<button style='{style}' onclick='{onTap}' id={Id} class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent">
  <span class="mdc-button__ripple"></span>
  <i class="material-icons mdc-button__icon" aria-hidden="true">{icon}</i>
  <span class="mdc-button__label">{text}</span>
</button>"""
