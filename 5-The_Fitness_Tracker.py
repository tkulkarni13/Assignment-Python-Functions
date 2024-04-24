# Task 1: Function to log different fitness activites and their duration

def addActivity(activity, time):
    activities.append(activity)
    duration.append(time)

# Task 2: Extimate calories burned

def caloriesBurned (time):
    return time * 3.5

# Task 3: Summary function

def summary():
    for i, a in enumerate(activities):
        print("You burned " + str(caloriesBurned(duration[i])) + " calories " + a + " for " + str(duration[i]) + " minutes")

activities = []
duration = []

addActivity('dancing', 10)
addActivity('swimming', 30)
addActivity('biking', 20)
addActivity('running', 60)
summary()