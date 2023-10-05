# CountryWeatherNow
CountryWeatherNow is a user-friendly a realtime weather application that provides instant access to weather data for selected country. Stay informed about current weather conditions, temperature, and forecasts for any city or country.


# Weather Data Web Scraping Python Script

This Python script is designed to perform two main tasks:

1. **Retrieve Country Names from Restcountries API:** It makes an HTTP GET request to the Restcountries API to retrieve a list of country names and sorts them alphabetically.

2. **Scrape Weather Data for Selected Country:** It provides a graphical user interface (GUI) using Tkinter to allow the user to select a country from a dropdown menu. When a country is selected, the script scrapes weather data for that country from Google and displays it in a custom dialog box.

## Dependencies

The script relies on the following Python libraries:

- [requests](https://pypi.org/project/requests/): Used for making HTTP GET requests.
- [requests_html](https://pypi.org/project/requests-html/): Used for web scraping with HTMLSession.
- [tkinter](https://docs.python.org/3/library/tkinter.html): Used for creating the graphical user interface (GUI).

## Usage

1. **Install Dependencies**: Before running the script, make sure you have the necessary dependencies installed. You can install them using pip:

   ```bash
   pip install requests
   pip install requests_html

2. **Run the Script**: Run the Python script using your preferred Python interpreter.

    ```bash
    python weather_data_web_scraping_.py

3. **View the Output** : If the request is successful, the script will show A Tkinter window will appear.

4. **GUI Interaction**: A Tkinter window will appear with a dropdown menu. Select a country from the dropdown, and click the "OK" button. A custom dialog box will display weather information for the selected country.

   ![run](https://github.com/JawaherCharfeddine/CountryWeatherNow/blob/main/execution%20result.png)

## Usage


Author
[JawaherCharfeddine]
License
This script is licensed under the MIT License.





