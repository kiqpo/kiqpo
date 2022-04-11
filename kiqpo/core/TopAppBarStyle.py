def TopAppBarStyle(background):
    getstyle = line(background)
    return f"""background-color: {background};"""


def line(background):
    topAppBarStyle = {
        'background-color': background,
    }


    pairs = topAppBarStyle.items()
    filtered_dictionary = {key: value for key, value in pairs if value != "None"}
    for key in filtered_dictionary:
        style = str(key+':'+filtered_dictionary[key]+";")

    return style