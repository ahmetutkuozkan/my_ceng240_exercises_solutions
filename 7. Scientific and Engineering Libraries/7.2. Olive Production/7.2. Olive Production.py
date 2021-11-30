from pandas import *
from numpy import *
from matplotlib.pyplot import *
def filter_function(average_value,valeus):
    return_value=[]
    for value in valeus:
        if(average_value>value):
            return_value.append(bool(False))
        else:
            return_value.append(bool(True))
    return return_value
def plot_function(xlabel1,ylabel1,title_of_plot,path_of_plot):
    figure()
    plot(xlabel1,ylabel1)
    xticks(range(min(xlabel1),max(xlabel1)+1), rotation="vertical")
    title(title_of_plot)
    savefig(path_of_plot)

data=read_csv("olives.csv")
Year=array(data["Year"],dtype=int)
Olive=array(data["Olive"],dtype=int)
Average_of_olive= average(Olive) # average is a function in numpy lib
filtered_olive = Olive[filter_function(Average_of_olive,Olive)]
filtered_year = Year[filter_function(Average_of_olive,Olive)]
plot_function(filtered_year,filtered_olive,"Average", "average.png")