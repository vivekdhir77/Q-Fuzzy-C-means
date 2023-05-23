import math
import random

def findRBinray(R):
    R_binary = []
    for i in range(len(R)):
        r = rand01()
        if((R[i]*R[i]) < r ):
            R_binary.append(1)
        else:
            R_binary.append(0)
    return R_binary

def alpha_new(alpha_old, delta_tetha):
    alpha_new = alpha_old * math.cos(delta_tetha) - math.sqrt(1-(alpha_old*alpha_old)) * math.sin(delta_tetha)
    return alpha_new

def Comp_Random_no(alphas, r):
    alpha_binary = []
    for i in range(len(alphas)):
        if ( (alphas[i]*alphas[i]) < r[i]):
            alpha_binary.append(1)
        else:
            alpha_binary.append(0)
    return alpha_binary

def rand01():
    return random.uniform(0, 1)
    
def binary_to_decimal(alpha_binary):
    alpha_binary.reverse()
    ans = 0
    twos = 1
    for i in alpha_binary:
        ans += (twos * i);
        twos *= 2
    return ans

def delta_tetha( s_gen, s_star, Ygen, Ymin, extremum):
    if(extremum==0):
        if(s_gen == 0 and s_star==1 and not(Ygen>Ymin)):
            return -0.03 * math.pi
        elif(s_gen == 1 and s_star==0 and not(Ygen>Ymin)):
            return 0.03 * math.pi
        else:
            return 0
    else:
        if(s_gen == 0 and s_star==1 and not(Ygen<Ymin)):
            return -0.03 * math.pi
        elif(s_gen == 1 and s_star==0 and not(Ygen<Ymin)):
            return 0.03 * math.pi
        else:
            return 0


def delta_tetha_r( r_gen, r_star, Ygen, Ymin):
    if(r_gen == 0 and r_star==1 and not(Ygen<Ymin)):
        return -0.03 * math.pi
    elif(r_gen == 1 and r_star==0 and not(Ygen<Ymin)):
        return 0.03 * math.pi
    else:
        return 0

def alpha_new(alpha_old, delta_tetha):
    alpha_new = alpha_old * math.cos(delta_tetha) - math.sqrt(1-(alpha_old*alpha_old)) * math.sin(delta_tetha)
    return alpha_new

def search_area(s):
    if(s==1):
        return 1.5+random.uniform(0, 0.25)
    elif(s==2):
        return 1.5+random.uniform(0.25, 0.5)
    elif(s==3):
        return 1.5+random.uniform(0.5, 0.75)
    elif(s==4):
        return 1.5+random.uniform(0.75, 1)
