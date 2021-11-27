import pandas as pd 
import plotly.figure_factory as ff 

df = pd.read_csv("data.csv")
print(df)

height_list = df["Height(Inches)"].tolist()
weight_list = df["Weight(Pounds)"].tolist()

graph1 = ff.create_distplot([height_list,weight_list],["height distribution","weight distribution"],show_hist = False)
#graph2 = ff.create_distplot([weight_list],["weight distribution"],show_hist=False)
#graph2.show()
graph1.show()