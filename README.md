# FunctionWithColor
<hr />
US: <br />
!Currently, blue color is defined in the codes in the project, it can be added in other colors with the same codes <br />
!functions are arranged according to the desired situation <br />
One of the aims of the project is to determine the color ranges detected from the cameras placed under the (UAV) and apply the necessary actions. <br />

Some of the aims of this project: <br />
1-Effectiveness can be achieved thanks to the cameras placed under the UAV vehicles. It can react autonomously to negative situations such as fire with the color ranges detected from the cameras. <br />
Example: If the thermal values of the fire exceed a certain size as soon as it is transmitted using a thermal camera, water evacuation and law enforcement can be notified. <br />
 <br />
2- Autonomous material extraction from drones, cameras placed under UAV vehicles, on a flat area according to the differences in needs.<br />
example scenario: snowy places on the mountain that are not immediately accessible, etc. In case of need, colored objects with a certain area given to the mountaineers can be set up on the flat area and the UAV detects this color and the given area, and according to the color difference, the desired water, food and other determined materials can be left from above in an autonomous way. <br />

example scenario: snowy places on the mountain that are not immediately accessible, etc. In case of need, colored objects with a certain area given to the mountaineers can be set up on the flat area and the UAV detects this color and the given area, and according to the color difference, the desired water, food and other determined materials can be left from above in an autonomous way. <br />

This project has been implemented with the OpenCV library <br />
########################################## <br />
working logic of the software:<br />
1-cameras are activated<br />
2-uses specific hsv value ranges for colors <br />
3-the square appears on the camera<br />
4-If the specified color field value is greater than the desired area, the color is framed. <br />
5-loop is entered if the area is inside the frame on the camera <br />
6-Writes the coordinate values from the camera to the console <br />
7-It detects which color is in the frame and determines the range of color values and runs the function of that color. <br />
8-software stops with "q" key <br />
########################################## <br />
<br />
<br />
<hr />
<hr />
TR: <br />
!Şuan projede kodlarında mavi renk tanımlıdır diğer renklerde aynı kodlarla eklenebilir <br />
!istenilen duruma göre fonksiyonlar düzenlenir <br />
<br />
Bu projenin amaçlarından bazıları: <br />
1-İHA araçlarının altına yerleştirilen kameralarda aktiflik sağlayabilmesidir.Kameralardan tespit edilen renk aralıklarıyla yangın gibi olumsuz durumlara otonom bir şekilde müdahale gerçekleştirebilir <br />
örnek:termal kamera kullanılarak yapılan intikal anında yangının verilen termal değerleri belirli büyüklüğü geçerse su bırakma ve kolluk kuvvetlerine haber iletimi yapılabilir. <br />
 <br />
2-İHA araçlarının altına yerleştirilen kameralardan düzlük alandaki ihtiyaç farklılıklarına göre malzemelerin ihadan otonom birşekilde atılması.<br />

örnek senaryo: laşılması anlık mümkün olmayan dağda karlık yerler vb. dağcılara verilen belirli alana sahip renkli nesneleri ihtiyaç durumunda düzlük alana kurup ihanın bu renk ve verilen alanı tespit etmesiyle renk farklılığına göre istenilen su,yemek ve diğer belirlenen malzemeleri otonom bir şekilde yukardan bırakılabilir. <br />
<br />
Projede OpenCV kütüphanesinden yaralanılmıştır <br />
<br />
########################################## <br />
Yazılımın çalışma sırası: <br />
1-İstenilen kameralar etkinleştirildi <br />
2-Renkler için spesifik hsv aralıkları kullanılır <br/>
3-değerlerin ekranın neresinde olmasını istediğimiz kare ekranda belirir <br/>
4-Renkler istenilen alanı geçmiş ise çerçeve içerisine alınıp belirlenir <br />
5-Eğer belirlenen alan ekranda belirlenen karenin içindeyse döngüye girilir <br />
6-kameradan aldığı ekrandakı 2lik düzlemdeki  kordinatini yazar <br />
7-Ekrandaki karenin içindeki renk aralığını deneyerek hangi renk olduğunu bulur ve o rengin fonksiyonunu çalıştırır(fonksiyonlar ihtiyaca göre düzenlenir) <br />
8-yazılım q tuşuna tıklayak durur <br />
<hr />







this software is written by batuhan

in any questions and other things mail: batuddxd@gmail.com

<a href="https://ibb.co/GxQGnfs"><img src="https://i.ibb.co/yfFKdmh/exp.png" alt="exp" border="0"></a>
