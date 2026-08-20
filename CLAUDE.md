# CLAUDE.md

Project-specific notes for Claude Code. General working preferences live
in the global CLAUDE.md.

## Overview

Single-script Python project. Checks the OpenWeatherMap 3-hour forecast
API for the next ~12 hours (4 entries) at a hardcoded lat/lon, prints
"Bring an umbrella!" if any forecasted weather condition code indicates
rain/precipitation (id < 700).

No build system, package manifest, or test suite. The entire project is
`main.py`.

## Running

python main.py


Requires `requests` and `python-dotenv` (no requirements.txt yet, install
manually: `pip install requests python-dotenv`).

## Configuration

OpenWeatherMap API key is read from the `APPID` environment variable via
`.env` (loaded with `python-dotenv`). `.env` is gitignored and present
locally, never commit it or print its contents.

## Architecture notes

- `main.py` is entirely top-level so far (no functions/classes yet):
  load env, build request params, call the OpenWeatherMap
  `/data/2.5/forecast` endpoint, iterate `weather_data["list"]`, check
  each entry's `weather[0]["id"]`.
- Rain threshold (`id < 700`) relies on OpenWeatherMap's condition code
  grouping: codes below 700 are Thunderstorm/Drizzle/Rain/Snow, 700+ are
  Atmosphere/Clear/Clouds.
- Lat/lon and forecast count (`cnt`) are hardcoded in `weather_parameters`,
  no CLI/config layer for changing location yet.