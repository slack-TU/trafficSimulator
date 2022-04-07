from trafficSimulator import *

# Create simulation
sim = Simulation()

# Add multiple roads
sim.create_roads([

    #entry roads
    ((0, -400), (0, -302)), #top entry 0
    ((-400, 0), (-302, 0)), #left entry  1

    #cross roads
    ((0, -298), (0, -2)), #top vertical 2
    ((0, 2), (0, 298)), #bottom verical 3

    ((-298, 0), (-2, 0)), #left horizontal 4
    ((2, 0), (298, 0)), #right horizontal 5


    #circuit
    ((2, -300), (300, -300)), #6

    ((300, -300), (300, -2)), #22 7
    ((300, 2), (300, 300)), #23  8

    ((300, 300), (2, 300)), #39 9
    ((-2,300), (-300, 300)), #40 10

    ((-300, 300), (-300, 2)), #56 11
    ((-300, -2), (-300, -300)), #57 12

    ((-300, -300), (-2, -300)), #73 13

    #exit roads
    ((0, 302), (0, 400)), #bottom exit 74 14
    ((302, 0), (400, 0)), # right exit 75 15

])

sim.create_gen({
    'vehicle_rate': 50,
    'vehicles': [
        [1, {"path": [0, *range(6, 14), 2, 5, 15]}], #top entry full circle, verical road right exit
        [1, {"path": [1, 4, 3, *range(10, 14), *range(6, 12), 4, 5, 15]}],
        [1, {"path": [0, 2, 3, *range(10, 14), *range(6, 12), 4, 3, 14]}],
        [1, {"path": [1, 12, 13, *range(6, 14), 2, 3, 14]}],

    ]
})

#signals
sim.create_signal([[2], [4]])
sim.create_signal([[0], [13]])
sim.create_signal([[3], [9]])
sim.create_signal([[1], [11]])
sim.create_signal([[5], [7]])

# Start simulation
win = Window(sim)
win.offset = (0, 0)
win.run(steps_per_update=5)
