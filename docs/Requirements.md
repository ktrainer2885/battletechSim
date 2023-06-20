# BattleTech Simulator Requirements  
Date: 19 June 2023  
Author: Rogelio Ramirez

## 1. Introduction
The BattleTech Simulator is a software application that is meant to simulate a 4 v 4 combat of battlemechs and provide the odds of winning. The software will use a simplified combat rules to simulate the combat. At the end of all the simulations, the software will output log files showing the combat results and a summary showing the odds of winning os loosing. 

## 2. Requirements
### 2.1 User Requirements
- The user will be able to select forces from the 3025 era.
- The software should have ability to do a lance on lance battle. (4 v 4)
- Any terrain features will not be implemented. (Line of Sight, Woods, Elevation, etc.)
- The user will be able to select the skill level of the pilots
- Log files should include the mechs that were used, as well as a break-down round after round of damage inflicted.
- Technology will be at the 3025 timeline. No advanced technology will be initially implemented.
- Armor, and internal structure will be modeled accurately.
- Critical hit locations will be modeled accurately.
- Critical hits will be modeled, including ammo explosions
- Pilot health, skills and modifiers from wounds will be modeled.
- Weapons will be accurately modeled. (missile dispersion, hit location)
- Ammo will be modeled accurately.
- Heat will be modeled accurately.
- A combat algorithm will be used for all the mechs initially.
- The user will be able to select the number of simulations to run.

### 2.2 System Requirements
- The software will be written in Python 3.X+ (Exact version TBD)
- The software will be able to be run on Windows 10.
- The software should not take more than 5 minutes to run 1000 simulations.
- The software should be deployed as a single executable file.
- The software will be a GUI interface.
- The software will output its logs to a text file.
- The software will output a summary of the results to a text file.
- The software will place the outputs in a default directory.
- The software will allow the user to customize the output directory.
- The software will have a default directory for the user to place the input files.
- The software will read the mech files from MegaMekLab. (They are text based files)

### 2.3 Non-Functional Requirements
- The software should be user-friendly and intuitive.
- The software will optimize the algorithm to run as fast as possible.
- The software will have a simple GUI interface.
- The software will be well documented, providing clear instructions on how to use it.

# 3. Constraints
- The software will only support the 3025 era initially.
- The software will not support any advanced technology, including "LostTech" from the Star League era.
- Catlyst Game Labs currently have custody of the BattleTech IP. The software will not be sold or distributed for profit.
- The software will not be used for any commercial purposes.

# 4. Assumptions and Dependencies
- The user is expected to have a basic knowledge of the BattleTech game.
- The project will depend on the mech files from MegaMekLab.

# 5. Future Enhancements
- The software will be able to support other eras.
- The software will be able to support other technology levels.
- The software will be able to support other combat algorithms to match with unit types.
- The software will export the results in such a way that it can be used for Machine Learning.
- The software will be able to support other game systems, such as Alpha Strike.
- The software will be able to support other game systems, such as BattleForce.
- The software will have other unit types other than mechs.
- 