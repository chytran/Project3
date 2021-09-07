import pandas as pd

df = pd.read_html('https://www.zillow.com/homes/San-Jose,-CA_rb/')

print(df)