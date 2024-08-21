<div id="top"></div>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center"> optimize-eig</h3>

  <p align="center">
    optimize eig
    <br />
    <a href="https://kostyfisik.github.io/optimize-eig/readme.html"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/kostyfisik/optimize-eig/issues">Report Bug</a>
    ·
    <a href="https://github.com/kostyfisik/optimize-eig/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
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

optimize eig

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To run this project locally, you will need to install the prerequisites and follow the installation section.

### Prerequisites

This Project depends on the following projects.
* Poetry
  ```sh
  pip install --user --upgrade poetry
  ```

* Poe the Poet
  ```sh
  pip install --user --upgrade poethepoet
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/kostyfisik/optimize-eig
   cd optimize-eig
   ```
2. Install Poe the Poet and Poetry
   ```sh
   pip install --user --upgrade poethepoet poetry
   ```
3. Install requirements for development
   ```sh
   poe install-dev
   ```
4. Run tests
   ```sh
   poe test
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Some useful examples of how this project can be used:

*  Install requirements
   ```sh
   poe install-dev
   ```

*  Run tests
   ```sh
   poe test
   ```

*  Run the project
   ```sh
   poe run
   ```

*  Generate API documentation
   ```sh
   poe doc
   ```

*  Build a docker image for tests
   ```sh
   poe docker-build --target test --build-tag 3.10-alpine
   docker run -ti --rm optimize_eig:test-3.10-alpine
   ```

*  Build a docker image to run the root files only without running any test
   ```sh
   poe docker-build --target prod --build-tag 3.10-alpine --no-test
   docker run -ti --rm optimize_eig:prod-3.10-alpine
   ```
   

_For more examples, please refer to the [Documentation](https://kostyfisik.github.io/optimize-eig/readme.html)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add tests
- [x] Add code coverage
- [x] Improve documentation
- [ ] Include more tests

See the [open issues](https://github.com/kostyfisik/optimize-eig/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Konstantin Ladutenko - [@kostyfisik](https://github.com/kostyfisik) - kostyfisik@gmail.com

Project Link: [https://github.com/kostyfisik/optimize-eig/](https://github.com/kostyfisik/optimize-eig/)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

This project was created using cookiecutter and NullHack's python-project-template:

* [NullHack's python-project-template](https://github.com/nullhack/python-project-template/)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the GPL_3.0 License. See [`LICENSE`](https://github.com/kostyfisik/optimize-eig/blob/main/LICENSE) for more information.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/kostyfisik/optimize-eig.svg?style=for-the-badge
[contributors-url]: https://github.com/kostyfisik/optimize-eig/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/kostyfisik/optimize-eig.svg?style=for-the-badge
[forks-url]: https://github.com/kostyfisik/optimize-eig/network/members
[stars-shield]: https://img.shields.io/github/stars/kostyfisik/optimize-eig.svg?style=for-the-badge
[stars-url]: https://github.com/kostyfisik/optimize-eig/stargazers
[issues-shield]: https://img.shields.io/github/issues/kostyfisik/optimize-eig.svg?style=for-the-badge
[issues-url]: https://github.com/kostyfisik/optimize-eig/issues
[license-shield]: https://img.shields.io/badge/license-GPL_3.0-green?style=for-the-badge
[license-url]: https://github.com/kostyfisik/optimize-eig/blob/main/LICENSE

