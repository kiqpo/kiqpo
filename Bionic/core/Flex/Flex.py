def Flex(*Div, options=''):
    DivTagsList = [*Div]
    DivTags = ""
    for ele in DivTagsList:
        DivTags += ele

    FlexDiv = f"""
    <div style="{options}" >
        {DivTags}
    </div>
    """
    return FlexDiv

