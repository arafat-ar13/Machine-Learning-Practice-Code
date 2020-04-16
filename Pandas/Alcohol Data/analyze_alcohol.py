import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
plt.style.use("Solarize_Light2")

alcohol_data = pd.read_csv("Alcohol.csv")

# Let's work on cleaning up the continents
continent_fullname = {"AS": "Asia", "EU": "Europe",
                      "AF": "Arica", "SA": "South America", "OC": "Oceania"}

for continent_short, continent_long in continent_fullname.items():
    alcohol_data["continent"] = alcohol_data.continent.apply(
        lambda x: continent_long if x == continent_short else x)

alcohol_data.continent.fillna(value="North America", inplace=True)
continents = alcohol_data.continent.unique()

# Creating a total alcohol column
def total_count(x):
    return x.beer_servings + x.spirit_servings + x.wine_servings


alcohol_data["total_alcohol"] = alcohol_data.apply(total_count, axis=1)


# First plot: Types of alcohol servings in each continents
alcohol_data_melted = alcohol_data.melt(id_vars=["country", "total_litres_of_pure_alcohol", "continent", "total_alcohol"], value_vars=[
                                        "beer_servings", "spirit_servings", "wine_servings"], var_name="type_of_serving", value_name="servings")

type_servings = alcohol_data_melted.groupby(
    ["continent", "type_of_serving"]).servings.mean().reset_index()

# Selecting the different types of alcohol
beer = type_servings[type_servings.type_of_serving == "beer_servings"]
spirit = type_servings[type_servings.type_of_serving == "spirit_servings"]
wine = type_servings[type_servings.type_of_serving == "wine_servings"]

wine_bottom = np.add(beer.servings.tolist(), spirit.servings.tolist())

plt.bar(beer.continent, beer.servings, label="Beer", color="orange")
plt.bar(spirit.continent, spirit.servings,
        bottom=beer.servings, label="Spirit", color="green")
plt.bar(wine.continent, wine.servings,
        bottom=wine_bottom, label="Wine", color="red")

plt.title("Alcohol consumption by continent")
plt.xlabel("Continent")
plt.ylabel("Alcohol Consumpiton")

plt.legend()

plt.show()
plt.close("all")


# Second plot: Seaborn bar graph of top 5 countries by alcohol consumption
top_five = alcohol_data.sort_values(by="total_alcohol", ascending=False).head()

sns.barplot(x="country", y="total_alcohol", data=top_five)

plt.title("Top five countries by consumption")
plt.xlabel("Country")
plt.ylabel("Total alcohol consumption")

plt.show()