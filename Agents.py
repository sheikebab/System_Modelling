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

    def Update_Trust_Citizens(self, agent_df, time_period):
        #Initialise lists for average trust
        self.avg_black_trust = []
        self.avg_white_trust = []
        self.avg_asian_trust = []
        self.avg_hispanic_trust = []
        self.daily_avg = []
        #Initialising for loop to simulate timeline of defined time period
        for i in range(time_period):
            #the initialised variables change in every time period, affect on community varies daily
            zeta = numpy.random.rand(1)
            community_happiness = numpy.random.randint(0, 4)
            alpha = numpy.random.rand(1)
            beta = 0.2
            agent_df['Policed On'] =agent_df['Policed On'] + numpy.random.choice([0,1], self.number_of_agents,
                                                                                              p=[0.998, 0.002])
            agent_df['T+%d' % i] = numpy.full(self.number_of_agents, 0, dtype=int)
            #initialising for loop to go through each agent in dataframe
            for j in range(self.number_of_agents):
                #Simulated bias of cops towards black and hispanic peopel
                if agent_df.Race[j] == 'Black' or agent_df.Race[j] == 'Hispanic':
                    agent_df.loc[j, 'Policed On'] = agent_df.loc[j, 'Policed On'] + numpy.random.choice([0,1],
                                                                                                    p = (0.996, 0.004))
                #Initialed trust in time period T+0
                if i == 0:
                    if agent_df.Race[j] == 'Black':
                        agent_df.loc[j, 'T+%d' % i] = agent_df['Initial Trust'][j]
                    elif agent_df.Race[j] == 'White':
                        agent_df.loc[j, 'T+%d' % i] = agent_df['Initial Trust'][j]
                    elif agent_df.Race[j] == 'Asian':
                        agent_df.loc[j, 'T+%d' % i] = agent_df['Initial Trust'][j]
                    else:
                        agent_df.loc[j, 'T+%d' % i] = agent_df['Initial Trust'][j]
                else:
                    if agent_df.Race[j] == 'Black':
                        agent_df.loc[j, 'T+%d' % i] = agent_df['T+%d' % (i - 1)][j] - \
                                                            agent_df['Policed On'][
                                                                j] * alpha + community_happiness - \
                                                            agent_df['Size of Social Network'][j] * beta
                    elif agent_df.Race[j] == 'White':
                        agent_df.loc[j, 'T+%d' % i] = agent_df['T+%d' % (i - 1)][j] - \
                                                            agent_df['Policed On'][
                                                                j] * alpha + community_happiness - \
                                                            agent_df['Size of Social Network'][j] * beta + zeta
                    elif agent_df.Race[j] == 'Asian':
                        agent_df.loc[j, 'T+%d' % i] = agent_df['T+%d' % (i - 1)][j] - \
                                                            agent_df['Policed On'][
                                                                j] * alpha + community_happiness - \
                                                            agent_df['Size of Social Network'][j] * beta
                    else:
                        agent_df.loc[j, 'T+%d' % i] = agent_df['T+%d' % (i - 1)][j] - \
                                                            agent_df['Policed On'][
                                                                j] * alpha + community_happiness - \
                                                            agent_df['Size of Social Network'][j] * beta
            agent_df['Final Trust'] = agent_df['T+%d' % i]
            self.avg_asian_trust.append(agent_df.ix[lambda s: agent_df.Race == 'Asian']['T+%d' % i].mean())
            self.avg_black_trust.append(agent_df.ix[lambda s: agent_df.Race == 'Black']['T+%d' % i].mean())
            self.avg_hispanic_trust.append(agent_df.ix[lambda s: agent_df.Race == 'Hispanic']['T+%d' % i].mean())
            self.avg_white_trust.append(agent_df.ix[lambda s: agent_df.Race == 'White']['T+%d' % i].mean())
            self.daily_avg.append(agent_df['T+%d' % i].mean())