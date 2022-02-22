def Navigator(path, windowRender, title, windowClassName):
    arg =  f'"{path}",{windowRender},"{title}","{windowClassName}"',
    print(arg[0])
    nav = f"Navigate({arg[0]})"
    return str(nav)
