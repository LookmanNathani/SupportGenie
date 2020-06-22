# Solution to Exercise 2
import random

class Agent:
    def __init__(self, name, is_available, available_since, role):
        self.name = name
        self.is_available = is_available
        self.available_since = available_since
        self.role = role

class Issue:
    def __init__(self, name, selection_mode):
        self.name = name
        self.selection_mode = selection_mode

def assign_agents(list_of_agents, name, selection_mode):
    eligible_agents = []
    selection_mode = selection_mode.lower().rstrip()

    if selection_mode == 'all_available':
        for agent in list_of_agents:
            if agent.role == name and agent.is_available is True:
                eligible_agents.append(agent)
        return eligible_agents

    if selection_mode == 'least_busy':
        eligible_agents = []
        available_since = []
        for agent in list_of_agents:
            if agent.role == name and agent.is_available is True:
                available_since.append(agent.available_since)
        for agent in list_of_agents:
            if agent.role == name and agent.available_since == max(available_since) and agent.is_available is True:
                eligible_agents.append(agent)
                return eligible_agents

    if selection_mode == 'random':
        eligible_agents = []
        random_agent = random.choice(list_of_agents)
        for _ in list_of_agents:
            if random_agent.role == name and random_agent.is_available is True:
                eligible_agents.append(random_agent)
                return eligible_agents
            else:
                random_agent = random.choice(list_of_agents)
        return eligible_agents

if __name__ == '__main__':
    # Creating list of agents
    agent1 = Agent('John', True, 3, 'sales')
    agent2 = Agent('Jack', False, 0, 'sales')
    agent3 = Agent('Marie', True, 1, 'spanish_speaker')
    agent4 = Agent('Anne', True, 0, 'support')
    agent5 = Agent('Bob', False, 7, 'spanish_speaker')
    agent6 = Agent('Justin', True, 6, 'support')
    agent7 = Agent('Conor', True, 14, 'sales')
    agent8 = Agent('Zain', False, 2, 'support')
    agent9 = Agent('Julie', True, 5, 'support')
    agent10 = Agent('Daren', True, 0, 'sales')

    list_of_agents = [agent1, agent2, agent3, agent4, agent5, agent6, agent7, agent8, agent9, agent10]

    # Creating list of issues
    issue1 = Issue('sales', 'all_available')
    issue2 = Issue('spanish_speaker', 'least_busy')
    issue3 = Issue('support', 'random')
    issue4 = Issue('spanish_speaker', 'all_available')

    issues = [issue1, issue2, issue3, issue4]

    # Passing each issue to the Agent Selector
    for issue in issues:
        result = assign_agents(list_of_agents, issue.name, issue.selection_mode)
        if result:
            print('List of eligible agents for',issue.name,'which is',issue.selection_mode)
            for value in result:
                print(value.name)
        else:
            print('No eligible agent available for',issue.name)

