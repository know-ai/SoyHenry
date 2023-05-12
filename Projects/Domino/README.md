# Domino Game

Dominoes is a family of tile-based games played with gaming pieces. Each domino is a rectangular tile, usually with a line dividing its face into two square ends. Each end is marked with a number of spots (also called pips or dots) or is blank. The backs of the tiles in a set are indistinguishable, either blank or having some common design. The gaming pieces make up a domino set, sometimes called a deck or pack. The traditional European domino set consists of 28 tiles, also known as pieces, bones, rocks, stones, men, cards or just dominoes, featuring all combinations of spot counts between zero and six. A domino set is a generic gaming device, similar to playing cards or dice, in that a variety of games can be played with a set. Another form of entertainment using domino pieces is the practice of domino toppling.

# Goal

The goal of this project is to develop an algorithm that simulates being a domino player in order to win a game.

# Premise

Although the game has a logic behind it, it is intended to simulate as many game scenarios as possible, so that with that information, a data-based algorithm can be generated.

# Development Porposal

To achieve the objective, it is proposed to create a project divided into 2 sections.

## App

Create a service that simulates the game of dominoes, initially with 2 deployment modes

- Generate
- Test

### Generate Mode

This mode will create as play scenarios as possible to generate enough data to train de model.

### Test

This mode will test any model create in the *Model Section* in some play scenarios.

## Pipeline

This section aims to automate the ETL, Preprocessing and Model Creation stages according to the data generated in the application

### ETL

This package aims to load the data generated in the simulations of the game scenarios, and apply the necessary techniques to prepare the data for the preprocessing stage. 

### Preprocessing

This package aims to prepare the data according to the AI algorithm selected.

### Model

This package aims to create the algorithm based on data.