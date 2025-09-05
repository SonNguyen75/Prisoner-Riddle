import random
def main():

    # Set the parameter for simulation
    num_prisoners = int(input("Please enter the number of prisoner you want to simulate [Preferably in multiple of 10]: "))
    num_simulations = int(input("Please enter the number of run you want simulate: "))
    num_trials = num_prisoners // 2

    # Number of simulation that failed to calculate winning probability
    num_of_runs_failed = 0
    
    for _ in range(num_simulations):

        # Generating new boxes containing random slips    
        boxes = random.sample(range(int(num_prisoners)), int(num_prisoners))

        # Running through each prisoner to proceed their run
        for current_prisoner in range(num_prisoners):

            # print("Prisoner #" + str(current_prisoner) + " begins their run")

            #Set the intial choice of box to that prisoner number  
            current_choice = int(current_prisoner)

            #A flag to know if the current prisoner choosing has failed to search for their slip, assume true until they found their own slip
            current_prisoner_failed = True

            # Each prisoner get to choose (Num Of Boxes / 2) number of boxes to open and find their slip
            for _ in range(num_trials):
                
                # Prisoner follow the strategy of opening a box, if the box does not contain the slip of their number, they open the next box with the number of the slip in the box that they just opened
                if boxes[current_choice] == current_prisoner:
                    current_prisoner_failed = False # Prisoner has found their slip
                    break

                current_choice = boxes[current_choice]
            
            if current_prisoner_failed:

                # print("Prisoner #" + str(current_prisoner) + " has failed to find their own slip! This run has failed")

                num_of_runs_failed += 1
                break
    
    print("Number of succesful runs: " + str(num_simulations - num_of_runs_failed))
    print("Number of failed runs: " + str(num_of_runs_failed))

    probability_of_succeeding = (num_simulations - num_of_runs_failed) / num_simulations
    print("Probability of success: " + str(probability_of_succeeding*100) + "%")
 
               
if __name__ == "__main__":
    main()
