# RFOA -> red fox optimization algortihm
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
import math

best_service = 0
#function to sort the optimized values
def sort(table1, table2):
    for i in range(len(table1)):
        for j in range(len(table1)):
            if table1[i]<table1[j]:
                    table1[i], table1[j]=table1[j], table1[i]
                    table2[i], table2[j]=table2[j], table2[i]                    
    return table1, table2
#function to calculate fitness
def fitnessFunction(point):
    tmp=0
    for i in range(len(point)):
        tmp+=point[i]**2
    return tmp
#defining RFO function which take population size, iterations, min and max (L,R) values and then dataset is the cloud qos values
def rfoa(populationSize, dimension, iterations,L,R, dataset):
    global best_service
    foxes=[]
    fitness=[]
    for i in range(0, populationSize):
        foxes.append([dataset[i,0], dataset[i,1], dataset[i,2], dataset[i,3], dataset[i,4], dataset[i,5], dataset[i,6], dataset[i,7]])
    for i in range(len(foxes)):
        fitness.append(fitnessFunction(foxes[i]))
    fitness, foxes=sort(fitness,foxes)   
    
    for T in range(iterations):       
        #reproduction and leaving the herd            
        FromIndex=populationSize-0.05*populationSize
        for index in range(int(FromIndex),populationSize):
            habitatCenter=[]
            for i in range(dimension):
                habitatCenter.append((foxes[0][i]+foxes[1][i])/2)
          #  habitatDiameter=distance.euclidean(foxes[0],foxes[1])
            kappa=np.random.uniform(0,1)
            if kappa>=0.45:
                for i in range(dimension):
                    foxes[index][i]=np.random.uniform(L,R)
            else:
                for i in range(dimension):
                    foxes[index][i]=kappa*habitatCenter[i]
        
        #global phase - food searching
        for i in range(len(foxes)):
            #distances.append(distance.euclidean(foxes[i],foxes[0]))
            alpha=np.random.uniform(0,distance.euclidean(foxes[i],foxes[0]))
            for j in range(dimension):
                value=1
                if foxes[0][j]-foxes[i][j]<0:
                        value=-1
                if foxes[i][j]+alpha*value<R and foxes[i][j]+alpha*value>L:  
                    foxes[i][j]+=alpha*value
                elif foxes[i][j]-alpha*value<R and foxes[i][j]-alpha*value>L:  
                    foxes[i][j]-=alpha*value
        #local phase - traversing through the local habitat
        a=np.random.uniform(0,0.2)
        for i in range(len(foxes)):
            if np.random.uniform(0,1)>0.75:
                phi=[]
                for xx in range(dimension):
                    phi.append(np.random.uniform(0,2*3.14))
                r=np.random.uniform(0,1)

                if phi[0] != 0:
                    r=a*math.sin(phi[0])/phi[0]
                for j in range(dimension):
                    if j==0:
                        a= foxes[i][j]+a*r*math.cos(phi[0])
                        b= foxes[i][j]-a*r*math.cos(phi[0])
                        if a<R and a>L:  
                            foxes[i][j]=a
                        elif b<R and b>L:  
                            foxes[i][j]=b
                    else:
                        for k in range(j):
                            if k!=j:
                                a= foxes[i][j]+a*r*math.sin(phi[j])
                                b= foxes[i][j]-a*r*math.sin(phi[j])
                                if a<R and a>L:  
                                    foxes[i][j]=a
                                elif b<R and b>L:  
                                    foxes[i][j]=b
                            else:
                                a= foxes[i][j]+a*r*math.cos(phi[j])
                                b= foxes[i][j]-a*r*math.cos(phi[j])
                                if a<R and a>L:  
                                    foxes[i][j]=a
                                elif b<R and b>L:  
                                    foxes[i][j]=b
        fitness.clear()
        for i in range(len(foxes)):
            fitness.append(fitnessFunction(foxes[i]))
        high_fit = 0
        best_service = 0
        for i in range(len(fitness)):
            if fitness[i] > high_fit:
                best_service = i
                high_fit = fitness[i]
        fitness, foxes=sort(fitness,foxes)        
    return foxes[0], best_service




