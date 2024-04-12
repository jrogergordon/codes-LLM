import pandas as pd
data = {"County":{"0":"Adams","1":"Alamosa","2":"Arapahoe","3":"Archuleta","4":"Baca"},"2014Pop":{"0":479477,"1":15758,"2":617498,"3":12240,"4":3576},"2015Pop":{"0":489774,"1":15854,"2":628951,"3":12401,"4":3544},"2016Pop":{"0":497419,"1":16006,"2":637266,"3":12839,"4":3522},"2017Pop":{"0":503375,"1":16056,"2":643257,"3":13316,"4":3539},"2018Pop":{"0":511868,"1":16683,"2":651215,"3":13765,"4":3585}}
df = pd.DataFrame(data)
# Find the top 3 counties with the highest population in 2018
top_3_counties = df.sort_values('2018Pop', ascending=False).head(3)

# Create a new DataFrame containing only these counties and their population data for all years
top_3_counties_all_years = top_3_counties[['County'] + [col for col in df.columns if col.endswith('Pop')]]

# Print the resulting DataFrame
print(top_3_counties_all_years)