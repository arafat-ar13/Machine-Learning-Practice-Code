import pandas as pd
import glob
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np

# Opening all the states data files using glob
files = glob.glob("states*.csv")

us_list = []
for file in files:
    data = pd.read_csv(file)
    us_list.append(data)

# Concatenating all the different data frames together
us_census = pd.concat(us_list)

# Starting by working on the Income of each state
us_census["Income"] = us_census["Income"].replace("[$]", "", regex=True)
us_census["Income"] = pd.to_numeric(us_census["Income"])


# Seperating Male and Female population data
us_census["GenderPop"] = us_census["GenderPop"].str.split("_")
us_census["Male"] = us_census["GenderPop"].str[0].replace(
    "[M]", "", regex=True)
us_census["Female"] = us_census["GenderPop"].str[1].replace(
    "[F]", "", regex=True)
del us_census["GenderPop"]
# Turning both the population in to numeric, workable data
us_census["Male"] = pd.to_numeric(us_census["Male"])
us_census["Female"] = pd.to_numeric(us_census["Female"])
# Filling missing female population
us_census["Female"] = us_census["Female"].fillna(
    us_census["TotalPop"] - us_census["Male"])

# Droping duplicates
us_census = us_census.drop_duplicates(subset=["State"])


# Readying the race data
for column in us_census.columns:
    if column in ["White", "Hispanic", "Black", "Pacific", "Asian", "Native"]:
        us_census[column] = us_census[column].replace("[%]", "", regex=True)
        us_census[column] = pd.to_numeric(us_census[column])

# Filling missing Pacific population values
us_census["Pacific"] = us_census["Pacific"].fillna(
    100 - (us_census["Hispanic"] + us_census["White"] + us_census["Black"] + us_census["Native"]) + us_census["Asian"])

# Making Female data integers
us_census["Female"] = us_census.Female.astype(int)
us_census = us_census.reset_index()

del us_census["index"]


# # Readying race data for plotting
race_name = [race for race in us_census.columns if race in ["White", "Hispanic", "Black", "Pacific", "Asian", "Native"]]
race_data = [us_census[data].mean() for data in race_name]


new_df = pd.DataFrame({"Race": race_name, "Average People": race_data})
ax = plt.subplot()

sns.barplot(x="Race", y="Average People", data=new_df)
ax.set_yticklabels([str(integer) + "%" for integer in range(0, 100, 10)])

plt.title("USA Race Data")
plt.ylabel("% of population")

plt.tight_layout()
plt.show()