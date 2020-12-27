import csv
import pandas as pd
import plotly.express as px

df = pd.read_csv("C:/Users/Manorama/Downloads/c104p.csv")
fig = px.scatter(df,x="date",y="cases",color = "country")
fig.show()
