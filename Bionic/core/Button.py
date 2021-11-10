def Button(
    width="20%",
    classname="",
        Text="",
        OnTap="",
        Margin="1px",
        Min_width="10%",
        Bg="#2c9bff",
        Text_align="center",
        FontColor="#ffffff",
        BorderRadius="5px"):

    style = f"""
            margin:        {Margin};    
            background:    {Bg};
            border:        0px solid #556699;
            border-radius: {BorderRadius};
            padding:       1.5% 6%;
            color:         {FontColor};
            display:       inline-block;
            font:          normal bold 1rem/1 "Open Sans", sans-serif;
            text-align:    {Min_width};
            min-width:     {Min_width};
            width:         {width};
            

         """

    if classname != "":
        return f"""<button onclick="{OnTap}" class='{classname}'>{Text}</button>"""
    else:
        return f"""<button onclick="{OnTap}" style='{style}' >{Text}</button>"""
