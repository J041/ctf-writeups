## Challenges
1. Hidden Image
2. Blank Excel
3. The hardest challenge
4. Mysterious Picture
5. There are plenty of flags
6. The answer
7. Snake
8. Deconstruct-Reconstruct
9. Don’t Scan Me
10. Musically Inclined
11. Stegosaurus
12. get pawn-ed
13. What’s my Password

## Hidden Image
![](./Hidden%20Image/challenge.png)

[Hidden.jpg](./Hidden%20Image/Hidden.jpg)


o	Step 1 : Change file type of hidden.png to txt and do a quick search command 

![](./Hidden%20Image/1.png)

```
flag: NYP{RED_PANDA}
```


## Blank Excel
![](./Blank%20Excel/challenge.png)

[challenge.xlsx](./Blank%20Excel/challenge.xlsx)


o	Step 1 : Find the hidden sheet in challenge.xlsx which contain the flag by using the “unhide” option

![](./Blank%20Excel/1.png)
![](./Blank%20Excel/2.png)

```
flag: NYP{HIDDEN_CELL}
```


## The hardest challenge
![](./The%20hardest%20challenge/challenge.png)

o	Step 1 : Complete survey provided by NYP Infosec


## Mysterious Picture
![](./Mysterious%20Picture/challenge.png)

[challenge](./Mysterious%20Picture/backtoschool.jpg)

o	Step 1 : Change file type of backtoschool.png to txt and do a quick search command 

![](./Mysterious%20Picture/1.png)

```
flag: NYP{yay_back_t0_sch00l}
```


## There are plenty of flags
![](./There%20are%20plenty%20of%20flags/challenge.png)

![](./There%20are%20plenty%20of%20flags/Flag.jpg)

o	Step 1 : Flag Semaphore


## The answer
![](./The%20answer/challenge.png)

[The answer.zip](./The%20answer/The%20Answer.zip)

o	Step 1 : Extract The Answer.zip and run this command on linux to get the flag
```
grep -rnw '/path_of_zip/' -e 'NYP{'
```

## Snake
![](./Snake/challenge.png)

[Snake.exe](./Snake/Snake.exe)

o	Step 1 : Change the filetype of Snake.exe to text file 

![](./Snake/1.png)

o	Step 2 : Convert the binary to ASCII/UTF-8 character on a online converter and you will see a base64 encoded string on the header

![](./Snake/2.png)

o	Step 3 : Decode the base64 character for the flag
```
flag: NYP{PYTHONISATYPEOFSNAKE}
```


## Deconstruct-Reconstruct
```
unsolved
```
![](./Deconstruct-Reconstruct/challenge.png)

[Reco](./Deconstruct-Reconstruct/Reco)
[nstru](./Deconstruct-Reconstruct/nstru)
[ction](./Deconstruct-Reconstruct/ction)


## Dont Scan Me
![](./Don't%20Scan%20Me/challenge.png)

![](./Don't%20Scan%20Me/Dont%20Scan%20Me.png)

o	Step 1 : Check the metadata of Don’t Scan Me.png on [www.metadata2go.com](www.metadata2go.com)

![](./Don't%20Scan%20Me/1.png)

```
flag: NYP{EXIF_DATA}
```


## Musically Inclined
![](./Musically%20Inclined/challenge.png)

![](./Musically%20Inclined/BTS_MusicallyInclined.png)

o	Step 1 : Decode it on [https://www.dcode.fr/music-sheet-cipher](https://www.dcode.fr/music-sheet-cipher) with the character on  BTS_MusicallyInclined.png
![](./Musically%20Inclined/music.png)

```
flag: NYP{YOUAREMUSICALLYTALENTED}
```


## Stegosaurus
![](./Stegosaurus/challenge.png)

![](./Stegosaurus/Stego.png)

![](./Stegosaurus/hint.png)

o	Step 1 : Go to [https://futureboy.us/stegano/decinput.html](https://futureboy.us/stegano/decinput.html)

o	Step 2 : Find the password by taking the first character of each word from the Hint

o	Step 3 : Select Stego.jpg and enter Password as Ze3cAC
 
![](./Stegosaurus/1.png)

o	Step 4 : Convert the binaries to ASCII/UTF-8 for the flag 
```
flag: NYP{ST3GAN0GRAPHY}
```

## get pawn-ed
```
unsolved
```
![](./get%20pawn-ed/challenge.png)
![](./get%20pawn-ed/qn.png)


## What's my Password?
![](./What's%20my%20Password/challenge.png)

[secret.zip](./What's%20my%20Password/secret.zip)

o	Step 1 : Brute force the zip file by using rockyou.txt and frcrackzip to find the password
```
fcrackzip -v -u -D -p rockyou.txt secret.zip
```
