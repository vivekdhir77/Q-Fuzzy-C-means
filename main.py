from c_means import *
from Quantum_solver import *
import pandas as pd


if __name__ == "__main__":
    filename = "./iris.csv"
    generations = 100
    target_column = '4'
    
    df = pd.read_csv(filename)
    labels = df[target_column] # actual labels
    df = df.drop([target_column], axis=1) # dropping labels column


    df = df.values.tolist()
    labels = labels.values.tolist()

    f = [0.707 for i in range(2)]
    quant = Quantum_solver(extremum=1, features = f) # we are using this to maximize
    m = search_area(quant.solver()+1) # search space: range of values between 1.5 to 2.5
    global si
    for gen in range(generations):
        # print(m)
        cluster = Cmeans(df, labels, epsilon=1, distType=0, m=m)
        cluster.c_means()
        si = cluster.getSI()
        m = search_area(quant.solver(si)+1) # we are trying to maximize SI closer to 1 
    print(f"SI after {generations} generations: ",si)



