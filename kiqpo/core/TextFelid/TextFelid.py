def TextFelid(textType="text", onChange="", Id="01"):
    if onChange == "":
        return f"""<input id="{Id}"   type="{textType}">"""
    else:
        return f"""<input id="{Id}" onchange={onChange} type="{textType}">"""
