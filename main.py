from selenium import webdriver
from bs4 import BeautifulSoup
from pandas import DataFrame
from dataclasses import dataclass


@dataclass
class Data:
    apparent_magnitude: str
    name: str
    bayer_designation: str
    distance: str
    spectral_class: str
    mass: str
    radius: str
    luminosity: str


start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("D:/setup/chromedriver_win32/chromedriver.exe")
browser.get(start_url)

data = []

soup = BeautifulSoup(browser.page_source, "html.parser")
raw_data = soup.find('tbody')
for i, v in enumerate(raw_data.children):
    if v == '\n':
        continue
    res = list(v.children)
    while res.count('\n'):
        res.remove('\n')

    try:
        apparent_magnitude = res[0].get_text().rstrip()
        name = res[1].find('a').get_text().rstrip()
        bayer_designation = res[2].get_text().rstrip()
        distance = res[3].get_text().rstrip()
        spectral_class = res[4].get_text().rstrip()
        mass = res[5].get_text().rstrip()
        radius = res[6].get_text().rstrip()
        luminosity = res[7].get_text().rstrip()

        data.append(Data(apparent_magnitude, name, bayer_designation, distance, spectral_class, mass, radius, luminosity))
    except:
        pass


# define pandas dataframe
data_frame = DataFrame(data, columns=list(filter(lambda x: not x.startswith('__'), dir(data[0]))))

# convert to csv
data_frame.to_csv('data.csv')
