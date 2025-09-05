# Prisoner Simulation

A Python program that simulates the "100 Prisoners Problem" (or a generalized version).  
The simulation calculates the probability that all prisoners can find their own slip when following a specific strategy.
The aim for the program is to see how a unique and unconventional strategy can improve the odd of sucessful dramatically when compared to just choosing randomly.
This program is inspired by a video by Veritasium

[Link To Veritasium Video](https://www.youtube.com/watch?v=iSNsgj1OCLA)

---

## Features

- Simulate any number of prisoners (preferably a multiple of 10)  
- Run multiple simulation runs to estimate success probability  
- Follows the “loop-following” strategy used in the problem  

---

## Requirements

- Python 3.x  
- No additional packages required (uses built-in `random` module)  

---

## How It Works

1. Each prisoner is allowed to open half of the boxes.
2. Each prisoner starts by opening the box labeled with their number.
3. If the prisoner does not find their slip, they follow the number on the slip they just found.
4. If any prisoner fails to find their slip, the run fails.

---

## How to Run

1. Clone the repository or download the `.py` file.  
2. Open a terminal and navigate to the project folder.  
3. Run the simulation with the command:
python3 your_file_name.py
4. Enter the requested inputs:
    - Number of prisoners
    - Number of simulations
5. The program will output:
    - Number of sucessful runs
    - Number of failed runs
    - Estimated probability of success

---

## Example Output
Enter number of prisoners (preferably multiple of 10): 10
Enter number of simulation runs: 1000
Number of runs succeeded: 307
Number of runs failed: 693
Probability of success: 0.3070



