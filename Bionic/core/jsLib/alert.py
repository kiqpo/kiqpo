def alert(data, js=False):
    if js == False:
        return f'alert("{data}")'
    else:
        return f'alert({data})'
