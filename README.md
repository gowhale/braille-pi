# braille-pi

## Introduction

Welcome to Braille-Pi's code! 

In this repository you will find all of the code and insfrastucture scripts needed to set up a Braille-Pi.

The main aim of the Braille-Pi is to help people learn Braille. Currently, the system teaches characters A-Z.

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

## Hardware Prerequisites

This code works best on a Raspberry Pi 3 Model A+ running the Raspian OS. To add to that 6 switches should be attached to the Raspberry Pi's GPIO pins like so:

### Circuit Diagram

<img width="620" alt="Circuit Diagram" src="https://user-images.githubusercontent.com/32711718/118108676-30533780-b3d8-11eb-91a8-7e704b75cff5.png">

### Wiring 

<img width="620" alt="Wiring" src="https://user-images.githubusercontent.com/32711718/118108749-47922500-b3d8-11eb-9f91-c3923b6ef4a0.png">

### Bird's Eye View

<img width="620" alt="Buttons" src="https://user-images.githubusercontent.com/32711718/118108807-57116e00-b3d8-11eb-96da-4160f51bfd02.png">

## Software Prerequisites

This project uses Python 3.8.5 this project also uses additional modules which need to be installed. To install the additional modules use the following command to install all needed modules:

    pip3 install -r requirements.txt

## Sound Prerequisite

The current code uses a module called espeak to sound out words on the Raspberry Pi. To install espeak run the following command in the terminal:

    sudo apt-get install espeak

## BDD Tests Prerequisites

Please install the BDD test modules using the pip and the requirements document. 

Use the following command to install all needed modules:

    pip3 install -r requirements.txt

## Executing The Tests

Once the requirements have been satisfied run the BDD tests by running the following command:

    behave

To run unit tests run the command:

    pytest

## Future Works

 - More Lessons and Quizzes
 - More testing with users
 - More BDD and Unit Tests
 - Improvements on the Learning Algorithm
 - Actioning of Tech Debts

