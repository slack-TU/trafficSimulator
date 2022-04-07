from trafficSimulator import *

# Create simulation
sim = Simulation()

# Add multiple roads
sim.create_roads([

    #entry roads
    ((0, -400), (0, -302)), #top entry 0
    ((-400, 0), (-302, 0)), #left entry  1

    #circuit
    ((2, -300), (300, -300)), #2

    ((300, -300), (300, -2)), # 3
    ((300, 2), (300, 300)), # 4

    ((300, 300), (2, 300)), #5
    ((-2,300), (-300, 300)), #6

    ((-300, 300), (-300, 2)), #7
    ((-300, -2), (-300, -300)), #8

    ((-300, -300), (-2, -300)), #9

    #exit roads
    ((0, 302), (0, 400)), #bottom exit 10
    ((302, 0), (400, 0)), # right exit 11

])

sim.create_gen({
    'vehicle_rate': 50,
    'vehicles': [
        [1, {"path": [0, *range(2,10), *range(2,10), *range(2,10), *range(2,10), *range(2,10), *range(2,10), *range(2,10), *range(2,10), 2, 3, 11]}], #top entry full circles,  right exit
        
    ]
})

#signals


# Start simulation
win = Window(sim)
win.offset = (0, 0)
win.run(steps_per_update=5)
