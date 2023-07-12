# import pandas library
import pandas as pd
import numpy as np

other_path = "http://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

df = pd.read_csv(other_path, header=None)
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
           "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
           "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
           "peak-rpm", "city-mpg", "highway-mpg", "price"]
print("headers\n", headers)

df.columns = headers
# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe")
print(df.head(5))
print("The last 5 rows of the dataframe")
print(df.tail(5))

df1=df.replace('?',np.NaN)

df = df1.dropna(subset=["price"], axis=0)
df.head(20)

# Write your code below and press Shift+Enter to execute
print(df.columns)

df.to_csv("automobile.csv", index=False)

df.dtypes

# check the data type of data frame "df" by .dtypes
print(df.dtypes)

df.describe()

# describe all the columns in "df"
df.describe(include="all")

# Write your code below and press Shift+Enter to execute
df[['length', 'compression-ratio']].describe()

# look at the info of "df"
df.info()
