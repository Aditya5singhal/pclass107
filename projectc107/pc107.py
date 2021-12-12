import pandas as pd
import plotly.express as px
import csv

data=pd.read_csv("data2.csv")
mean=data.groupby(["student_id","level"],as_index=False)["attempt"].mean()
print(mean)
figure=px.scatter(mean,x="student_id",y="level",size="attempt",color="attempt")
figure.show()



