
import zillow_scraper as zs
import pandas


path = r"G:\coding\housing_proj/chromedriver"

## Denver, CO --> 1148170

df = zs.get_listings('madison', 10, path, 6)

print(df.iloc[0])

data_path = r"G:\coding\housing_proj\data_new.csv"

df.to_csv(data_path, index = False)
