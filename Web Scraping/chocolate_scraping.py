import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

source = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/cacao/index.html').text
soup = BeautifulSoup(source, "html.parser")

# This will get the ratings of all the chocolates in float
ratings = []
for rating in soup.find_all("td", attrs={"class": "Rating"}):
	ratings.append(rating.text)
ratings = ratings[1:]
ratings = [float(rating) for rating in ratings]

# This is plot a histogram of the ratings
plt.hist(ratings)
plt.show()

# This gets all the companies as a list
company_tags = soup.find_all("td", attrs={"class": "Company"})
companies = []
for company in company_tags:
  companies.append(company.text)
companies = companies[1:]

# This is the dictionary to be used with pandas pd DataFrame
company_with_ratings = {"Companies": companies, "Rating": ratings}
df = pd.DataFrame.from_dict(company_with_ratings)

# This gets the average rating of all the companies grouped together
grouped_info = df.groupby("Companies").Rating.mean()
# The companies with the top ten ratings
top_ten = grouped_info.nlargest(10)

# This strips the "%" from the percentages and stores them as a list
cocoa_percentage = []
for each in soup.find_all("td", attrs={"class": "CocoaPercent"}):
    cocoa_percentage.append(each.text)
cocoa_percentage = cocoa_percentage[1:]
cocoa_percentage = [float(cocoa.strip("%")) for cocoa in cocoa_percentage]

# This creates a new column in our dataframe
df["Cocoa Percentage"] = cocoa_percentage

# Here, I am using matplotlib to plot a scrattered data, comparing the ratings with the percentages
plt.scatter(df["Cocoa Percentage"], df.Rating)
z = np.polyfit(df["Cocoa Percentage"], df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(df["Cocoa Percentage"], line_function(df["Cocoa Percentage"]), "r--")
plt.show()