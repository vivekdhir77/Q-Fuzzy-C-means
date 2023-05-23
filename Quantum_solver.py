from functions import *

class Quantum_solver: # if extremum = 1 then it finds maxima else mimima
    def __init__(self, features, extremum=0, rand_solve=True):
        self.Feature_Count = len(features)
        self.alphas = features
        self.rand_solve = rand_solve
        self.extremum = extremum
        self.r = [rand01() for i in range(self.Feature_Count)]
        self.Smax = [0 for i in range(self.Feature_Count)]
        self.Y_extremum_value = 0
        self.iteration = 0
        self.generation = 0 #store the best gen when we got the optimal value
        if(extremum == 0):
            self.Y_extremum_value= 1
        else:
            self.Y_extremum_value= 0

    def solver(self, fitness=1): #returns a binary list
    # ----------------------------
    # initialising alpha values, Y_extremum_value and Smax-(List for storing Maximum Binary list) 
        # alphas = [0.707, 0.707]# alpha1, alpha2 .....

        # Y_extremum_value = 1000
        
        # Smax = [0 for i in range(self.Feature_Count)]
    # -------------------------------------------------------
        R_binary = findRBinray(self.r) # making binary string from 'r' values -> condition: [ (R[i]*R[i]) < r ]
        alpha_binary = Comp_Random_no(self.alphas, self.r) # comparition with random no to get binary list

        if (self.iteration == 0):
            self.iteration+=1
            search_space = binary_to_decimal(alpha_binary)
            return search_space

        # S = binary_to_decimal(alpha_binary) + 1 # finding search space
        Ygen = fitness
    # -------------------------------------------------------
        if(self.extremum == 0):
            if(Ygen< self.Y_extremum_value):
                self.Y_extremum_value = Ygen
                self.generation = self.iteration
                self.Smax = alpha_binary
        else:
            if(Ygen> self.Y_extremum_value):
                self.Y_extremum_value = Ygen
                self.generation = self.iteration
                self.Smax = alpha_binary
    # -------------------------------------------------------
        for j in range(self.Feature_Count):
            s_star = self.Smax[j]
            s_gen = alpha_binary[j]
            S_r = R_binary[j]
            self.alphas[j] = alpha_new(self.alphas[j], delta_tetha( s_gen, s_star, Ygen, self.Y_extremum_value, self.extremum)) # updating bits using quantum rotation gate
            if( not(self.rand_solve) ):
                self.r[j] = alpha_new( self.r[j], delta_tetha_r( s_gen, S_r, Ygen, self.Y_extremum_value)) # updating r bits using quantum rotation gate
        if(self.rand_solve):
            self.r = [rand01() for i in range(self.Feature_Count)]
        self.iteration += 1
        search_space = binary_to_decimal(alpha_binary)
        return search_space
    def best(self):
        return self.Y_extremum_value
    # -------------------------------------------------------