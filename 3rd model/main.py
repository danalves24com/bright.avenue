import matplotlib.pyplot as plt
import random
import string
tlog=[]
random.seed(10529)
road                = 400000 #meters
lanes               = 4
carsOnRoad          = 150
safeDistance        = 8
maxSpeed            = 140 #kmph
timePeriodToMonitor = 300 #seconds
cars                = []

decay = []
velocities = []


carsLocation = []
class newVehicle:
    def __init__(self, x, y, speed):
        self.id = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(20))
        self.x = x
        self.y = y 
        self.speed = speed
        self.carsAhead = 0
for car in range(carsOnRoad):
   cars.append(newVehicle(random.randint(0, int(road*0.80)), random.randint(0, lanes), random.randint(80, 130)))
fig, ax = plt.subplots()
def updateView(title, index):
    plt.cla()
    print(title)
    currentVelocities = []
    for car in cars:
        #plt.figure(index)
        plt.scatter(car.x, car.y, marker="4", label=car.speed)        
        plt.title(title)
        plt.ylabel("Car lanes")
        plt.xlabel("1m spaces")
        currentVelocities.append(car.speed)
        if len(cars) <= 30:
            plt.legend()
    plt.pause(0.01)
    velocities.append(currentVelocities)
updateView("INITIAL CAR LAYOUT", -1)
def project():
    for t in range(timePeriodToMonitor):        
        for car in cars:
            car.carsAhead = 0
            if car.x >= road:
                cars.remove(car)
            else:
                for otherCar in cars:
                    if (otherCar.x >= car.x) and (otherCar.y == car.y):
                        car.carsAhead+=1
                    if (otherCar.x >= car.x+safeDistance) and (otherCar.y == car.y):
                        car.speed = otherCar.speed-10
                        car.x += car.speed*0.2777777778
                    elif otherCar.x+safeDistance >= car.x+(int(safeDistance/2)):
                        car.speed = otherCar.speed
                        car.x += car.speed*0.2777777778
                    elif car.carsAhead == 0:
                        car.speed = maxSpeed
                    else:
                        car.x += car.speed*0.2777777778
        title = f"projection #{t} t={t} onScreen={len(cars)}"        
        updateView(title, t)
        tlog.append(f"------ t={t} | onScreen={len(cars)} \n")
        decay.append(len(cars))
        for c in cars:
            tlog.append(f"{c.id} -- X:{c.x}, Y:{c.y}, V:{c.speed}, Ahead:{c.carsAhead} \n")
    plt.show()
tlog.append(f"ROAD: {road}, LANES: {lanes}, CARS: {carsOnRoad}, MAX_SPEED: {maxSpeed}, MONITOR_PERIOD: {timePeriodToMonitor} \n")
project()
with open('TrafficLog.txt', 'w') as f:    
    f.writelines(tlog)
plt.plot(decay)
plt.title("Cars on Road")
plt.show()
