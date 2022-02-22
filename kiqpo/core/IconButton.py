def IconButton(
        style="",
        text="",
        icon="",
        Id="0",
        onTap=""):


    if onTap == "":
        if style == "":
            return f"""<button style='background: var(--primary);' id={Id} class="mdc-button mdc-button--raised mdc-button--leading">
  <span class="mdc-button__ripple"></span>
  <i class="material-icons mdc-button__icon" aria-hidden="true">{icon}</i>
  <span class="mdc-button__label">{text}</span>
</button>"""
        else:
            return f"""<button style='{style}' id={Id} class="mdc-button mdc-button--raised mdc-button--leading">
  <span class="mdc-button__ripple"></span>
  <i class="material-icons mdc-button__icon" aria-hidden="true">{icon}</i>
  <span class="mdc-button__label">{text}</span>
</button>"""
    else:
        if style == "":
            return f"""<button style='background: var(--primary);' onclick='{onTap}' id={Id} class="mdc-button mdc-button--raised mdc-button--leading">
  <span class="mdc-button__ripple"></span>
  <i class="material-icons mdc-button__icon" aria-hidden="true">{icon}</i>
  <span class="mdc-button__label">{text}</span>
</button>"""
        else:
            return f"""<button style='{style}' onclick='{onTap}' id={Id} class="mdc-button mdc-button--raised mdc-button--leading">
  <span class="mdc-button__ripple"></span>
  <i class="material-icons mdc-button__icon" aria-hidden="true">{icon}</i>
  <span class="mdc-button__label">{text}</span>
</button>"""
