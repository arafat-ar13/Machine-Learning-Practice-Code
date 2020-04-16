import pandas as pd
import requests
from bs4 import BeautifulSoup

source = requests.get("https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/shellter.html").text
soup = BeautifulSoup(source, "html.parser")
prefix = "https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/"

banner_headline = soup.find("div", attrs={"class": "banner"}).h1.text
banner_para = soup.find("span", attrs={"class": "brag"}).text

turtle_name_list = []
turtle_data_list = []

for turtle_info in soup.find_all("div", class_="box adopt"):
    turtle_link = turtle_info.a["href"]
    turtle_data_source = requests.get(prefix+turtle_link).text
    turtle_data = BeautifulSoup(turtle_data_source, "html.parser")

    turtle_name = turtle_data.find("div", class_="banner").p.text
    turtle_name_list.append(turtle_name)

    a_list = []
    for info in turtle_data.find_all("li"):
        a_list.append(info.text)
    turtle_data_list.append(a_list)

turtle_data = {key: value for key, value in zip(turtle_name_list, turtle_data_list)}

names = [x for x in turtle_data]
index = 0
for age, weight, sex, breed, source in turtle_data.values():
    print(f"{names[index]} is {age.split()[1]} years old and weighs {weight.split()[1]} lbs. It is a {sex.split()[1]} {' '.join(breed.split()[1:])} breed. We found it at {' '.join(source.split()[3:])}")
    index += 1
