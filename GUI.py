import os
import numpy as np
import pandas as pd
from tkinter import *
from tkinter import simpledialog
import tkinter
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter import ttk
import timeit
from RedFox import * #importing redfox class

global filename

main = tkinter.Tk()
main.title("Cloud Service Composition using RedFox Algorithm")
main.geometry("1300x1200")

def uploadDataset():
    global filename, dataset
    text.delete('1.0', END)
    filename = filedialog.askopenfilename(initialdir="Dataset")
    status.config(text = os.path.basename(filename)+" loaded")
    dataset = pd.read_csv(filename)
    text.insert(END, str(dataset))

def runRedFox():
    global filename, dataset
    text.delete('1.0', END)
    num_population = int(population_list.get()) #read population size
    itr = int(iterations_list.get()) #taking num iterations
    dataset = pd.read_csv(filename, nrows=num_population) #reading dataset
    start = timeit.default_timer()
    #now called rfo algorithm function with dataset values to get optimized selected service values
    fitness, best_service = rfoa(dataset.shape[0], dataset.shape[1], 10, np.sum(dataset.min().ravel()), np.sum(dataset.max().ravel()), dataset.values)
    fitnesses = []
    fitnesses.append(fitnessFunction(fitness))
    avg_fitness = sum(fitnesses)
    end = timeit.default_timer()
    print(avg_fitness)
    avg_fitness = f"{avg_fitness:.30f}"
    text.insert(END,"Red Fox Optimized Average Fitness = "+str(avg_fitness)+"\n\n")
    text.insert(END,"Execution Time = "+str(end - start)+" Sec\n\n")
    text.insert(END,"Best Optimized Selected Service Composition Details\n\n")
    services = ['Response Time', 'Availability', 'Throughput', 'Successability', 'Reliability', 'Compliance', 'Best Practices', 'Latency']
    dataset = dataset.values
    for i in range(len(services)):
        text.insert(END,services[i]+" = "+str(dataset[best_service,i])+"\n")
    
font = ('times', 12, 'bold')
title = Label(main, text='Cloud Service Composition using RedFox Algorithm',anchor=W, justify=CENTER)
title.config(bg='yellow4', fg='white')  
title.config(font=font)           
title.config(height=3, width=120)       
title.place(x=0,y=5)
       
font1 = ('times', 13, 'bold')
    
upload = Button(main, text="Upload Dataset", command=uploadDataset)
upload.place(x=10,y=100)
upload.config(font=font1)  
    
status = Label(main, text='')
status.config(font=font1)
status.place(x=180,y=100)
    
l1 = Label(main, text='Population :')
l1.config(font=font1)
l1.place(x=10,y=150)

population = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]

population_list = ttk.Combobox(main,values=population, postcommand=lambda: population_list.configure(values = population))
population_list.place(x=180,y=150)
population_list.current(0)
population_list.config(font=font1) 
    
l2 = Label(main, text='Iterations :')
l2.config(font=font1)
l2.place(x=10,y=200)

iterations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

iterations_list = ttk.Combobox(main,values=iterations, postcommand=lambda: population_list.configure(values = iterations))
iterations_list.place(x=180,y=200)
iterations_list.current(0)
iterations_list.config(font=font1)


b3 = Button(main, text = "Run RedFox Algorithms", command=runRedFox)
b3.config(font=font1)
b3.place(x=90,y=250)
    

text=Text(main,height=15,width=120)
scroll=Scrollbar(text)
text.configure(yscrollcommand=scroll.set)
text.place(x=10,y=300)
text.config(font=font1)
    
main.config(bg='magenta3')
main.mainloop()














    
