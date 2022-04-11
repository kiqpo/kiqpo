def Home(*Tags):
    HtmlTagsList =  [*Tags]
    DivTags = ""
    for ele in HtmlTagsList:
        DivTags+=ele
    return f"<div style='margin-top: 10px;' >{DivTags}</div>"
