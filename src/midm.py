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
    ((2, -300), (250, -300)), #6
    *curve_road((250, -300), (300, -250), (300, -300)), #top to right, 7 - 21
    ((300, -250), (300, -2)), #22

    ((300, 2), (300, 250)), #23 
    *curve_road((300, 250), (250, 300), (300, 300)), #24-38 right to bottom
    ((250, 300), (2, 300)), #39

    ((-2,300), (-250, 300)), #40
    *curve_road((-250, 300), (-300, 250), (-300, 300)), #41-55 bottom to left
    ((-300, 250), (-300, 2)), #56

    ((-300, -2), (-300, -250)), #57
    *curve_road((-300, -250), (-250, -300), (-300, -300)), #58-72 left to top
    ((-250, -300), (-2, -300)), #73

    #exit roads
    ((0, 302), (0, 400)), #bottom exit 74
    ((302, 0), (400, 0)), # right exit 75

])

sim.create_gen({
    'vehicle_rate': 20,
    'vehicles': [
        [1, {"path": [0, *range(6, 74), 2, 3, 74]}], #top entry full circle, verical road bottom exit
        [1, {"path": [0, *range(6, 74), *range(6, 57), 4, 5, 75]}], #top entry, full circle, three quarter to horizontal road, right exit
        [1, {"path": [1, *range(57, 74), *range(6, 74), 2, 3, 74]}], #left entry, quarter circle, full circle, verical road bottom exit
        [1, {"path": [1, *range(57, 74), *range(6, 57), 4, 5, 75]}], #left entry, full circle, horizontal road right exit
        [1, {"path": [0, 2, 3, *range(40, 74), 2, 3, 74]}],
        [1, {"path": [1, 4, 5,  *range(23, 57), 4, 5, 75]}],
        [1, {"path": [0, 2, 3, *range(40, 74), *range(6, 57), 4, 5, 75]}],
        [1, {"path": [1, 4, 5,  *range(23, 74), 2, 3, 74]}]
    ]
})

#signals
sim.create_signal([[2], [4]])
sim.create_signal([[0], [73]])
sim.create_signal([[3], [39]])
sim.create_signal([[1], [56]])
sim.create_signal([[5], [22]])

# Start simulation
win = Window(sim)
win.offset = (0, 0)
win.run(steps_per_update=5)
