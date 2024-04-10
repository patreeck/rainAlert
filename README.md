![IMG_20240410_180901](https://github.com/patreeck/rainAlert/assets/163764755/eee7aeab-995e-4ecb-92e9-d80e0e39a757)
**Weather Forecast Notification Script**

This Python script integrates with the OpenWeatherMap API and Twilio SMS messaging to provide proactive weather notifications. It automatically checks weather forecasts for a specified location (Dublin, Ireland) and sends SMS alerts if rain is predicted.

**Key Features**

**Automated Weather Checks:** Fetches weather forecasts for Dublin using OpenWeatherMap API.

**Rain Prediction Logic:** Determines if rain is forecasted based on weather condition codes.

**SMS Notifications:** Sends SMS alerts via Twilio to notify users about forecasted rain and recommend carrying an umbrella.

**Secure Data Handling:** Uses environment variables for sensitive information like API keys and authentication tokens.

**Error Handling:** Implements robust error handling to manage exceptions during API requests and data processing.


**Requirements**

Python 3.x
requests library (pip install requests)
twilio library (pip install twilio)

**Setup**

Clone the Repository:

git clone https://github.com/your_username/weather-forecast-notification.git

cd weather-forecast-notification


**Install Dependencies:**

pip install -r requirements.txt

Set Environment Variables:
Create a .env file in the project directory and add the following:
OWN_API_KEY=your_openweathermap_api_key
AUTH_TOKEN=your_twilio_auth_token


**Run the Script:**

python weather_forecast_notification.py
Environment Variables
OWN_API_KEY: Your OpenWeatherMap API key.
AUTH_TOKEN: Your Twilio account authentication token.


**Usage**

Update DUBLIN_LAT and DUBLIN_LONG in the script to change the location (latitude and longitude) for weather forecasts.
Customize the SMS message in the script (body parameter of client.messages.create()) as needed.
