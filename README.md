DRIVE SQUARE: 

The core problem here is how to get the robot to initiate the turn, and how to execute the turn. For the first problem, I used a simple while loop to initiate the robot turn. I wait 2.5 seconds while the robot drives forward, and then I stop the robots forward progress, and begin to turn. To keep the turn to 90 degrees, I recorded the turn start time, and update the current angle to be the angular speed times the total time elapsed, which equals the current angle. When the angle is greater than 90 degrees, the robot stops turning, and the cycle repeats itself. 

The script only has two functions. In __init__, I initialize the RosTopic, and in run, I execute what was outlined above. 

CHALLENGES: 

To be honest, I struggled a lot with getting Gazebo to work and the NoMachine, which has been really buggy for me, to work. I struggled for a little bit with adjusting the speed of the robot and playing with the angular speed so that it would actually get close to making the angular turns and not run past them and turn to far. 

I also am still sort of figuring out object-oriented programming, so writing code like that is still a bit of an adjustment for me. 

FUTURE WORK: 

I would change from using time to control the amount of time it goes forward to a different mechanism. The time thing seems to arbitrary, and I would have liked to explore other ways of implementing this, perhaps like tracking the distance it travelled. Theoretically I could have done that by just multiplying the time and forward speed. 

I would also like to find a way to control for the noise better. I don't like that it makes impeerfect squares, and sort of slowly strays farther and farther from the initial position. Some sort of error correcting mechanism could be interesting to explore here. 

TAKEAWAYS:
* Identify whether you are publishing or subscribing, and what rostopic you will need to use as your first steps. Once you have figured this out, you can proceed to implement the specific task
* Think of the steps to complete as 1)Initialize RosTopic and 2) Run the specific task at hand. 

![drivesquare](https://github.com/jonahkaye/warmup_project/blob/main/scripts/drivesquare.gif)


PERSON FOLLOWER: 

The core problem here is how to recognize which direction to turn the robot towards so that it is facing the person/object. This difficulty is exentuated by the fact that as the robot moves forward, noise means that person will not continue to be in front of the robot after a turn has been made. To resolve this, the robot scans using LIDAR to find the direction (measured in degrees) closest to person, and then turns that way. When turning, it will either turn left or right, depending on which way reaches the desired degree first. The turning is PID, so it will turn faster as the degrees it needs to travel to is larger and slower as it gets closer to the degree it needs to get to. If it is the case that the person is actually right in front of the robot (with room for noise so 359 - 1 degrees), then the robot does not turn. 

To make the movement smooth, the robot turns and moves linearly simaltaneously. If the object is within 0.5 meters and 3.5 meters (the LIDAR boundary), then the robot moves linearly, and if it is at less that 0.5 meters, it does not move linearly. 

The script has 3 functions. init, where we create a Subscriber and a Publisher, distance, where we calculate the angle and distance of the person and set the angular and linear velocity, and run, where the rospy is activated. 

ChALLENGES: 

I struggled with the object oriented aspect of this a lot at first. I didn't realize that the distance callback function that the scan rostopic uses requires that you pass self to it, so that took me a while to figure out. Also, the idea to separate the linear and angular speed calculations to generate smooth driving was a big help that eliminated alot of the challenges I was having with jittery driving. The other big problem was realizing that the robot should turn left or right depending on which one was closer to the desired angle. Before I realized that (all of these thing Pouya helped me on a lot), the turning was also very slow. 

FUTURE WORK: 

My implementation ends a little oddly. I think because of noise, the robot stops in front of the person and then just sort of jitters back and forth changing the angle. If I had more time, I would have fized that so that it came to a complete stop when right in front of the object, perhaps by creating a global boolean variable to indicate if the robot is in following mode or waiting for the object to be moved mode. 

TAKEAWAYS: 

*The biggest takeaways were definetly about separating linear and angular velocity setting so that the robots movement could be smooth, learning how to use the scan rostopic, and learning how to do object oriented programming better. 
*I also got to use PID, which was good practice implementing what we recently did in class. 

![drivesquare](https://github.com/jonahkaye/warmup_project/blob/main/scripts/person_follower2.gif)

WALL FOLLOWER: 

The core problem here is how to switch between the two main modes of the robot: driving straight alongside the wall and turning at the corners. To acheive this, we use a global boolean variable, set to 0 if the robot has walls on two sides and needs to turn, and set to 1 otherwise. When the value is 1, the robot drives forward using a PID operation, which has a smaller angular velocity as the robot is closer to the 0.5 meter away from the wall line, and has a constant linear velocity. When it is 0, the robot turns with no linear velocity. 

This setup also works at the onset when the robot is in the center of the room and needs to approach a wall. Since it is not in range of any two walls, the global boolean is set to one and it drives forward until it gets to be directly infront of wall, and which point the global bolean becomes 0 and it turns, and then begins following the wall. 

The script has 3 functions. init, where we create a Subscriber and a Publisher, distance, where we set the global boolean and set the angular and linear velocity, and run, where the rospy is activated. 

CHALLENGES: 

The core challenge here was playing with the coefficient so that my robot was close enough to follow the wall but not to close that it didnt have room to turn. I also had to experiment a bit with different values for the PID equation for the robots angular velocity. 

FUTURE WORK: 

I would optimize the intitial process to find the first wall. My code works because the robot will just drive forward with an angular velocity when it is stuck in the middle of the room, and then enter the wall following phase. There is a weird bug where the robot does a double turn, and with more time I would try to fix it. I might try creating a third value for the global variable for a new wall finding phase. 

TAKEAWAY

* Using a global variable to switch between different phases of the robots movement. This is essentially like breaking the problem in two, and solving them seperately, which I thought was a good methodology.
* Again, separating the angular and linear processes was a good methodology that allowed the robot to travel more smoothely as it can simaltaneously use PID to alter the angular while mooving forward. 

![drivesquare](https://github.com/jonahkaye/warmup_project/blob/main/scripts/wall_follower.gif)