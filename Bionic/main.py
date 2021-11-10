from view import *


def RunApp():
    Head(title="Welcome"),
    Body(
        Text("hello", Id="hello_text"),
        Button(
            Text="new",
            OnTap=(
                State(Id="hello_text", SetState="welcome")
            )),

    ),
