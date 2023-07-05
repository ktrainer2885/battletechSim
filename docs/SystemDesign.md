# BattleTech Simulator Requirements  
Date: 4 July 2023
Author: Rogelio Ramirez

## 1. Introduction
The BattleTech Simulator is a software application that is meant to simulate a 4 v 4 combat of battlemechs and provide the odds of winning. The software will use a simplified combat rules to simulate the combat. At the end of all the simulations, the software will output log files showing the combat results and a summary showing the odds of winning os loosing. 

## 2. System Overview
The Battletech Simulator will consist of the following components:
- A GUI Interface that will allow the user to select the number of times the simulation will be used. The GUI will also allow the user to select the forces to be used in the simulation.
- A simulator class that will run all the simulations.
  - This may be even more classes focusing on each aspect of the simulation.
    - Combat 
    - Damage 
    - Heat 
    - Pilot Skills
    - Map/Distance
- A log class that will output the results of the simulation.
  - Will include a summary of the results.
- A file reader class that will read the mech files from MegaMekLab.

## 3. System Architecture
The Battletech Simulator will be a stand alone program. It will have no need to connect to a network.  

The simulator program will start the GUI aspect.
The GUI will display the informtion for the combat.
The user will use the GUI to start the simulations.
At this point the simulator will be on autopilot as it does all the calculations.
The simulator will output the results to a log file.
The simlator will output a summary of the results to a text file and to the GUI.

Each Section shoudl be as loosely coupled as possible. This will allow for future enhancements.
To help ensure this, it should be hypothetically possible to run the simulaort without the GUI.

## 4. User Interface
 The GUI shoudl be simple and have some adornment to make it look like a BattleTech interface.
 The GUI should have the following:
 - A button to start the simulation.
 - A button to select the forces.
 - A selcection box to select the forces.
 - A box to input the number of simulations.
- a box to output the results of the simulation.
