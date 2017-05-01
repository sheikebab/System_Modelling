import pandas as pd
import numpy
import matplotlib.pyplot as plt

plt.rc('font', family='serif', size=40)

pd.set_option('display.width', 1000)

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
Community_Happiness = numpy.random.randint(0,4)
for i in range(100):
    print 'i', i
    Citizen_Agents['Policed On'] = Citizen_Agents['Policed On'] + numpy.random.choice(Policed_On, 100, p=[0.99, 0.01])
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


