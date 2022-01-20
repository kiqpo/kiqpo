from pydoc import classname
from view import *


def RunApp():
    Head(style="./style.css"),
    Body(
        Div(
            TopNav(backgroundColor="#f1f1f1"),
            Text("Hey, kiqpo dev's", TextStyle=TextStyle(
                FontSize="350%",
                LetterSpacing="4px",
                Weight="250",
                Color="#ffffff"
            )),
            Img(src="https://i.ibb.co/zVHfMDW/rounded-corners.png", classname="icon"),
            Link(url="https://kiqpo.github.io/kiqpo-dco/",
                 name="Get started | doc", classname="url-doc"),
            classname="bg"
        ),
    )
