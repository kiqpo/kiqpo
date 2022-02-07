def Text(Text="", classname="", Type="p", TextStyle="", Id="0"):
    if TextStyle != "":
        if classname != "":
            return f"""<{Type} id={Id} class='{classname}' style='{TextStyle}'>{Text}</{Type}>"""
        else:
            return f"""<{Type} id={Id} style='{TextStyle}'>{Text}</{Type}>"""

    else:
        if classname != "":
            return f"""<{Type} id={Id} class='{classname}'>{Text}</{Type}>"""
        else:
            return f"""<{Type} id={Id}>{Text}</{Type}>"""
