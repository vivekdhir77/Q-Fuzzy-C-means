from c_means import *
from Quantum_solver import *
import pandas as pd

def main(df, labels, generations, distType=0):
    f = [0.707 for i in range(2)]
    quant = Quantum_solver(extremum=1, features = f) # we are using this to maximize
    m = search_area(quant.solver()+1) # search space: range of values between 1.5 to 2.5
    global si
    for gen in range(generations):
        # print(m)
        cluster = Cmeans(df, labels, epsilon=1, distType=distType, m=m)
        cluster.c_means()
        si = cluster.getSI()
        m = search_area(quant.solver(si)+1) # we are trying to maximize SI closer to 1
    return si 

def norm(df):
    df_new = []
    for row in df: # row/sqrt(f1^2 + f2^2 + f3^2...)
        denominator = 0
        for feature in row:
            denominator += (feature*feature)
        denominator = math.sqrt(denominator)
        record = []
        for feature in row:
            try:
                record.append(feature/denominator)
            except:
                record.append(0)
        df_new.append(record)
    df = df_new
    return df

if __name__ == "__main__":
    filename = "./iris.csv"
    generations = 100
    target_column = '4'
    
    df = pd.read_csv(filename)
    labels = df[target_column] # actual labels
    df = df.drop([target_column], axis=1) # dropping labels column
    df = df.values.tolist()
    df_normalized = norm(df)
    labels = labels.values.tolist()
    si1 = main(df, labels, generations)
    si2 = main(df_normalized, labels, generations, 1)
    print(f"(non qunatum) SI after {generations} generations: ",si1)
    print(f"(qunatum) SI after {generations} generations: ",si2)



