# FunctionWithColor

One of the aims of the project is to determine the color ranges detected from the cameras placed under the (UAV) and apply the necessary actions.

exp:For example, the color ranges of the fire can be determined in an infrared camera or a normal camera, and when the color ranges come to a certain angle of the camera, it can provide the necessary operations autonomously.

--This project has been implemented with the cv2 library
---------------------------------------------------------------------------------------------------------------------------------
working logic of the software:
1-cameras are activated
2-uses specific hsv value ranges for colors 
3-the square appears on the camera
4-If the specified color field value inside the square is greater than the desired color, the color is framed.
5-Writes the coordinate values from the camera to the console
6-loop is entered if the area is inside the frame on the camera
7-It detects which color is in the frame and determines the range of color values and runs the function of that color.
8-software stops with "q" key
-----------------------------------------------------------------------------------------------------------------------------------

this software is written by batuhan

in any questions and other things mail: batuddxd@gmail.com




