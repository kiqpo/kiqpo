def initialize(name):
    return f"""<div id="{name}" class="mdl-js-snackbar mdl-snackbar">
      <div class="mdl-snackbar__text"></div>
      <button class="mdl-snackbar__action" type="button"></button>
    </div>"""


def show(name,message):
    return f"""snackbarShow("{name}","{message}")"""