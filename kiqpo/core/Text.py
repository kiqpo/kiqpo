def Text(text, classname="", type="p", style="", Id="0"):
    """Return simple text render wIdget\n
    type specific text type like h1 , h2 etc.\n
    example -:
    Text("Hello from Kiqpo", type='H2',style=Textstyle(Color='red'))
    """

    
    try:
        # this is a js State 
        print(text['isState'])
        if style != "":
            if classname != "":
                return f"""<{type} id={Id} class='{classname}' style='{style}'><script>document.write({text['state']})</script></{type}>"""
            else:
                return f"""<{type} id={Id} style='{style}'><script>document.write({text['state']})</script></{type}>"""

        else:
            if classname != "":
                return f"""<{type} id={Id} class='{classname}'><script>document.write({text['state']})</script></{type}>"""
            else:
                return f"""<{type} id={Id}><script>document.write({text['state']})</script></{type}>"""                       
    except:
        if style != "":
            if classname != "":
                return f"""<{type} id={Id} class='{classname}' style='{style}'>{text}</{type}>"""
            else:
                return f"""<{type} id={Id} style='{style}'>{text}</{type}>"""

        else:
            if classname != "":
                return f"""<{type} id={Id} class='{classname}'>{text}</{type}>"""
            else:
                return f"""<{type} id={Id}>{text}</{type}>"""
