def FlexOptions(alignItems="center", justifyContent="space-evenly", width="100vw", flexDirection="row", height="max-content", background="  # ffffff", position="relative", left="", right="", top="", bottom=""):
    cssBlock = f""" 
    position:{position};
    width: {width};
    height: {height};
    left: {left};
    right:{right};
    top: {top};
    bottom:{bottom};
    background: {background};
    display: flex;
    flex-direction: {flexDirection};
    justify-content: {justifyContent};
    align-items: {alignItems};
     """

    return cssBlock
