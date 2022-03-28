from trafficSimulator import *

# Create simulation
sim = Simulation()

# Add multiple roads
sim.create_roads([  

    #circuit
    ((4, 40), (30, 40)), #top road section moving left, id: 0
    ((30, 40), (56, 40)),  #top road section, id: 1

    ((60, 44), (60, 60)), #right road moving down, 2
    ((60, 60), (60, 80)), #3

    ((56, 84), (30, 84)), #bottom road moving right, 4
    ((30, 84), (4, 84)), #5

    ((0, 80), (0, 60)),   #left road moving upward ,6
    ((0, 60), (0, 44)), #7

    *curve_road((56, 40), (60, 44), (60, 40)), #top to right, 8-22
    *curve_road((60,80), (56, 84), (60, 84)), # right to bottom, 23 - 37
    *curve_road((4,84), (0, 80), (0, 84)),  #bottom to left, 38-52
    *curve_road((0,44), (4, 40), (0, 40))   #left to top, 53-67
])

sim.create_gen({
    'vehicle_rate': 10,
    'vehicles': [
        [1, {"path": [0, 1, 2, 3, *range(23, 37), 4, 5,
         *range(38, 52), 6, 7, *range(53, 67), 0, 1, 
         *range(8, 22), 2, 3, *range(23, 37), 4, 5,
         *range(38, 52), 6, 7, *range(53, 67) ]}] 
         #cars disappear after driving top road twice, must repeat the path

        ## ^vehicles move in sequence until they hit a corner,
        #  then move around the corner in some janky-kinda way ##
    ]
})

# Start simulation
win = Window(sim)
win.offset = (-150, -110)
win.run(steps_per_update=5)