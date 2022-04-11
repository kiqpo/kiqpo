def Spinner(singleColor=True):
    classname = 'mdl-spinner mdl-spinner--single-color mdl-js-spinner is-active' if singleColor == True else "mdl-spinner mdl-js-spinner is-active"
    return f"""<div class="{classname}"></div>"""