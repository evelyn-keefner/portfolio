*CS110 Midterm Exam

##Short Description
A program that utilizes the turtle module in order to randomly generate a tree like structure using a variety of user parameters

##Known Bugs and Incomplete Parts
1.
User input is prone to error, as in order to not have to spend time writing specific while loops for every new input, there is one input function that handles all user input, and only has one check, this check being whether or not the user inputted a float value. However, if the user inputs a negative value, this will cause an error to be pushed after all inputs are gathered. On top of this, certain parameters such as the 'size_decay' parameter can ONLY take a positive value above 1. This is because the 'size_decay' parameter determines the end condition of the recursive function, if the value is below one, the branches will GROW in size rather than decay and the end condition will not be met. If the value is exactly one, the branches will not change in size, also causing the end condition to not be met. This a solvable issue, but for now the user is simply provided with instructions on what values to input with no boundary checking for these certain cases.

2. 
Performance within this program is not ideal. The time complexity of the recursive function is absurd in worst case scenarios. The compute time is largely dependant on the "branch_frequency" parameter. For example, with the recommended value of 3, in a worst case scenario which has a 0.00169350878% chance of occurring, the draw_branches() function will call itself 12 times. In the average case, the function will call itself an average of 2.3 times. The function will go 4 layers deep when using the recommended values for every other parameter, the parameters that influence this value are size and size_decay. 

3. 
If the tree gets drawn outside the bounds of the window, the window does not expand to contain the tree

##References 
Prior knowledge of recursion from experience with Java

##Miscellaneous Comments 
None

