def Padding(child, padding="1.5%", top="0%", bottom="0%", left="0%", right="0%"):
    if(top != "0%" or bottom != "0%" or left != "0%" or right != "0%"):
        return f"<div style='padding-top:{top};padding-bottom:{bottom};padding-left:{left};padding-right:{right};' >{child}</div>"
    else:
        return f"<div style='padding:{padding};' >{child}</div>"
