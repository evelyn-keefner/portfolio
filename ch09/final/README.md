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
3. Infinite map; the game loads a 3x3 chunk around the player at all times and emulates an infinitely expansive area.
4. Replayability & Ending Screen; When the player either wins by surviving for 10 minutes or dies to the enemies, an ending screen gives the player the option to try again or to exit 
5. Animation System; The player and the enemies are animated by using loaded images from the assets folder

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

Weapon
    Handles multiple weapon types

Spawner
    Handles enemy spawning and incremental scaling of difficulty

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Program          | GUI Window Appears with a start screen |
|  2                   | click start button   | display changes scene to a flat grid and a player in the center with enemy sprites spawning in around the player, there is constant updating information in the top left | 
| 3                    | click W, A, S, D keys| Player sprites should move up, left, down, right respectively |
| 4                    | Walk near enemy      | Enemy should begin heading in the direction of the player and the player should begin firing bullets |
| 5                    | Enemy dies from bullet | The enemy should drop an experience orb that can be picked up and the xp display in the top left should update respectively |
| 6                    | Player surpasses maximum xp for their level | The game switches scene and the player is presented 3 options, the game in the back is frozen |
| 7                    | Player selects powerup | The corresponding statistic should increase or decrease and influence the game directly, given the player only levels up once the game returns back to the main loop, if the player levels up multiple times they are given the option to choose another powerup |
| 8                    | Player runs into enemy | Player heatlh decreases |
| 9                    | Player health is 0     | Game end screen appears, with option to quit or restart |
| 10                   | Restart button pressed | Game restarts | 
| 11                   | Quit button pressed    | Game window closes |
| 12                   | Q is pressed during main loop | Game window closes |
| 13                   | Time ticks to 0        | A win screen is presented with the options to quit or restart
