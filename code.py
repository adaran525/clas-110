
import plotly.figure_factory as ff
import csv
import plotly.graph_objects as go
import statistics
import random
import pandas as pd

df = pd.read_csv('newdata.csv')
data = df['average'].tolist

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data))
        Value = data[random_index]
        dataset.append(Value)
    mean = statistics.mean(dataset)
    return mean

#fuction to plot the mean on the graph
def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["average"],show_hist = False)
    fig.add_trace(go.Scatter(x = [mean,mean],y = [0,1],mode = 'lines',name = 'mean'))
    fig.show()


#pass the number of time you want the mean of the data point as a parameter in range function
def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)

    mean = statistics.mean(mean_list)
    print("mean of sampling distribution: -",mean)

setup()


#code to find the mean of the raw data
population_mean = statistics.mean(data)
print("population mean: -",population_mean)

#code to find standard deviation of sample data
def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)


    std_deviation = statistics.stdev(mean_list)
    print('standard deviation of sampling distribution: -',std_deviation)


standard_deviation()


