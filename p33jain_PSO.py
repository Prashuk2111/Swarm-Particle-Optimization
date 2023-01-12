import random
# import math
import copy
from matplotlib import pyplot as plt
import numpy as np

# Fitness calculations
def fitness(X_Y):
    fitness = ((4 - (2.1*pow(X_Y[:,0],2)) + (pow(X_Y[:,0],4)/3))*pow(X_Y[:,0],2)) + (X_Y[:,0]*X_Y[:,1]) + ((-4 + (4*pow(X_Y[:,1],2)))*pow(X_Y[:,1],2))
    return fitness

# Main Function
def main(Population_size,Iterations):

    # Intializing X,Y, their velocities, personal and global best
    X_Y_Current = np.random.uniform(-5,5,(Population_size,2))
    X_Y_Velocity = np.zeros((Population_size,2),dtype=float)
    P_Best_X_Y = X_Y_Current
    G_Best = [random.uniform(-5,5),random.uniform(-5,5)]
    Global_best_fitness = ((4 - (2.1*pow(G_Best[0],2)) + (pow(G_Best[0],4)/3))*pow(G_Best[0],2)) + (G_Best[0]*G_Best[1]) + ((-4 + (4*pow(G_Best[1],2)))*pow(G_Best[1],2))
    
    # Parameters for veloctiy calcuation which can further be manipulated
    C1 = 1.44944
    C2 = 1.449744
    W = 0.792
    iter = 0

    # Parameters for plot
    average_fitness, Best_fitness = np.array([]), np.array([])
    Number_of_iterations = np.arange(Iterations)+1
    
    # PSO implementation
    while(iter<Iterations):
        
        R1,R2 = random.uniform(0,1), random.uniform(0,1)
        X_Y_Velocity = W*X_Y_Velocity + C1*R1*(P_Best_X_Y - X_Y_Current) + C2*R2*(G_Best-X_Y_Current)
        X_Y_Current = X_Y_Current + X_Y_Velocity
        X_Y_Fitness = fitness(X_Y_Current)
        X_Y_Fitness_Personal_best = fitness(P_Best_X_Y)
        IS_True = np.less(X_Y_Fitness, X_Y_Fitness_Personal_best)  

        # quick note P_Best_X_Y[IS_True] is same as P_Best_X_Y[IS_True, :]
        P_Best_X_Y[IS_True] = X_Y_Current[IS_True]

        Best_fitness_overall = fitness(P_Best_X_Y)
        Index_min_fitness = np.argmin(Best_fitness_overall)

        if (Best_fitness_overall[Index_min_fitness] < Global_best_fitness):
            Global_best_fitness = Best_fitness_overall[Index_min_fitness]
            G_Best = P_Best_X_Y[Index_min_fitness,:]
        
        # W- 0.001, just remember W value should not drop less than 0.5 for example, in our case iterations is less so this makes sense, else put this under if statement
        iter,W = iter+1,W-0.001
        # iter = iter+1
        average_fitness = np.append(average_fitness,np.average(X_Y_Fitness))
        Best_fitness = np.append(Best_fitness,Global_best_fitness)

    print(G_Best)
    print(Global_best_fitness)
    fig, [ax1,ax2] = plt.subplots(2)
    ax1.plot( Number_of_iterations,average_fitness)
    ax1.set_title("average_fitness")
    ax2.plot(Number_of_iterations,Best_fitness)
    ax2.set_title("best_fitness")
    plt.show()

if __name__ == "__main__":
    main(10, 100)


