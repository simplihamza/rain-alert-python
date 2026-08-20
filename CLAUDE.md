# CLAUDE.md

Project-specific notes for Claude Code. General working preferences live
in the global CLAUDE.md.

## Overview

Single-script Python project. Checks the OpenWeatherMap 3-hour forecast
API for the next ~12 hours (4 entries) at a hardcoded lat/lon, and if any
forecasted weather condition code indicates rain/precipitation (id < 700),
sends an SMS through the Twilio API. It no longer just prints to the
console.

No build system, package manifest, or test suite. The entire project is
`main.py`.

## Running

python main.py


Requires `requests`, `python-dotenv`, and `twilio` (no requirements.txt
yet, install manually: `pip install requests python-dotenv twilio`).

## Configuration

Read from environment variables via `.env` (loaded with `python-dotenv`):
- `APPID`: OpenWeatherMap API key.
- `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`: Twilio auth.
- `TWILIO_TRIAL_NUMBER`: Twilio sender number.
- `RECEIVER_NUMBER`: phone number the alert is sent to.

`.env` is gitignored and present locally, never commit it or print its
contents.

## Architecture notes

- `main.py` is entirely top-level so far (no functions/classes yet):
  load env, build request params, call the OpenWeatherMap
  `/data/2.5/forecast` endpoint, iterate `weather_data["list"]`, check
  each entry's `weather[0]["id"]`, setting `will_rain = True` if any
  entry indicates rain. `will_rain` is initialized to `False` before
  the loop, so a no-rain forecast falls through cleanly.
- If `will_rain` is `True`, a Twilio `Client` is built and a single SMS
  is sent via `client.messages.create(...)` with a fixed body ("It's
  going to rain today. Remember to bring an ☔️"), and the message
  status is printed. Nothing is printed/sent if no rain is forecast.
- Rain threshold (`id < 700`) relies on OpenWeatherMap's condition code
  grouping: codes below 700 are Thunderstorm/Drizzle/Rain/Snow, 700+ are
  Atmosphere/Clear/Clouds.
- Lat/lon and forecast count (`cnt`) are hardcoded in `weather_parameters`,
  no CLI/config layer for changing location yet.