def Text(Text="", classname="", Type="p", Style="", Id="0"):
    """Return simple text render widget\n
    Type specific text type like h1 , h2 etc.\n
    example -:
    Text("Hello from Kiqpo", Type='H2',Style=TextStyle(Color='red'))
    """
    if Style != "":
        if classname != "":
            return f"""<{Type} id={Id} class='{classname}' style='{Style}'>{Text}</{Type}>"""
        else:
            return f"""<{Type} id={Id} style='{Style}'>{Text}</{Type}>"""

    else:
        if classname != "":
            return f"""<{Type} id={Id} class='{classname}'>{Text}</{Type}>"""
        else:
            return f"""<{Type} id={Id}>{Text}</{Type}>"""
