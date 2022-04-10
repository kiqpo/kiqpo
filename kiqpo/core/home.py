def Home(*Tags):
    HtmlTagsList =  [*Tags]
    DivTags = ""
    for ele in HtmlTagsList:
        DivTags+=ele
    return f"<div>{DivTags}</div>"
