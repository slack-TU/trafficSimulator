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

    #entry roads
    ((150, 0), (150, 200)), #12 top entry
    ((-150, 300), (0, 300)), #13 left entry

    #exit roads
    ((150,300), (150, 450)), #14 bottom exit
    ((300,300), (330, 300)), #15 right exit


    *curve_road((280, 200), (300, 220), (300, 200)), #top to right
    *curve_road((300,400), (280, 420), (300, 420)), # right to bottom 
    *curve_road((20,420), (0, 400), (0, 420)),  #bottom to left 
    *curve_road((0,220), (20, 200), (0, 200))   #left to top 
])

sim.create_gen({
    'vehicle_rate': 10,
    'vehicles': [
        #[1, {"path": [12, 5, *range(16, 30), 6, 7, *range(31, 45), 8, 9, *range(46, 60), 10, 11, *range(61, 75),
        #4, 5, *range(16, 30), 6, 7, *range(31, 45), 8, 9, *range(46, 60), 10, 11, *range(61, 75), 4, 0, 1, 14]}], #two loops, then exit on vertical road
        #3[1, {"path": [12, 5, *range(16, 30), 6, 7, *range(31, 45), 8, 9, *range(46, 60), 10, 11, *range(61, 75),
        #4, 5, *range(16, 30), 6, 7, *range(31, 45), 8, 9, *range(46, 60), 10, 2, 3, 15]}], #one loop, then travel to horizontal road and exit
        #[1, {"path": [12, 0, 1, 9, *range(46, 60), 10, 2, 3, 7, *range(31, 45), 8, 9, *range(46, 60), 10, 11, *range(61, 75), 4, 0, 1, 14 ]}], # take vertical road, then travel and take horizontal road, then travel back to vertical road and exit
        #[1, {"path": [13, 2, 1, 9, *range(46, 60), 10, 11, *range(61, 75), 4, 0, 1, 14]}],
        [1, {"path": [13, 11, *range(61, 75), 4, 5, *range(16, 30), 6, 7, *range(31, 45), 8, 9, *range(46, 60), 10, 11, *range(61, 75),  4, 5, *range(16, 30), 6, 15]}]

    ]
})

sim.create_signal([[0], [2]])
sim.create_signal([[1], [8]])
sim.create_signal([[6], [3]])
sim.create_signal([[12], [4]])
sim.create_signal([[13], [10]])




# Start simulation
win = Window(sim)
win.offset = (-150, -210)
win.run(steps_per_update=5)