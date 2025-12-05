# Swarm Computing
## CS110  Final Project  Fall, 2025

## Team Members

Benji Lin, Evelyn Keefner, Jade Felske

***

## Project Description

Our project is our take on a "Vampire Survivors-Like" Roguelike game.
The player's goal is to survive for 10 minutes while facing a horde of enemies.
The player will be able to upgrade themselves with the experience gained from defeating enemies.
The enemy's difficulty increases as time goes on.

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Enemies; the enemies become more difficult (i.e. more health) over time.
2. Upgrades; the player can upgrade themselves or weapons from xp
3. Infite map; the game loads a 3x3 chunk around the player at all times and emulates an infinitely expansive area.
4. << Feature 4 >>
5. << Feature 5 >>

### Classes

CameraGroup
    CameraGroup handles both the generation of the background and ground, along with handling the camera code

Player
    The Player class contains all data related to the player, such as health and speed. The player class handles player movement along with 

Enemy
    The Enemy class

Spawner
    Handles enemy spawning and difficulty scaling over time.

Experience
    Renders the experience that appears from defeated enemies and it's interaction with the player.

Bullet
    Bullet class manages bullet data and it's interaction with enemies.

Powerup
    Handles how powerups are applied to the player.

Button
    Used to render the buttons used for the start screen and the upgrade screen.

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
etc...
