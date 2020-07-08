# What Is Bright Avenue?
An algorithm to suggest optimal driver behaviour based on basic factors to optimise time on the rode and prevent unwanted situations
## about
Bright Avenue creates the perfect collective driving plan for every vehicle that it has in range. this can be used to optimize time on the road and for collison avoidance
### core of 3rd model
```
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
```
