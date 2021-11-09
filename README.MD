<div align="center">
  <h1>ESO Raider — performance analysis tool</h1>
  <p>
    <a href="https://eso-raider.onrender.com/">
      <img src="https://eso-raider.onrender.com/icons/favicon-128x128.png" alt="ESO Raider logo" />
    </a>
  </p>
  <h2>ESO Raider is a performance analysis and suggestion tool to help you improve your Elder Scrolls Online raiding performance</h2>
  <p>Inspired by <a href="https://wowanalyzer.com/">WoWAnalyzer</a> and <a href="https://xivanalysis.com/">xivanalysis</a></p>
</div>

---

# esoraider-server

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg?style=flat-square)](https://www.python.org/)
[![Website eso-raider.onrender.com](https://img.shields.io/website-up-down-green-red/https/eso-raider.onrender.com.svg?style=flat-square)](https://eso-raider.onrender.com/)
[![Support Server](https://img.shields.io/discord/871135724408295434.svg?color=7289da&label=ESO+Raider&logo=discord&style=flat-square)](https://discord.gg/KP8GpascgQ)

## Getting started

For development I'm using [Visual Studio Code](https://code.visualstudio.com/) and its integration with [Windows Subsystem for Linux (WSL2, Ubuntu 20.04 LTS)](https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode)

### Install **Python 3.9**

If you went with WSL and Ubuntu you might need to install python from PPA

```bash
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt install python3.9
```

Make sure that you have the right version by running

```bash
$ python -V
Python 3.9.6
```

### Install **Pipenv**

```bash
$ pip install --user pipenv
```

Please refer to [Installing Pipenv](https://pipenv.pypa.io/en/latest/install/#installing-pipenv) if you encounter any problems

### Clone repo

```bash
$ git clone https://github.com/Dreemurro/esoraider-server.git
$ cd esoraider-server
```

### Install dependencies (including dev-packages)

```bash
$ pipenv install -d
```

### Create and populate `.env` file

The `.env` file should be inside source folder, where `app.py` is located

```bash
$ touch esoraider_server/.env
```

Get your `CLIENT_ID` and `CLIENT_SECRET` from [ESO Logs API](https://www.esologs.com/api/clients/) by creating a new client

```dosini
# .env
CLIENT_ID=<YOUR_CLIENT_ID>
CLIENT_SECRET=<YOUR_CLIENT_SECRET>
DEBUG=True
SHOW_ERROR_DETAILS=True
```

### Activate shell

```bash
$ pipenv shell
```

### Run server locally

```bash
$ sh debug.sh
```

or

```bash
$ uvicorn esoraider_server.app:app --port 5000 --reload
```

## TODO

- Follow [wemake-python-styleguide](https://github.com/wemake-services/wemake-python-styleguide)
- Utilize [mypy](https://github.com/python/mypy)
- Switch to [poetry](https://github.com/python-poetry/poetry)
- Dockerize everything
