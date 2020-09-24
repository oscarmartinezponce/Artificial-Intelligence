from environtments.environment import Environment
from environtments.floor import Floor
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

print()

print(e)
print(e.__len__())

floor = Floor(2, 5)

print(floor.__len__())
print(floor)

print(floor.rows)
print(floor.columns)
floor.dirty_squares()
print(floor)

