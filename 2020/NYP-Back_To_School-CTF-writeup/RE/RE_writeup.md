## Challenges
1. APK
2. SHA256()

## APK
![](/RE/APK/challenge.png)


* [apk file](/RE/APK/Infosec.apk)

o	Step 1 : Extract files from apk

![](/RE/APK/extract.png)


**Flag**
o	Step 2: under assets > www > img, there is a banner.png which is the flag
![](/RE/APK/banner.png)



## SHA256()
![](/RE/SHA256()/challenge.png)


o	Step 1 : Go to the URL

![](/RE/SHA256()/1.png)


o	Step 2: View the page source
	In the page source there is this js function And a lot of links to images
![](/RE/SHA256()/2.png)
![](/RE/SHA256()/3.png)

o	Step 3:from the js function, if the login is successful, it will display image 161


o	Step 4: opening image 161, we get the flag

![](/RE/SHA256()/aasSGDFGHFFtdsgdfhsghdffgDFHHsdhdfsghdgggSGDSGGSgj.png)
