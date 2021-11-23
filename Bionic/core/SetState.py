def SetState(Id='', Value='', Js=False,operation=""):
    if Js == False:
        return f'document.getElementById("{Id}").innerText="{Value}"'
    else:
        return f'document.getElementById("{Id}").innerText={Value}{operation}'
