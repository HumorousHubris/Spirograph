# Spirograph
Program that draws a Spirograph using python turtle graphics.

This program prompts the user for the number of "arms" and then the lengths and angular velocities of each arm.
The spirograph is drawn by laying each arm end to end, like in vector addition, and a point is placed at the end of the last one.

The current implementation of this is very slow. I suspect this is because the turtle graphics themselves are slow. Eventually I will modify this program to run faster. 

One advantage of the current version of the program is that it runs on the default version of Python 3 without having to install anything else. 

For the best looking results, it is recommended to set the angular velocities to small (less than 1) values. These angular velocities have no units at the moment, as the system just adds them as fast as possible on each iteration of the main loop. 
