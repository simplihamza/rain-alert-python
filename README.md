# Rain Alert

A small Python script that checks the weather forecast for a fixed
location and sends you an SMS via Twilio if rain is coming in the
next ~12 hours.

## Features

- Fetches the 3-hour forecast for the next 4 time slots (~12 hours)
  from the OpenWeatherMap API for a hardcoded latitude/longitude.
- Checks each forecast entry's weather condition code and, if any of
  them indicate rain, drizzle, snow, or a thunderstorm (condition
  id < 700), sends an SMS notification through the Twilio API.
- Reads the OpenWeatherMap API key and Twilio credentials (account
  SID, auth token, sender/receiver numbers) from environment variables
  via a `.env` file, so nothing is hardcoded in source.

## How to Run

1. Install dependencies:
   ```
   pip install requests python-dotenv twilio
   ```
2. Create a `.env` file in the project root with your OpenWeatherMap
   API key and your Twilio credentials:
   ```
   APPID=your_openweathermap_api_key
   TWILIO_ACCOUNT_SID=your_twilio_account_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_TRIAL_NUMBER=your_twilio_sender_number
   RECEIVER_NUMBER=the_number_to_receive_the_alert
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
- If no rain is forecast, `will_rain` and `message` are never
  assigned, so the script exits with a `NameError` instead of exiting
  cleanly.
- The SMS body text is a hardcoded placeholder, not an actual
  "rain is coming" message.
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
- How to send an SMS through the Twilio API using the `twilio`
  Python client.