from trafficSimulator import *

# Create simulation
sim = Simulation()

# Add multiple roads
sim.create_roads([

    #cross roads
    ((150, 200), (150, 300)), #vertical middle, 0
    ((150, 300), (150, 420)),
    ((0, 300), (150, 300)), #horizontal middle, 2
    ((150, 300), (300, 300)),  

    #circuit
    ((20, 200), (150, 200)), #top, 4
    ((150, 200), (280, 200)),  

    ((300, 220), (300, 300)), #right 6
    ((300, 300), (300, 400)),

    ((280, 420), (150, 420)), #bottom 8
    ((150, 420), (20, 420)), 

    ((0, 400), (0, 300)),   #left, 10
    ((0, 300), (0, 220)),

    *curve_road((280, 200), (300, 220), (300, 200)), #top to right, 12-26
    *curve_road((300,400), (280, 420), (300, 420)), # right to bottom 27-41 
    *curve_road((20,420), (0, 400), (0, 420)),  #bottom to left , 42- 56
    *curve_road((0,220), (20, 200), (0, 200))   #left to top , 57-71
])

sim.create_gen({
    'vehicle_rate': 10,
    'vehicles': [
        [1, {"path": [4, 5, *range(12, 26), 6, 7, *range(27, 41), 8, 9, *range(42, 56), 10, 11, *range(57, 71), 4, 5, *range(12, 26), 6, 7, *range(27, 41), 8, 9, *range(42, 56), 10, 11, *range(57, 71), 4, 0, 1]}],
        [1, {"path": [4, 5, *range(12, 26), 6, 7, *range(27, 41), 8, 9, *range(42, 56), 10, 2, 3, 7, *range(27, 41), 8, 9, *range(42, 56), 10, 11, *range(57, 71), 4, 0, 1]}],
        [1, {"path": [0, 3, 7, *range(27, 41), 8, 9, *range(42, 56),10, 2, 1]}],
        [1, {"path": [0, 1, 9, *range(42, 56),10, 2, 1]}],
        [1, {"path": [0, 1, 9, *range(42, 56),10, 11, *range(57, 71), 4, 5, *range(12, 26), 6, 7, *range(27, 41), 8, 9, *range(42, 56), 10, 2, 3]}]
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