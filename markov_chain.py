import numpy as np
import random as random

states = ["Hot", "Cold", "Tepid"]

transitionName = [["HH", "HT", "HC"], ["TH", "TT", "TC"], ["CH", "CT", "CC"]]

transitionMatrix = [[0.2, 0.6, 0.2], [0.1, 0.6, 0.3], [0.2, 0.7, 0.1]]

if sum(transitionMatrix[0]) + sum(transitionMatrix[1]) + sum(transitionMatrix[2]) != 3:
    print("Somewhere something went wrong, transition matrix maybe?")
    
else: print("All's good! Time to move on.")

def state_forecast(days):
    stateToday = "Hot"

    print("Start state: ", stateToday)

    stateList = [stateToday]
    i = 0

    prob = 1

    while i != days:
        if stateToday == "Hot":
            change = np.random.choice(transitionName[0], replace = True, p = transitionMatrix[0])
            print("change: ", change)

            if change == "HH":
                prob = prob * 0.2
                stateList.append(stateToday)
                pass
            elif change == "HT":
                prob = prob*0.6
                stateToday = "Tepid"
                stateList.append(stateToday)

            else:
                prob = prob*0.2
                stateToday = "Cold"
                stateList.append(stateToday)
        
        elif stateToday == "Tepid":
            change = np.random.choice(transitionName[1], replace = True, p = transitionMatrix[1])
            print("change: ", change)

            if change == "TT":
                prob = prob*0.6
                stateList.append(stateToday)
                pass

            elif change == "TH":
                prob = prob*0.1
                stateToday = "Hot"
                stateList.append(stateToday)
            else:
                prob = prob*0.3
                stateToday = "Cold"
                stateList.append(stateToday)

        elif stateToday == "Cold":
            change = np.random.choice(transitionName[2], replace = True, p = transitionMatrix[2])
            print("change: ", change)

            if change == "CC":
                prob = prob*0.1
                stateList.append(stateToday)
                pass

            elif change == "CH":
                prob = prob*0.2
                stateToday = "Hot"
                stateList.append(stateToday)
            else:
                prob = prob*0.7
                stateToday = "Tepid"
                stateList.append(stateToday)
        i += 1

    print("Possible States: ", str(stateList))
    print("End State after " + str(days) + " days: " + stateToday)
    print("Probability of the possible sequence of states: " + str(prob))

state_forecast(4)