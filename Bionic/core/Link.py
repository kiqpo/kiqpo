def Link(url, Label="", hideLabel=False):
    if Label == "":
        if hideLabel == True:
            Label = ""
        else:
            Label = url

    return f""" <a href='{url}'>{Label}</a>"""
