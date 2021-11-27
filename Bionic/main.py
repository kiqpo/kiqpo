from view import *


def RunApp():
    Head(),
    Body(
        Text(Text=0, Id='Number'),
        Button(text='+', onTap=(
            Alert("Hi there 👋, thanks for trying out Bionic. Team of Bionic wish you a very happy web development.")
        )),
    )

