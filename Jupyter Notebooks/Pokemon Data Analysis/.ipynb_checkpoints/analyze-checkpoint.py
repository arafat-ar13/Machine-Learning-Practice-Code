import pandas as pd

df = pd.read_csv("pokemon_data.csv", encoding='ISO-8859-1')

fire_pokemon = df[df["Type 1"] == "Fire"]
grass_pokemon = df[df["Type 1"] == "Grass"]

df.drop(columns="Powerful?", inplace=True)

sum_of_points = df.HP + df.Attack + df.Defense + df["Sp. Atk"] + df["Sp. Def"] + df.Speed

df["Average Points"] = sum_of_points/6

type1_attack_mean = df.groupby("Type 1").Attack.mean().reset_index()
type1_attack_mean.sort_values(by="Attack", inplace=True, ascending=False)

print(type1_attack_mean)

print(df[df["Type 1"] == "Dragon"].Attack.mean())

# Things yet to refresh upon
# TODO: pandas groupby
# TODO: panas pivot
# TODO: pandas merge: left merge, right merge, inner merge, outer merge, "left-on", "right-on"
# TODO: pandas concat
# TODO: pandas melt