DRIVE SQUARE: 

The core problem here is how to get the robot to initiate the turn, and how to execute the turn. For the first problem, I used a simple while loop to initiate the robot turn. I wait 2.5 seconds while the robot drives forward, and then I stop the robots forward progress, and begin to turn. To keep the turn to 90 degrees, I recorded the turn start time, and update the current angle to be the angular speed times the total time elapsed, which equals the current angle. When the angle is greater than 90 degrees, the robot stops turning, and the cycle repeats itself. 

The script only has two functions. In __init__, I initialize the RosTopic, and in run, I execute what was outlined above. 



