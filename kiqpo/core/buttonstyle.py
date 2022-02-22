def buttonstyle(borderRadius="None", background="None", width="None"):
    getstyle = line(borderRadius, background, width)
    return f"""
    background-color: {background};
    border-radius: {borderRadius};
    width:{width};
    """


def line(borderRadius, background, width):
    buttonStyles = {
        'borderRadius': borderRadius,
        'background': background,
        'width': width,
    }


    pairs = buttonStyles.items()
    filtered_dictionary = {key: value for key, value in pairs if value != "None"}
    for key in filtered_dictionary:
        style = str(key+':'+filtered_dictionary[key]+";")
        print(style)

    return style
