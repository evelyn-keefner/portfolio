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

## ATP
Test: Start screen UI
Desc: Checks the start screen renders and functions as it should.
| Step                 |Procedure             
|----------------------|--------------------:
|  1                   | Run program          
|  2                   | Verify game instructions are present on start screen
|  3                   | Click the start button
|  4                   | Verify the user is now on the game screen
^
|Expected Results
|----------------------:
|Start screen should display simple game instructions and a button which brings user into the game screen.

Test: Player movement
Desc: Verifies player movement is functional and tied ot the right keys.
| Step                 |Procedure             
|----------------------|--------------------:
|  1                   | Run program          
|  2                   | Click the start button
|  3                   | Press W, A, S, D
|  4                   | Verify player character moves up(W), left(A), down(S), and right(D)
^
|Expected Results
|----------------------:
|Player character should move in tandem with the keys pressed.

Test: Player-enemy collision
Desc: Tests whether playe-enemy collisions have been implemented correctly.
| Step                 |Procedure             
|----------------------|--------------------:
|  1                   | Run program          
|  2                   | Click the start button
|  3                   | Note player's current health
|  4                   | Use WASD to move player into an enemy sprite
|  5                   | Verify player health has decreased from it's initial value
^
|Expected Results
|----------------------:
|Player character health should decrease when in contact with an enemy.

Test: Bullet-enemy collision
Desc: Tests whether bullet-enemy collisions have been implemented correctly>
| Step                 |Procedure             
|----------------------|--------------------:
|  1                   | Run program          
|  2                   | Click the start button
|  3                   | Player will automatically shoot bullets at the nearest enemy
|  4                   | Verify that the enemy "dies" after an amount of bullets have been fired at them
^
|Expected Results
|----------------------:
|Enemy sprites should eventually "die" after being hit with bullet objects.

Test: XP functionality
Desc: Ensures that XP appears and interacts with the player as intended.
| Step                 |Procedure             
|----------------------|--------------------:
|  1                   | Run program          
|  2                   | Click the start button
|  3                   | Note player's current XP
|  4                   | Defeat a few enemies
|  5                   | Verify that a "blue gem" is dropped where the enemy is defeated
|  6                   | Use WASD to move player into the gem
|  7                   | Verify that player's current XP has gone up
^
|Expected Results
|----------------------:
|Player character heshould gain XP upon touching the gems dropped from enemies.

Test: Upgrade UI
Desc: Checks if the Ugrade UI appears correctly and is applied correctly.
| Step                 |Procedure             
|----------------------|--------------------:
|  1                   | Run program          
|  2                   | Click the start button
|  3                   | Note player's current statistics
|  4                   | Defeat enemies and collect XP until player's current XP is full
|  5                   | Verify an "Upgrade UI" appears with 3 options for the user
|  6                   | Select an option
|  7                   | Verify this selection has altered their respective statistics
^
|Expected Results
|----------------------:
|Player character statistics should change accordingly to the upgrade chosen.

Test: Game over
Desc: Verifies the game screen ends when the player has "lost".
| Step                 |Procedure             
|----------------------|--------------------:
|  1                   | Run program          
|  2                   | Click the start button
|  3                   | Use WASD to move player into an enemy sprite
|  4                   | Repeat step 3 until health reaches 0
|  5                   | Verify that player is sent back to start screen
^
|Expected Results
|----------------------:
|Program displays a start screen again when player has lost all health points.

Test: Game win
Desc: Ensures the player wins when the win condition is met.
| Step                 |Procedure             
|----------------------|--------------------:
|  1                   | Run program          
|  2                   | Click the start button
|  3                   | Play through the game until timer reaches 0
|  4                   | Verify that a game win screen is displayed
^
|Expected Results
|----------------------:
|Program displays a win screen when the player has stayed alive for 10 minutes.

Test: Error handling
Desc: Verifies that the program does not respond or crash to unexpected inputs.
| Step                 |Procedure             
|----------------------|--------------------:
|  1                   | Run program          
|  2                   | Click around start button
|  3                   | Verify the game screen does not show up unless start button is specifically pressed
|  4                   | Click the start button
|  5                   | Input key values other than 'W','A','S', and 'D'
\  6                   | Verify the program does not close or crash
^
|Expected Results
|----------------------:
|Program should not respond to any non-specified inputs.