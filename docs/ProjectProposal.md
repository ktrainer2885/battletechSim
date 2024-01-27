# Project Proposal: BattleTech Simulator  
Date: 19 June 2023  
Author: Rogelio Ramirez

## Executive Summary:  
I am proposing to create a BattleTech Simulator. This piece of software will perform simplified combat between BattleMechs and record the results for later analysis. The software aims to be easy and friendly to operate. This will allow the users to simulate different a number of times to see the probability of the match easily. The results will contain detailed log the fight.

## Background:
BattleTech is a modern tabletop game that dates back to the mid 1980's and is still played today. It involves the players controlling giant robots that have pilots inside of them.  

The players take turns moving and attacking each other. The game has a variety of rules for the mechs, such as weight and weapons loadouts. Each turn the player will move their mech and attack the opposing player's mech. The first player will roll dice to determine if any weapon attacks hit, and where they hit. The player that got hit will tick off damage on a sheet of paper known as a record sheet. The damage will be applied to armor and later on the internal structure of the mech. 

These variables and others will influence the outcome of the battle.

## Project Overview:
This project is trying to solve the issue of determining the odds of winning in a BattleTech game.

The project plans on simulating two forces fighting each other using the BattleTech rules as a basis. There will be some simplifications, but the odds should be reasonable. The simulations will be programmed to follow a basic combat algorithm that will run until the end of combat.

The BattleTech Simulator will run the specific combat simulation multiple times and give the result of a force winning. The simulator will record all the fights in a log file(s), as well as the a log of all the fights for that simulation.


## Objectives:
- Develop a BattleTech Simulator that enables users to simulate combat between teams of Mechs.
- Provide a simplified version of the BattleTech rules focused on the 3025 time period, essentially beginner rules.
- Allow users to set up battles with up to 4 versus 4 Mechs.
- Record the results of each simulation in a log file.
- Record the results of multiple simulations of the same battle in a log file.
- Provide an intuitive user interface for easy navigation and interaction.

## Scope:  
The following features will be implemented:
- The user will be able to select forces from the 3025 era.
- The software should have ability to do a lance on lance battle. (4 v 4)
- Any terrain features will not be implented. (Line of Sight, Woods, Elevation, etc.)
- The user will be able to change the skill level of the pilots
- Log files should include the mechs that were used, as well as a break-down round after round of damage inflicted.
- Technology will be at the 3025 timeline. No advanced technology will be initially implemented.
- Armor, and internal structure will be modeled accurate.
- Critical hit locations will be modeled accurately. 
- Critical hits will be modeled, including ammo explosions
- Pilot health, skills and modifiers from wounds will be modeled. 
- Weapons will be accurately modeled. (missile dispersion, hit location)

## Deliverables:
- A fully functional simulator. (Specifics will in the requirements document)
- Documentation for the whole project. This includes any system design documents, this document, requirements etc.
- Source code

## Timeline:
Due to the ambitious nature fo this project, a conservative timeline will be used. It is anticipated that the primary developers job will slow down development dramatically.

- June 18-July 3 2023- Requirements gathering and analysis
- ~~July 4- 17 2023- Design documents and architecture~~
- ~~July 17 - Dec 20- Creation of the simulator. Using Agile like methodology (2-week sprints)~~
- ~~Jan 8 - 17 2024- Deployment and Release.~~
- TBD (27 JAN 2024)

## Stakeholders
- The primary devleoper
- Players of Battletech
