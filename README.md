# MUNICS SI Lab1

<div align="center">

***Information Security: Lab assignment I - Onion Routing***

[![Python](https://img.shields.io/badge/Python-black?logo=python&logoColor=white&labelColor=grey&color=%233776AB)](<https://www.python.org/> "Python")
[![License: MIT](<https://img.shields.io/github/license/danielfeitopin/MUNICS-SI-Lab1>)](LICENSE "License")
[![GitHub issues](https://img.shields.io/github/issues/danielfeitopin/MUNICS-SI-Lab1)](<https://github.com/danielfeitopin/MUNICS-SI-Lab1> "Issues")
[![GitHub stars](https://img.shields.io/github/stars/danielfeitopin/MUNICS-SI-Lab1)](<https://github.com/danielfeitopin/MUNICS-SI-Lab1/stargazers> "Stars")

</div>

## Table of Contents

- [MUNICS SI Lab1](#munics-si-lab1)
  - [Table of Contents](#table-of-contents)
  - [Configuration](#configuration)
    - [Configure Files](#configure-files)
    - [Add the Keys](#add-the-keys)
    - [Set up the virtual environment](#set-up-the-virtual-environment)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)


## Configuration

### Configure Files

Complete the [config.py](<src/tor/config.py>) file with the required configuration.

```py
ID = # TODO My MQTT User
PASSWORD = # TODO Password to read the private key (or None)

# MQTT Conexion Configuration
MQTT_USER_NAME = # TODO
MQTT_PASSWORD = # TODO
MQTT_IP = # TODO
MQTT_PORT = # TODO
MQTT_KEEPALIVE = # TODO
```

Add the public keys to the `pubkey_dictionary` dictionary inside [pubkeys.py](<src/tor/pubkeys.py>).

```py
pubkey_dictionary = {
    # TODO
}
```

### Add the Keys

Add the private and public `ssh-rsa` keys to the `src` folder.

### Set up the virtual environment

A [Pipfile](<src/Pipfile>) is provided to create a virtual environment.

```sh
cd src
pipenv install
```

## Usage

Use the python package with the desired option (a help menu is provided):

```sh
pipenv run python -m tor
```

```
Usage: python -m tor (activate | encrypt | send):
    activate    Activates tor node.
    encrypt     Prints output of nest encryption.
    send        Sends message using nest encryption.
```

## Contributing

Contributions are welcome! If you have improvements, bug fixes, or new modules to add, feel free to submit a pull request.

## License

The content of this repository is licensed under the [MIT License](LICENSE).

## Contact

Feel free to get in touch with me!

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-%23181717?style=for-the-badge&logo=github&logoColor=%23181717&color=white)](<https://github.com/danielfeitopin>)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-white?style=for-the-badge&logo=linkedin&logoColor=white&color=%230A66C2)](<https://www.linkedin.com/in/danielfeitopin/>)

</div>