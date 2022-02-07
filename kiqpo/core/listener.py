def listener(listenerType, id, script):

    listener = f"""document.getElementById('{id}').addEventListener('{listenerType}',(e)=>{script})"""
    return listener
