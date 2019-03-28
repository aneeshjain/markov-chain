import numpy as np
import random as random

states = ["Sleep", "Ice Cream", "Run"]

transitionName = [["SS", "SR", "SI"], ["RS", "RR", "RI"], ["IS", "IR", "II"]]

transitionMatrix = [[0.2, 0.6, 0.2], [0.1, 0.6, 0.3], [0.2, 0.7, 0.1]]

if sum(transitionMatrix[0]) + sum(transitionMatrix[1]) + sum(transitionMatrix[2]) != 3:
    print("Somewhere something went wrong, transition matrix maybe?")
    
else: print("All's good! Time to move on.")

def activity_forecast(days):
    activityToday = "Sleep"

    print("Start state: ", activityToday)

    activityList = [activityToday]
    i = 0

    prob = 1

    while i != days:
        if activityToday == "Sleep":
            change = np.random.choice(transitionName[0], replace = True, p = transitionMatrix[0])
            print("change: ", change)

            if change == "SS":
                prob = prob * 0.2
                activityList.append(activityToday)
                pass
            elif change == "SR":
                prob = prob*0.6
                activityToday = "Run"
                activityList.append(activityToday)

            else:
                prob = prob*0.2
                activityToday = "Ice Cream"
                activityList.append(activityToday)
        
        elif activityToday == "Run":
            change = np.random.choice(transitionName[1], replace = True, p = transitionMatrix[1])
            print("change: ", change)

            if change == "RR":
                prob = prob*0.6
                activityList.append(activityToday)
                pass

            elif change == "RS":
                prob = prob*0.1
                activityToday = "Sleep"
                activityList.append(activityToday)
            else:
                prob = prob*0.3
                activityToday = "Ice Cream"
                activityList.append(activityToday)

        elif activityToday == "Ice Cream":
            change = np.random.choice(transitionName[2], replace = True, p = transitionMatrix[2])
            print("change: ", change)

            if change == "II":
                prob = prob*0.1
                activityList.append(activityToday)
                pass

            elif change == "IS":
                prob = prob*0.2
                activityToday = "Sleep"
                activityList.append(activityToday)
            else:
                prob = prob*0.7
                activityToday = "Run"
                activityList.append(activityToday)
        i += 1

    print("Possible States: ", str(activityList))
    print("End State after " + str(days) + " days: " + activityToday)
    print("Probability of the possible sequence of states: " + str(prob))

activity_forecast(3)