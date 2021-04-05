DRIVE SQUARE: 

The core problem here is how to get the robot to initiate the turn, and how to execute the turn. For the first problem, I used a simple while loop to initiate the robot turn. I wait 2.5 seconds while the robot drives forward, and then I stop the robots forward progress, and begin to turn. To keep the turn to 90 degrees, I recorded the turn start time, and update the current angle to be the angular speed times the total time elapsed, which equals the current angle. When the angle is greater than 90 degrees, the robot stops turning, and the cycle repeats itself. 

The script only has two functions. In __init__, I initialize the RosTopic, and in run, I execute what was outlined above. 

CHALLENGES: 

To be honest, I struggled a lot with getting Gazebo to work and the NoMachine, which has been really buggy for me, to work. I struggled for a little bit with adjusting the speed of the robot and playing with the angular speed so that it would actually get close to making the angular turns and not run past them and turn to far. 

I also am still sorf of figuring out object-oriented programming, so writing code like that is still a bit of an adjustment for me. 

FUTURE WORK: 

I would change from using time to control the amount of time it goes forward to a different mechanism. The time thing seems to arbitrary, and I would have liked to explore other ways of implementing this, perhaps like tracking the distance it travelled. Theoretically I could have done that by just multiplying the time and forward speed. 

I would also like to find a way to control for the noise better. I don't like that it makes impeerfect squares, and sort of slowly strays farther and farther from the initial position. Some sort of error correcting mechanism could be interesting to explore here. 

TAKEAWAYS:
* Identify whether you uare publishing or subscribing, and what rostopic you will need to use as your first steps. Once you have figured this out, you can proceed to implement the specific task
* Think of the steps to complete as 1)Initialize RosTopic and 2) Run the specific task at hand. 

![drivesquare](https://github.com/jonahkaye/warmup_project/blob/main/scripts/drivesquare.gif)