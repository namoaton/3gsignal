# 3gsignal python script for OpenWRT
![Screenshot](https://github.com/namoaton/3gsignal/blob/master/3signal.png)

- [x] To start this programm check the fist lines of the programm and update the ip address and login-password of your router. Then just type in command line
```
python get_signal3g.py 
```

Please note, some users may expirience problems (inappropriate signal strength that is not changing) - this is due to the different outputs in the "comgt" function. Please adjust the line 20 playing with the numbers in brackets [15:17], [16:19] and so on.
