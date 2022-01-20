<div align="center">
<a href="https://kiqpo.github.io/kiqpo-dco/" ></a>
<img width="15%" src="https://i.ibb.co/zVHfMDW/rounded-corners.png" />

<br/>

<h3>kiqpo<h3>

<img src="https://img.shields.io/badge/contributions-welcome-green?&logo=github">

<img src="https://img.shields.io/website?url=https://kiqpo.github.io/kiqpo-dco/&logo=icon"></img>

<b><p>Open open source WEB-UI framework</p></b>

</div>

### Fast 🚀

Bionic is fast. It's powered core python without any extra dependencies.
Bionic offers stateful hot reload, allowing you to make changes to your code and see the results instantly without restarting your app or losing its state.

### Getting Started

<a href="https://bionic-py.github.io/Bionic-Documentation/">documentation 📖 </a>
</br>
This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

#### Installation 📥

```shell:
pip install bionic.control
```

#### Crafting new projct 👷

```shell:
Bionic.py create hello_world
```

#### Running & Testing ⚗️

```shell:
cd Bionic
bionic.py
```

#### This is how the default page looks like ✨:-

<img width="75%" src='https://i.ibb.co/b5dwzHM/Screenshot-from-2021-11-20-00-35-45.png' />

#### Code example ⚡

```python
from view import *

def RunApp():
    Head(title="Welcome"),
    Body(
        Text("hello"),
        Button(Text="btn", OnTap=Alert("hello")),
    )
```

<!-- CONTRIBUTING -->

#### Contributing 🤝

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

happy coding ❤️
