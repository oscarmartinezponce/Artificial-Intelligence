from environtments.floor import Floor
from agents.vacuum import Vacuum
from time import sleep


delay_vacuum = 2
delay_floor = 4

floor = Floor()
vacuum = Vacuum()

floor.add_agent(vacuum)

print(vacuum)

print("Iniciamos en la posición x:" + str(vacuum.pos_x) + ", y:" + str(vacuum.pos_y))
print("El piso esta limpio: " + floor.__str__())

floor.run(delay_floor)
vacuum.run(delay_vacuum, ((0, 1), (0, 0)))

while True:
    sleep(5)
    print(vacuum)
