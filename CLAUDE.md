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
  each entry's `weather[0]["id"]`, then build a Twilio `Client` and send
  an SMS if rain was detected.
- Rain threshold (`id < 700`) relies on OpenWeatherMap's condition code
  grouping: codes below 700 are Thunderstorm/Drizzle/Rain/Snow, 700+ are
  Atmosphere/Clear/Clouds.
- Lat/lon and forecast count (`cnt`) are hardcoded in `weather_parameters`,
  no CLI/config layer for changing location yet.
- Known bug: `will_rain` is only ever assigned inside the forecast loop
  (never initialized to `False` beforehand), and `message` is only
  assigned inside the `if will_rain:` block. If no forecast entry
  indicates rain, both the `if will_rain:` check and the trailing
  `print(message.status)` raise `NameError` instead of exiting cleanly.
- The SMS body sent via `client.messages.create(...)` is currently a
  hardcoded placeholder string, not an actual "rain is coming" message.