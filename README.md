



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://i.imgur.com/5z9hADM.png">
    <img src="https://i.imgur.com/5z9hADM.png" alt="Logo" width="250" height="80">
  </a>

  <h3 align="center">ACML</h3>

  <p align="center">
    Advanced Config Markup Language
    <br />
    <a href="https://github.com/brodycritchlow/ACML/wiki"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">PyPi</a>
    ·
    <a href="https://github.com/brodycritchlow/ACML/issues">Report Bug</a>
    ·
    <a href="https://github.com/brodycritchlow/ACML/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

ACML is a custom markup language designed for creating complex configuration files with nested sections and key-value pairs. It allows users to organize their configuration data into different subsections, making it easy to manage and modify large configuration files.

Here's why:
- With ACML, you can easily define subsections using the [section.subsection] syntax, and populate them with any number of key-value pairs. These key-value pairs can be simple strings, integers, floats, lists, and even JSON-style dictionaries.

Of course, no one configuration format will serve all projects since your needs may be different. So I'll be adding more in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue.


### Built With

ACML is purely built off of Python, we chose Python for its flexibility and easy grammar so more people can contribute.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

We are hosted on [PyPi](https://pypi.org/project/acml/), so you can sit back and relax by using `pip`.

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Download Python and PIP
2. Open a command prompt
3. Run the following command: 
	- `pip install ACML`  - This may work on most systems
	- `py -m pip install ACML` - Works 100% of the time on Windows 10+
	- `pip3 install ACML` - Linux Distros

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

```py
from ACML import *

config = parse("path/to/config.conf/")
config["key"]["key2"]
```

_For more examples, please refer to the [Documentation](https://github.com/brodycritchlow/ACML/wiki)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Add Parser
- [x] Add Read Me
- [x] Add License
- [ ] Add multiple config formats
- [ ] Add more tests

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Brody Critchlow - [thornily#6566](https://discord.com/users/612107033608585252)

Project Link: [https://github.com/brodycritchlow/ACML](https://github.com/brodycritchlow/ACML)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Readme Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>