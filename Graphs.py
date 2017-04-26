import pandas as pd
import numpy

#Array of Race to be chosen from while creating agents
Race_dist = ['White', "Black", 'Hispanic', 'Asian']

#Dataframe creates 100 agents with
#45% white, 25% Black, 12% asians, 18% hispanic peopel
#Criminality is random distribution
#the trust value ranges between 58-72 and varies randomly
Citizen_Agents = pd.DataFrame({"Race": numpy.random.choice(Race_dist, 100, p=[0.45, 0.25, .12, 0.18 ]),
                               'Criminality': numpy.random.randint(2, size=100),
                               'Size of Social Network' : numpy.random.randint(2,20, size=100),
                               'Trust': numpy.random.randint(58, 72, size=100)})
print(Citizen_Agents)


