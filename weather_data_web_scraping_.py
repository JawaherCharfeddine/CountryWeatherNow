
#libreries
from requests_html import HTMLSession
import tkinter as tk
from tkinter import ttk
import requests

# Make a GET request to the Restcountries API
responsecountry = requests.get("https://restcountries.com/v3.1/all")

# Check if the request was successful
if responsecountry.status_code == 200:
    # Parse the JSON response
    data = responsecountry.json()

    # Extract and print country names
    country_names = [country["name"]["common"] for country in data]
    country_names = sorted(country_names)

else:
    print("Failed to retrieve country data.")

# Function to scrape weather data for the selected country
def scrape_weather_data(query):
    # Create an HTMLSession object
    session = HTMLSession()
    url = f'https://www.google.com/search?q=wether+tunisia&oq=wether+{query}'
    # Send an HTTP GET request to a webpage
    response = session.get(url, headers={
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47'})

    # get the temperature
    temperature = response.html.find('span#wob_tm',
                                     first=True).text  # sapn#wob_tm : get the span with the "idwob_tm"
    # get the unit
    unit = response.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
    desc = response.html.find('div.VQF4g', first=True).text
    return f"Weather in {query}:\nTemperature: {temperature} {unit}\nDescription: {desc}"

# Function to open a custom dialog box
def open_custom_dialog(country, weather_data):
    dialog = tk.Toplevel(window)
    dialog.title(f"Weather Information for {country}")
    dialog.geometry("300x200")  # Set the width and height of the dialog box

    label = tk.Label(dialog, text=weather_data, padx=20, pady=10)
    label.pack()
    ok_button = tk.Button(dialog, text="OK", command=dialog.destroy, width=10)
    ok_button.pack()


# Function to handle the selection from the dropdown
def on_country_select(event):
    selected_country = country_combobox.get()
    if selected_country:
        weather_data = scrape_weather_data(selected_country)
        #messagebox.showinfo("Weather Information", weather_data)
        open_custom_dialog(selected_country, weather_data)

# Create a Tkinter window
window=tk.Tk()
window.title("Country Selector")
window.geometry("300x150")

# Create a label
label = tk.Label(window, text="Select a Country to show weather:")
label.pack(pady=20)

# Create a Combobox (Dropdown) to display the country names
country_combobox = ttk.Combobox(window, values=country_names, width=20)
country_combobox.bind("<<ComboboxSelected>>", on_country_select)
country_combobox.pack(pady=20)

# Set a default value for the Combobox
default_value = "default"
country_combobox.set(default_value)

# Start the Tkinter main loop
window.mainloop()


