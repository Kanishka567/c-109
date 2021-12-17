import pandas as pd
import statistics
import csv
df=pd.read_csv("height-weight.csv")
height_list=df["Height(Inches)"].to_list()
weight_list=df["Weight(Pounds)"].to_list()
height_mean=statistics.mean(height_list)
weight_mean=statistics.mean(weight_list)
height_median=statistics.median(height_list)
weight_median=statistics.median(weight_list) 
height_mode=statistics.mode(height_list)
weight_mode=statistics.mode(weight_list)
print("mean,median,mode of height is{},{}and{}respectively".format(height_mean,height_median,height_mode))
print("mean,median,mode of weight is{},{}and{}respectively".format(weight_mean,weight_median,weight_mode))
height_std_deviation=statistics.stdev(height_list)
weight_std_deviation=statistics.stdev(weight_list)
print("standard deviation for height"height_standard_deviation)
print("standard deviation for weight"weight_standard_deviation)
height_first_std_deviation_start, height_first_std_deviation_end = height_mean-height_std_deviation, height_mean+height_std_deviation
height_second_std_deviation_start, height_second_std_deviation_end = height_mean-(2*height_std_deviation), height_mean+(2*height_std_deviation)
height_third_std_deviation_start, height_third_std_deviation_end = height_mean-(3*height_std_deviation), height_mean+(3*height_std_deviation)
weight_first_std_deviation_start, weight_first_std_deviation_end = weight_mean-weight_std_deviation, weight_mean+weight_std_deviation
weight_second_std_deviation_start, weight_second_std_deviation_end = weight_mean-(2*weight_std_deviation), weight_mean+(2*weight_std_deviation)
weight_third_std_deviation_start, weight_third_std_deviation_end = weight_mean-(3*weight_std_deviation), weight_mean+(3*weight_std_deviation)
