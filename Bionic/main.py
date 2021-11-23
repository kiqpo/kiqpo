from view import *


def RunApp():
    Head(),
    Body(
        Text(Text=0, Id='Number'),
        Button(text='+', onTap=(
            Alert("hey")
        )),
    )
