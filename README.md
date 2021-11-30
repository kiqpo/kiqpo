

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/bionic-py/Bionic)
![Lines of code](https://img.shields.io/tokei/lines/github/bionic-py/Bionic)
![GitHub](https://img.shields.io/github/license/bionic-py/Bionic)
![GitHub Hacktoberfest combined status](https://img.shields.io/github/hacktoberfest/2021/bionic-py/Bionic)
![GitHub issue/pull request detail](https://img.shields.io/github/issues/detail/title/bionic-py/Bionic/1)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/bionic.control?logo=python&logoColor=white)
[![Gitter](https://badges.gitter.im/Bionic-community/community.svg)](https://gitter.im/Bionic-community/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)



<!-- <img src="https://repository-images.githubusercontent.com/426888760/64d87104-0e32-4373-b2a9-0ce078153db9" /> -->





<p align="center">
  <img width='85%' src="https://repository-images.githubusercontent.com/426888760/64d87104-0e32-4373-b2a9-0ce078153db9" />
</p>



> Bionic is Python Framework for crafting beautiful, fast user experiences for web and is free and open source.

### Fast 🚀

 Bionic is fast. It's powered core python without any extra dependencies.
 Bionic offers stateful hot reload, allowing you to make changes to your code and see the results instantly without restarting your app or losing its state.

### Getting Started

<a href="https://bionic-py.github.io/Bionic-Documentation/">documentation  📖 <a/>
 </br>
This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

##### Installation 📥

```shell:
pip install bionic.control
```

##### Crafting new projct 👷

```shell:
Bionic.py create hello_world
```

##### Running & Testing ⚗️

```shell:
cd Bionic
bionic.py
```




##### This is how the default page looks like ✨:-
<img width="75%" src='https://i.ibb.co/b5dwzHM/Screenshot-from-2021-11-20-00-35-45.png' />




##### Code example ⚡

```python:
from view import *

def RunApp():
    Head(title="Welcome"),
    Body(
        Text("hello"),
        Button(Text="btn", OnTap=Alert("hello")),
    )
```

<!-- CONTRIBUTING -->
##### Contributing 🤝

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

happy coding ❤️
