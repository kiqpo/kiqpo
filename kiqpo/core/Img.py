def img(src='',alt='img',classname='',style=""):
    return f"""
    <img style='{style}' class='{classname}' src="{src}" alt='{alt}'' />
    """