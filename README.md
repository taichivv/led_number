# led_number

### 今回行ったこと
今回ROSを用いて打ち込んだ数字が偶数の場合LED点灯、奇数の場合LED消灯というのもを作成しました。  
以下がYouTubeリンクになります。  
https://youtu.be/exzufHrwbvo
  
  
$ cd ~/catkin_ws/src  
$ git clone https://github.com/taichivv/led_number.git  
$ cd ..  
$ catkin_make  
$ cd src/led_number/myled  
$ bash setup.bash  
$ roslaunch led_ros led.launch  
$ (任意の数字)
