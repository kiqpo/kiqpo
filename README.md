<div align="center">
<a href="https://kiqpo.github.io/kiqpo-dco/" ></a>
<img width="17%" src="https://i.ibb.co/HqPgpQN/rounded-corners-3.png" />

<br/>

<h3>kiqpo<h3>

<!-- <img src="https://img.shields.io/badge/contributions-welcome-greenl?&logo=github">‏‎ ‎<img src="https://img.shields.io/badge/website-up-greenl"></img> -->

<b>
<sub>
    <p>Open open source WEB-UI framework</p>
</sub>
</b>

  <p>
    <sub>
      Built with ❤︎ by
      <a href="https://github.com/kiqpo/kiqpo/graphs/contributors">
        contributors
      </a>
    </sub>
  </p>

</div>

<div align="center">
<img src="https://i.ibb.co/3TcpRH0/rounded-corners-1.png" >
</br>
</br>
</br>
</div>

kiqpo is fast. It's powered core python without any extra dependencies.
Bionic offers stateful hot reload, allowing you to make changes to your code and see the results instantly without restarting your app or losing its state.

### Getting Started

<a href="https://kiqpo.github.io/kiqpo-dco//">documentation 📖 </a>
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
