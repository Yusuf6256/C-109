import csv
import plotly.figure_factory as pf
import pandas as pd
import statistics as st

df = pd.read_csv("height-weight.csv")
height_list=df["Height(Inches)"].to_list()
weight_list=df["Weight(Pounds)"].to_list()

height_mean= st.mean(height_list)
weight_mean= st.mean(weight_list)

height_mode= st.mode(height_list)
weight_mode= st.mode(weight_list)

height_median= st.median(height_list)
weight_median= st.median(weight_list)

print("mean,median,mode of height is {},{},{} respectively".format(height_mean,height_median,height_mode))
print("mean,median,mode of weight is {},{},{} respectively".format(weight_mean,weight_median,weight_mode))

height_std_deviation=st.stdev(height_list)
weight_std_deviation=st.stdev(weight_list)

height_first_std_deviation_start,height_first_std_deviation_end=height_mean-height_std_deviation,height_mean+height_std_deviation
height_second_std_deviation_start,height_second_std_deviation_end=height_mean-(2*height_std_deviation),height_mean+(2*height_std_deviation)
height_third_std_deviation_start,height_third_std_deviation_end=height_mean-(3*height_std_deviation),height_mean+(3*height_std_deviation)

weight_first_std_deviation_start,weight_first_std_deviation_end=weight_mean-weight_std_deviation,weight_mean+weight_std_deviation
weight_second_std_deviation_start,weight_second_std_deviation_end=weight_mean-(2*weight_std_deviation),weight_mean+(2*weight_std_deviation)
weight_third_std_deviation_start,weight_third_std_deviation_end=weight_mean-(3*weight_std_deviation),weight_mean+(3*weight_std_deviation)

list_of_data_within_1_std_deviation=[result for result in height_list if result>height_first_std_deviation_start and result<height_first_std_deviation_end]
list_of_data_within_2_std_deviation=[result for result in height_list if result>height_second_std_deviation_start and result<height_second_std_deviation_end]
list_of_data_within_3_std_deviation=[result for result in height_list if result>height_third_std_deviation_start and result<height_third_std_deviation_end]

print("{}% of data lies within 1 std_deviation of height".format(len(list_of_data_within_1_std_deviation)*100/len(height_list)))
print("{}% of data lies within 2 std_deviation of height".format(len(list_of_data_within_2_std_deviation)*100/len(height_list)))
print("{}% of data lies within 3 std_deviation of height".format(len(list_of_data_within_3_std_deviation)*100/len(height_list)))

list_of_data_within_1_std_deviation=[result for result in weight_list if result>weight_first_std_deviation_start and result<weight_first_std_deviation_end]
list_of_data_within_2_std_deviation=[result for result in weight_list if result>weight_second_std_deviation_start and result<weight_second_std_deviation_end]
list_of_data_within_3_std_deviation=[result for result in weight_list if result>weight_third_std_deviation_start and result<weight_third_std_deviation_end]

print("{}% of data lies within 1 std_deviation of weight".format(len(list_of_data_within_1_std_deviation)*100/len(weight_list)))
print("{}% of data lies within 2 std_deviation of weight".format(len(list_of_data_within_2_std_deviation)*100/len(weight_list)))
print("{}% of data lies within 3 std_deviation of weight".format(len(list_of_data_within_3_std_deviation)*100/len(weight_list)))

fig = pf.create_distplot([df["Height(Inches)"].tolist()],["Height"],show_hist=False)
fig.show()
