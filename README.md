# braille-pi

## Introduction

Welcome to Braille-Pi's code! 

In this repository you will find all of the code and insfrastucture scripts needed to set up a Braille-Pi.

The main aim of the Braille-Pi is to help people learn Braille. More aims and objectives found below...

## How to run the code?

To run the main loop of the Braille-Pi head into the main.py and run the file! 

If you are on raspberry pi and have correctly connected the 6 switches to the system you will be able to interact with the system using the 6 switches. If you are on Mac you will be able to interact with the system using 6 keys on your keyboard. 

## Breakdown of code

In the src folder you will find different Python packages seperated by the main groups of braille, error_reporting, interaction, learning and tests. Go into the src folder for more info.

## Aims and Objectives

The main aim of this project is to help people of different abilities and ages to learn braille. The project will deliver a solution developed on the Raspberry Pi this is because of its flexibility and value for money. 

Another aim for this project is for it to be as low cost as possible which would mean that users from all different financial backgrounds would have access to this product. 

To add to that a further aim of the project is to make the product physically intractable by making physical hardware which the users can play around with and learn from. 

The system will aim to be a small tool which could comfortably sit on a bookcase. Then when it is time to learn it can be plugged in with ease and power up and instantly be ready to help people learn.

Finally, an aim for the project is to be tested every week with the teacher who is learning braille. This will mean that I have a user centric design and the sprints will be able to find bugs, and features to implement.

## Sound Prerequisite

The current code uses a module called espeak to sound out words. To install espeak run the following command in the terminal:

    sudo apt-get install espeak
