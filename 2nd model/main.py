import random
import string
import matplotlib.pyplot as plt

road = 500000
lanes = 6
safeDistance = 5
carsInRange = 60

class Vehicle:
    def __init__(self, speed, originX, originY, destinationX, destinationY):
        self.id = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(20))
        self.x = originX
        self.y = originY
        self.originX = originX
        self.originY = originY
        self.destinationX = destinationX
        self.destinationY = destinationY
        self.speed = speed
        self.trip = destinationY-originY
        if destinationX >= originX:
            self.destionationToCurrentXDifference = destinationX-originX
        elif originX >= destinationX:
            self.destionationToCurrentXDifference = originX-destinationX
        self.duration = int(destinationY-originY/(speed*0.2777777778))
        self.laneChanges = []    
        self.generatedCarTrip = []
cars = []    
for car in range(carsInRange):
    cars.append(Vehicle(random.randint(80, 130), random.randint(1, lanes), random.randint(0, int(road/2)), random.randint(1, lanes), random.randint(int(road/2), road)))

def lanesCalculation():
    for car in cars:
        for change in range(car.destionationToCurrentXDifference):
            try:
                car.laneChanges.append(int(change*(car.trip/car.destionationToCurrentXDifference)))
            except:
                car.laneChanges.append(0)

        #print(car.laneChanges)        

def tripGeneration():
    for t in range(road):
        for car in cars:
            while car.y <= car.destinationY:      
                lanesChanged = 0
                for s in range(car.duration): 
                    if car.destionationToCurrentXDifference >= 1:
                        if lanesChanged <= car.destionationToCurrentXDifference:
                            print(f"more then 1: {car.destionationToCurrentXDifference}")
                            print(car.y, car.laneChanges, lanesChanged)
                            if car.laneChanges[lanesChanged] >= car.y:
                                car.x = int(car.x+1)
                                print(car.x)
                                lanesChanged+=1
                                car.y+=int(car.speed*0.2777777778)
                                print(f"lanes changed {lanesChanged} for {car.destionationToCurrentXDifference} at {car.y}")

                            #print(car.id, car.x, car.y, car.trip)
                            else:
                                car.y+=int(car.speed*0.2777777778)
                        else:
                            break
                    car.generatedCarTrip.append([car.x, car.y])
            else:
                break   
                #print(f"{car.id} is out of range")


lanesCalculation()
tripGeneration()
for car in cars:
    #print(car.generatedCarTrip)
    x = []
    y = []
    for ar in car.generatedCarTrip:
        x.append(ar[0])
        y.append(ar[1]) 
        print(ar[0], ar[1])
    plt.plot(y, x)

plt.show()    