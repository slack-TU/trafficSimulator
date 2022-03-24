from trafficSimulator import *

# Create simulation
sim = Simulation()

# Add multiple roads
sim.create_roads([

    #cross roads
    ((75, 100), (75, 150)), #vertical middle, 0
    ((75, 150), (75, 210)),
    ((0, 150), (75, 150)), #horizontal middle, 2
    ((75, 150), (150, 150)),  

    #circuit
    ((10, 100), (75, 100)), #top, 4
    ((75, 100), (140, 100)),  

    ((150, 110), (150, 150)), #right 6
    ((150, 150), (150, 200)),

    ((140, 210), (75, 210)), #bottom 8
    ((75, 210), (10, 210)), 

    ((0, 200), (0, 150)),   #left, 10
    ((0, 150), (0, 110)),

    *curve_road((140, 100), (150, 110), (150, 100)), #top to right, 12-26
    *curve_road((150,200), (140, 210), (150, 210)), # right to bottom 27-41 
    *curve_road((10,210), (0, 200), (0, 210)),  #bottom to left , 42- 56
    *curve_road((0,110), (10, 100), (0, 100))   #left to top , 57-71
])

sim.create_gen({
    'vehicle_rate': 50,
    'vehicles': [
        [1, {"path": [4, 5, *range(12, 26), 6, 7, *range(27, 41), 8, 9, *range(42, 56), 10, 11, *range(57, 71), 4, 0, 1]}],
        [1, {"path": [4, 5, *range(12, 26), 6, 7, *range(27, 41), 8, 9, *range(42, 56), 10, 2, 3]}]
    ]
})

sim.create_signal([[0], [2]])
sim.create_signal([[1], [8]])
sim.create_signal([[6], [3]])
sim.create_signal([[4], [10]])




# Start simulation
win = Window(sim)
win.offset = (-150, -110)
win.run(steps_per_update=5)