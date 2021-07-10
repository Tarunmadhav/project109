import random
import plotly_express as px
import plotly.figure_factory as ff
import pandas as pd
import statistics as st

df=pd.read_csv("StudentsPerformance.csv")
data=df["writing score"].tolist()

mean=st.mean(data)
standard=st.stdev(data)
print(mean)
print(standard)

first_std_start,first_std_end=mean-standard,mean+standard
second_std_start,second_std_end=mean-(2*standard),mean+(2*standard)
third_std_start,third_std_end=mean-(3*standard),mean+(3*standard)

thin_1_std_deviation=[result for result in data if result > first_std_start and result < first_std_end]
thin_2_std_deviation=[result for result in data if result > second_std_start and result < second_std_end]
thin_3_std_deviation=[result for result in data if result > third_std_start and result < third_std_end]


