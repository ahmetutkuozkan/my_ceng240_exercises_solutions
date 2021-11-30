from pandas import *
from numpy import *
from matplotlib.pyplot import *
def min_max_normalization_calculator(value):
    result=(value-value.min())/(value.max()-value.min())
    return result
def do_plot(path_of_plot,title_of_plot,xlabel1,ylabel1):
    figure()
    plot(xlabel1,ylabel1)
    title(title_of_plot)
    savefig(path_of_plot)
data=read_csv("railway.csv")
Lengths=array(data["Length"],dtype=int)
Passengers=array(data["Passenger"],dtype=int)
do_plot("No longer raw.png","No longer raw",min_max_normalization_calculator(Lengths),min_max_normalization_calculator(Passengers))
do_plot("Raw.png","Raw",Lengths,Passengers)