def Div(*Tags,classname=""):
    HtmlTagsList =  [*Tags]
    DivTags = ""

    for ele in HtmlTagsList:
        DivTags+=ele

    return f"<div class='{classname}' >{DivTags}</div>"