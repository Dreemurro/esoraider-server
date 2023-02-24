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

This quick guide assumes that you have [Docker](https://docs.docker.com/desktop/) installed

### Clone the repo

```bash
$ git clone https://github.com/Dreemurro/esoraider-server.git
$ cd esoraider-server
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

### Run server locally

```bash
$ docker-compose up
```
## TODO

- Follow [wemake-python-styleguide](https://github.com/wemake-services/wemake-python-styleguide)
- Add external health check
- Add more tests
- Add coverage report
- Full CI / CD
  - Run [pytest](https://docs.pytest.org/en/7.2.x/) before deployment
  - Run [mypy](https://github.com/python/mypy) before deployment
  - Run [flake8](https://flake8.pycqa.org/en/latest/) or [flakeheaven](https://flakeheaven.readthedocs.io/en/latest/) before deployment
- Use [structlog](https://www.structlog.org/en/stable/) for logging
