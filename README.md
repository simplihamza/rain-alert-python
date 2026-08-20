# Rain Alert

A small Python script that checks the weather forecast for a fixed
location and tells you to bring an umbrella if rain is coming in the
next ~12 hours.

## Features

- Fetches the 3-hour forecast for the next 4 time slots (~12 hours)
  from the OpenWeatherMap API for a hardcoded latitude/longitude.
- Checks each forecast entry's weather condition code and prints
  "Bring an umbrella!" if any of them indicate rain, drizzle, snow,
  or a thunderstorm (condition id < 700).
- Reads the OpenWeatherMap API key from an environment variable via a
  `.env` file, so the key isn't hardcoded in source.

## How to Run

1. Install dependencies:
   ```
   pip install requests python-dotenv
   ```
2. Create a `.env` file in the project root with your OpenWeatherMap
   API key:
   ```
   APPID=your_api_key_here
   ```
3. Run the script:
   ```
   python main.py
   ```

## Known Issues / Limitations

- The location (latitude/longitude) is hardcoded in `main.py`; there's
  no way to change it without editing the code.
- No `requirements.txt` yet, dependencies must be installed manually.
- No `.env.example` template committed.
- The script only prints a message to the console; there's no
  notification (email, push, etc.) beyond that.
- No tests.

## What I Learned

- How to call a REST API with `requests` and pass query parameters via
  a dict.
- How to keep an API key out of source control using `python-dotenv`
  and a gitignored `.env` file.
- How OpenWeatherMap groups its weather condition codes (codes below
  700 correspond to Thunderstorm/Drizzle/Rain/Snow, while 700+ are
  Atmosphere/Clear/Clouds), and how to use that grouping to detect
  rain without listing every individual code.