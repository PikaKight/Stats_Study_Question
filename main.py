import pandas as pd
import random

df = pd.read_excel("Stats Question.xlsx")
print(df.loc[random.randint(0,40)])

