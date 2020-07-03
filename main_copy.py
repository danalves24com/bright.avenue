import random
import string
import matplotlib.pyplot as plt

roadRange= 100000 #range of road in meters
roadLanes = 2
safeDistance = 9 #meters apart from each other

class Vehicle:
  def __init__(self, speed, origin, originLane, destination, destinationLane, currentLane):
    self.id = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(20))
    self.speed = speed
    self.origin = origin
    self.originLane = originLane    
    self.destination = destination
    self.destinationLane = destinationLane    
    self.currentLane = currentLane
    self.trip = destination-origin
    if destinationLane >= originLane:
        self.destionationToCurrentLaneDifference = destinationLane-originLane
    elif originLane >= destinationLane:
        self.destionationToCurrentLaneDifference = originLane-destinationLane
    self.currentLocation = origin   
    self.locationMap = []
    self.Velocities = []
cars = []
for c in range(60):
    cars.append(Vehicle(random.randint(90,160), random.randint(-10,50), random.randint(1, roadLanes), random.randint(50,roadRange), random.randint(1, roadLanes) ,random.randint(1, roadLanes)))    

carsInRange = len(cars)
def getSituation():
    for car in cars:
        vehiclesBehindCar = []
        vehiclesAheadCar = []
        for vehicle in cars:
            if vehicle.currentLocation <= car.currentLocation:
                vehiclesBehindCar.append(vehicle.id)
            if vehicle.currentLocation >= car.currentLocation:
                vehiclesAheadCar.append(vehicle.id)                
        print(car.id)
        print(f"dest to current lane difference: {car.destionationToCurrentLaneDifference}")
        print(f"trip: {car.trip}")
        print(vehiclesBehindCar)
        return([car.destionationToCurrentLaneDifference, car.trip, vehiclesBehindCar, vehiclesAheadCar])
def plotDrive(car):    
    tripDuration = 0    
    while car.currentLocation <= car.destination:
        currentMPS = (car.speed*27.7778)/100
        car.currentLocation+=currentMPS
        #print(currentMPS, car.currentLocation)
        car.locationMap.append(car.currentLocation)
        tripDuration+=1
    print(f"{car.id} TRIP DURATION: {tripDuration/60}")

def generateVelocities(subject):
    for car in cars:
        for location in car.locationMap:
            car.Velocities.append(car.speed)
    for car in cars:            
        print(f"COMPARING {car.id} with {subject.id}")
        posIndex = -1
        for pos in range(len(subject.locationMap)):
            posIndex+=1
            if car.id != subject.id:
                try:                    
                    if int(subject.locationMap[pos]) >= int(car.locationMap[pos]):
                        if (subject.locationMap[pos] - car.locationMap[pos]) <= safeDistance:
                            print(f"{car.id} and {subject.id} intersect at t={pos}(s) and d={subject.locationMap[pos]}(m)")
                            if car.Velocities[pos] <= subject.Velocities[pos]:
                                augmentedSpeed = subject.Velocities[pos] -5
                                for x in range(15):
                                    subject.Velocities[pos - x] = augmentedSpeed - x
                        else:
                            s=1
                    elif int(subject.locationMap[pos]) <= int(car.locationMap[pos]):
                        if (car.locationMap[pos] - subject.locationMap[pos]) <= safeDistance:
                            print(f"{car.id} and {subject.id} intersect at t={pos}(s) and d={subject.locationMap[pos]}(m)")
                            if car.Velocities[pos] <= subject.Velocities[pos]:
                                augmentedSpeed = car.Velocities[pos] - 5
                                for x in range(15):
                                    subject.Velocities[pos - x] = augmentedSpeed - x
                        else:
                            s=1                   
                except:                
                    break
    #for car in cars:
        #print(getSituation())
def generateTransitions(car):
    try:
        transitionRange = car.trip/car.destionationToCurrentLaneDifference
        laneTransitions = []
        for x in range(car.destionationToCurrentLaneDifference):
            laneTransitions.append(transitionRange*x)
        print(laneTransitions, car.destionationToCurrentLaneDifference)
    except:
        print("straight ride")
def augmentDrive():
    for car in cars:
        plotDrive(car)  
        #print(car.locationMap)
        generateVelocities(car)
        generateTransitions(car)
        

augmentDrive()
for car in cars:
    plt.plot(car.Velocities)     
plt.show()
for car in cars:
    plt.plot(car.locationMap)     
plt.show()

