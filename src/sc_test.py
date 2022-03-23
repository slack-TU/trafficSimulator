from trafficSimulator import *

# Create simulation
sim = Simulation()

# Add multiple roads
sim.create_roads([
    ((75, 100), (75, 150)), #vertical middle, 
    ((75, 150), (75, 210)),
    ((0, 150), (75, 150)), #horizontal middle, 
    ((75, 150), (150, 150)),  

    ((10, 100), (75, 100)), #top,
    ((75, 100), (140, 100)),  
    ((150, 110), (150, 150)), #right, 
    ((150, 150), (150, 200)),
    ((140, 210), (75, 210)), #bottom, 
    ((75, 210), (10, 210)), 
    ((0, 200), (0, 150)),   #left, 
    ((0, 150), (0, 110)),

    *curve_road((140, 100), (150, 110), (150, 100)), #top to right, 
    *curve_road((150,200), (140, 210), (150, 210)), # right to bottom 
    *curve_road((10,210), (0, 200), (0, 210)),  #bottom to left 
    *curve_road((0,110), (10, 100), (0, 100))   #left to top 


])

sim.create_gen({
    'vehicle_rate': 20,
    'vehicles': [
        [1, {"path": [0, 1]}],
        [1, {"path": [0, 3]}],
        [1, {"path": [2, 3]}],
        [1, {"path": [2, 3]}]
    ]
})

sim.create_signal([[0], [2]])
sim.create_signal([[3], [6]])
sim.create_signal([[1], [8]])


# Start simulation
win = Window(sim)
win.offset = (-150, -110)
win.run(steps_per_update=5)