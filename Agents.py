import pandas as pd
import numpy
import matplotlib.pyplot as plt

#Set display Options and seed generator
plt.rc('font', family='serif', size=40)
pd.set_option('display.width', 1000)
numpy.random.seed(6845)

class Agent_Generation:

    def __init__(self, agent_types, number_of_agents):
        self.agent_type = agent_types
        self.number_of_agents = number_of_agents

        #Initialise the Agent Dataframes
        self.Citizen_Agents = self.Generation_of_Agents(self.number_of_agents)

    def Generation_of_Agents(self, number_agents):
        import pandas
        race_dist = ['White', "Black", 'Hispanic', 'Asian']
        agents = pandas.DataFrame({"Race": numpy.random.choice(race_dist, number_agents, p=[0.45, 0.25, .12, 0.18]),
                                       'Criminality': numpy.random.randint(2, size=number_agents),
                                       'Size of Social Network': numpy.random.randint(2, 15, size=number_agents),
                                       'Policed On': numpy.full(number_agents, 0, dtype=int),
                                       'Initial Trust': numpy.random.randint(58, 72, size=number_agents),
                                       'Final Trust': numpy.full(number_agents, 0, dtype=int)})

        return agents