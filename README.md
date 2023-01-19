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
4-If the specified color field value is greater than the desired area, the color is framed. <br />
5-loop is entered if the area is inside the frame on the camera <br />
6-Writes the coordinate values from the camera to the console <br />
7-It detects which color is in the frame and determines the range of color values and runs the function of that color. <br />
8-software stops with "q" key <br />
########################################## <br />


<hr />
<hr />
TR:
!Şuan projede kodlarında mavi renk tanımlıdır diğer renklerde aynı kodlarla eklenebilir

Bu projenin amaçlarından bazıları:
1-İHA araçlarının altına yerleştirilen kameralarda aktiflik sağlayabilmesidir.Kameralardan tespit edilen renk aralıklarıyla yangın gibi olumsuz durumlara otonom bir şekilde müdahale gerçekleştirebilir
örnek:termal kamera kullanılarak yapılan intikal anında yangının verilen termal değerleri belirli büyüklüğü geçerse su bırakma ve kolluk kuvvetlerine haber iletimi yapılabilir.

2-İHA araçlarının altına yerleştirilen kameralardan düzlük alandaki ihtiyaç farklılıklarına göre malzemelerin ihadan otonom birşekilde atılması.
örnek senaryo: laşılması anlık mümkün olmayan dağda karlık yerler vb. dağcılara verilen belirli alana sahip renkli nesneleri ihtiyaç durumunda düzlük alana kurup ihanın bu renk ve verilen alanı tespit etmesiyle renk farklılığına göre istenilen su,yemek ve diğer belirlenen malzemeleri otonom bir şekilde yukardan bırakılabilir.

Projede OpenCV kütüphanesinden yaralanılmıştır

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
