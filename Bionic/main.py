from view import *


def RunApp():
    Head(),
    Body(
        Text('hello',Id='myText'),
        Button(text='text', onTap=(
            ReadJS('/button.js')
        )),
    ),
