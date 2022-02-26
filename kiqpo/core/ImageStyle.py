def ImageStyle(borderRadius="None", background="None", width="None",height="None"):
    return f"""
    background-color: {background};
    border-radius: {borderRadius};
    width:{width};
    height:{height};
    """


def line(borderRadius, background, width,height):
    ImageStyle = {
        'borderRadius': borderRadius,
        'background': background,
        'width': width,
        'height':height,
    }


    pairs = ImageStyle.items()
    filtered_dictionary = {key: value for key, value in pairs if value != "None"}
    for key in filtered_dictionary:
        style = str(key+':'+filtered_dictionary[key]+";")
        print(style)

    return style
