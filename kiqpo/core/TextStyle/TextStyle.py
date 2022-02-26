def TextStyle(Color="#000000",Margin="0px",FontSize="100%", Background="transparent",Weight="400",LetterSpacing="1"):
    return f"""
    color:{Color};
    font-size: {FontSize};
    background: {Background};
    font-weight: {Weight};
    letter-spacing: {LetterSpacing};
    margin: {Margin};
    """
