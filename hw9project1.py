#! /usr/bin/python
# Exercise No.  01
# File Name:    hw9project1.py
# Programmer:   Arthur Utnehmer
# Date: April 14, 2020
#
# Problem Statement: (what you want the code to do)
#
# Craps is a dice game played at many casinos.A player rolls a pair of normal six-sided dice. If the
# initial roll is 2, 3, or 12, the player loses. If the roll is 7 or 11, the player wins. Any other
# initial roll causes the player to "roll for point." That is, the player keeps rolling the dice until
# either rolling a 7 or re-rolling the value of the initial roll. If the player re-rolls the initial
# value before rolling a 7, it's a win. Rolling a 7 first is a loss.
# Write a program to simulate multiple games of craps and estimate the probability that the player wins.
#
# Overall Plan (step-by-step,howyou want the code to make it happen):
# 1. Ask player enter the number of rounds that they wish to simulate.
# 2. feed number of rounds into simulator.
# 3. calculate ratio of wins to looses and print it out.

import random

def startSimulation():

    numberOfRounds = int(input("This program will simulate a N number of games of crap. Please enter a number to specify the number of games you want to simulate:"))
    winsAndLoose = simulate(numberOfRounds)
    ratio = float(winsAndLoose[0]/(winsAndLoose[1]+ winsAndLoose[0]))
    print("Probability of winning is:", ratio, " out of 1.0")


def simulate(numberOfRounds):

    win = 0
    rounds = 1
    loose = 0
    roundContinue = True

    while(rounds < numberOfRounds+1):
        roll = rollDice()
        NumberOfRolls = 1
        print("Initial roll is ", roll)
        #sort into win or loose.
        if( (roll == 2) or (roll == 3) or (roll == 12) ):
            loose = loose + 1
            rounds = rounds + 1

        elif( (roll == 7) or (roll == 11)):
            win = win + 1
            rounds = rounds + 1

        #Roll for point.
        else:
            keepRolling = True
            while(keepRolling):
                rollForPoint = rollDice()
                #Roll for point untill win
                print("Roll for point for round ", rounds, "give us a roll total of:", rollForPoint)
                if((rollForPoint == 7)):
                    loose = loose + 1
                    keepRolling = False
                    rounds = rounds + 1
                elif(roll == rollForPoint):
                    win = win +1;
                    rounds = rounds + 1
                    keepRolling = False
                else:
                    keepRolling = True

        print("Number of wins:" , win , " Number of looses:" , loose, "Number of rolls per this round:", NumberOfRolls)
        NumberOfRolls = NumberOfRolls +1

    return win, loose


def rollDice():
     dice1 = random.choice([1, 2, 3, 4, 5, 6])
     dice2 = random.choice([1, 2, 3, 4, 5, 6])
     number = dice1 + dice2
     return number

startSimulation()