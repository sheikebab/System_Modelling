import pandas as pd
import numpy
import matplotlib.pyplot as plt
import math
plt.rc('font', family='serif', size=40)
pd.set_option('display.width', 1000)
numpy.random.seed(6845)
#Array of Race to be chosen from while creating agents
Race_dist = ['White', "Black", 'Hispanic', 'Asian']

#Dataframe creates 100 agents with
#45% white, 25% Black, 12% asians, 18% hispanic peopel
#Criminality is random distribution
#the trust value ranges between 58-72 and varies randomly
Citizen_Agents = pd.DataFrame({"Race": numpy.random.choice(Race_dist, 100, p=[0.45, 0.25, .12, 0.18 ]),
                               'Criminality': numpy.random.randint(2, size=100),
                               'Size of Social Network' : numpy.random.randint(2,15, size=100),
                               'Policed On' : numpy.full(100, 0, dtype=int),
                               'Initial Trust': numpy.random.randint(58, 72, size=100),
                               'Final Trust': numpy.full(100, 0, dtype=int)})
# print(Citizen_Agents)
Policed_On = [0,1]
Mean_Social_Network = Citizen_Agents['Size of Social Network'].mean()
# print Mean_Social_Network
gamma = numpy.random.choice(range(1,2,8))
Avg_Black_Trust = []
Avg_White_Trust = []
Avg_Asian_Trust = []
Avg_Hispanic_Trust = []
Daily_Avg = []
for i in range(90):
    print 'i', i
    zeta = numpy.random.rand(1)
    Community_Happiness = numpy.random.randint(0, 4)
    # Community_Happiness = Citizen_Agents['Policed On'].sum()*numpy.random.rand(1)
    alpha = numpy.random.rand(1)
    # beta = numpy.random.rand(1)
    beta = 0.2
    Citizen_Agents['Policed On'] = Citizen_Agents['Policed On'] + numpy.random.choice(Policed_On, 100, p=[0.998, 0.002])
    Citizen_Agents['T+%d' % i] = numpy.full(100, 0, dtype=int)
    for j in range(100):
        if i == 0:
            if Citizen_Agents.Race[j] == 'Black':
                Citizen_Agents.loc[j, 'T+%d' %i] = Citizen_Agents['Initial Trust'][j] + (Citizen_Agents['Policed On'][j])*(-1)
            elif Citizen_Agents.Race[j] == 'White':
                Citizen_Agents.loc[j, 'T+%d' %i] = Citizen_Agents['Initial Trust'][j] + (Citizen_Agents['Policed On'][j])*(1)
            elif Citizen_Agents.Race[j] == 'Asian':
                Citizen_Agents.loc[j, 'T+%d' %i] = Citizen_Agents['Initial Trust'][j] + (Citizen_Agents['Policed On'][j]) * (-0.4)
            else:
                Citizen_Agents.loc[j, 'T+%d' %i] = Citizen_Agents['Initial Trust'][j] + (Citizen_Agents['Policed On'][j])*(-0.8)
        else:
            if Citizen_Agents.Race[j] == 'Black':
                Citizen_Agents.loc[j, 'T+%d' %i] = Citizen_Agents['T+%d' %(i-1)][j] + (Citizen_Agents['Policed On'][j])*(-1)
            elif Citizen_Agents.Race[j] == 'White':
                Citizen_Agents.loc[j, 'T+%d' %i] = Citizen_Agents['T+%d' %(i-1)][j] + (Citizen_Agents['Policed On'][j])*(1) + Community_Happiness
            elif Citizen_Agents.Race[j] == 'Asian':
                Citizen_Agents.loc[j, 'T+%d' %i] = Citizen_Agents['T+%d' %(i-1)][j] + (Citizen_Agents['Policed On'][j]) * (-0.3) + Community_Happiness
            else:
                Citizen_Agents.loc[j, 'T+%d' %i] = Citizen_Agents['T+%d' %(i-1)][j] + (Citizen_Agents['Policed On'][j])*(-0.8)  + Community_Happiness
    Citizen_Agents['Final Trust'] = Citizen_Agents['T+%d'%i]
    Avg_Asian_Trust.append(Citizen_Agents.ix[lambda s: Citizen_Agents.Race == 'Asian']['T+%d'%i].mean())
    Avg_Black_Trust.append(Citizen_Agents.ix[lambda s: Citizen_Agents.Race == 'Black']['T+%d'%i].mean())
    Avg_Hispanic_Trust.append(Citizen_Agents.ix[lambda s: Citizen_Agents.Race == 'Hispanic']['T+%d'%i].mean())
    Avg_White_Trust.append(Citizen_Agents.ix[lambda s: Citizen_Agents.Race == 'White']['T+%d'%i].mean())
# print(Citizen_Agents)


# Plot Average trust for all races
x = numpy.arange(100)
plt.plot(x, Avg_Asian_Trust, color = 'red', linewidth=4.0)
plt.plot(x, Avg_Black_Trust, color = 'black',  linewidth=4.0)
plt.plot(x, Avg_Hispanic_Trust,  color = 'brown', linewidth=4.0)
plt.plot(x, Avg_White_Trust,  color = 'orange',  linewidth=4.0)
plt.legend(['Asian', 'Black', 'Hispanic', 'white'], loc = 'upper left')
plt.xticks(numpy.arange(0, 100, 5.0))
plt.xlabel('Time Period')
plt.ylabel('Average trust')
# plt.show()


