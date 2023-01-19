# FunctionWithColor
<hr />
US:
One of the aims of the project is to determine the color ranges detected from the cameras placed under the (UAV) and apply the necessary actions.

exp:For example, the color ranges of the fire can be determined in an infrared camera or a normal camera, and when the color ranges come to a certain angle of the camera, it can provide the necessary operations autonomously.

This project has been implemented with the OpenCV library <br />
########################################## <br />
working logic of the software:<br />
1-cameras are activated<br />
2-uses specific hsv value ranges for colors <br />
3-the square appears on the camera<br />
4-If the specified color field value inside the square is greater than the desired color, the color is framed. <br />
5-loop is entered if the area is inside the frame on the camera <br />
6-Writes the coordinate values from the camera to the console <br />
7-It detects which color is in the frame and determines the range of color values and runs the function of that color. <br />
8-software stops with "q" key <br />
########################################## <br />

this software is written by batuhan

in any questions and other things mail: batuddxd@gmail.com
<hr />

<a href="https://ibb.co/GxQGnfs"><img src="https://i.ibb.co/yfFKdmh/exp.png" alt="exp" border="0"></a>
