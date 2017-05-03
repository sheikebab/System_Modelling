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
        agents = pandas.DataFrame({'Race': numpy.random.choice(race_dist, number_agents, p=[0.45, 0.25, .12, 0.18]),
                                    'Criminality': numpy.random.randint(2, size=number_agents),
                                    'Size of Social Network': numpy.random.randint(2, 15, size=number_agents),
                                    'Policed On': numpy.full(number_agents, 0, dtype=int),
                                    'Initial Trust': numpy.random.randint(58, 72, size=number_agents),
                                    'Final Trust': numpy.full(number_agents, 0, dtype=int)})

        return agents

    def Update_Trust(self, agent_df, time_period):
        for i in range(time_period):
            zeta = numpy.random.rand(1)
            community_happiness = numpy.random.randint(0, 4)
            alpha = numpy.random.rand(1)
            beta = 0.2
            agent_df['Policed On'] =agent_df['Policed On'] + numpy.random.choice([0,1], self.number_of_agents,
                                                                                              p=[0.998, 0.002])
            agent_df['T+%d' % i] = numpy.full(self.number_of_agents, 0, dtype=int)
