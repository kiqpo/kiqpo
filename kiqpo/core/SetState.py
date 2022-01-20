def SetState(Id,Value,Js=True,operation=""):
    if Js == False:
        return f'document.getElementById("{Id}").innerText="{Value}"'
    else:
        return f'document.getElementById("{Id}").innerText={Value}{operation}'
