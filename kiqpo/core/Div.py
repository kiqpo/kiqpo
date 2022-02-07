def Div(*Tags,classname="",style=""):
    HtmlTagsList =  [*Tags]
    DivTags = ""

    for ele in HtmlTagsList:
        DivTags+=ele

    return f"<div style='{style}' class='{classname}' >{DivTags}</div>"