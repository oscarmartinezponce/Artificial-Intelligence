from environtments.environment import Environment
from agents.agent import Agent

e = Environment()

print(e)
print(e.__len__())

a = Agent()

e.add_agent(a)
print(e)
print(e.__len__())


a2 = Agent()
try:
    e.remove_agent(a2)
except ValueError as i:
    print("Error")



print(e)
print(e.__len__())

