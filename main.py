from selenium import webdriver
from bs4 import BeautifulSoup
from pandas import DataFrame
from time import sleep
from dataclasses import dataclass


@dataclass
class Data:
    name: str
    hyperlink: str
    light_years_from_earth: str
    planet_mass: str
    steller_magnitude: str
    discovery_date: str


@dataclass
class DataFinal:
    name: str
    hyperlink: str
    light_years_from_earth: str
    planet_mass: str
    steller_magnitude: str
    discovery_date: str

    planet_type: str
    planet_radius: str
    orbital_radius: str
    orbital_period: str
    eccenticity: str


start_url = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"

browser = webdriver.Chrome("D:/setup/chromedriver_win32/chromedriver.exe")
browser.get(start_url)

pre_data = []

soup = BeautifulSoup(browser.page_source, "html.parser")
raw_data = soup.find_all('ul', class_="exoplanet")
for row in raw_data:
    name = row.find('li', class_="display_name").find('a').get_text()
    hyperlink = row.find('li', class_="display_name").find('a')["href"]
    light_years_from_earth = row.find('li', class_="st_dist").get_text()
    planet_mass = row.find('li', class_="mass_display").get_text()
    steller_magnitude = row.find('li', class_="st_optmag").get_text()
    discovery_date = row.find('li', class_="discovery_date").get_text()

    pre_data.append(Data(name, hyperlink, light_years_from_earth, planet_mass, steller_magnitude, discovery_date))

data = []
# get more data
for cell in pre_data:
    browser.get("https://exoplanets.nasa.gov" + cell.hyperlink)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    res = soup.find_all('div', class_="value")
    res.pop()  # remove radial velocity
    data.append(
        DataFinal(
            cell.name, cell.hyperlink, cell.light_years_from_earth, cell.planet_mass, cell.steller_magnitude, cell.discovery_date,
            res[0].get_text(), res[3].get_text(), res[4].get_text(), res[5].get_text(), res[6].get_text()
        )
    )
    break

# define pandas dataframe
data_frame = DataFrame(data, columns=list(filter(lambda x: not x.startswith('__'), dir(data[0]))))

# convert to csv
data_frame.to_csv('data.csv')
