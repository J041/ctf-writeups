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
![](/misc/Hidden%20Image/challenge.png)

[Hidden.jpg](/misc/Hidden%20Image/Hidden.jpg)


o	Step 1 : Change file type of hidden.png to txt and do a quick search command 

![](/misc/Hidden%20Image/1.png)

```
flag: NYP{RED_PANDA}
```


## Blank Excel
![](/misc/Blank%20Excel/challenge.png)

[challenge.xlsx](/misc/Blank%20Excel/challenge.xlsx)


o	Step 1 : Find the hidden sheet in challenge.xlsx which contain the flag by using the “unhide” option

![](/misc/Blank%20Excel/1.png)
![](/misc/Blank%20Excel/2.png)

```
flag: NYP{HIDDEN_CELL}
```


## The hardest challenge
![](/misc/The%20hardest%20challenge/challenge.png)

o	Step 1 : Complete survey provided by NYP Infosec


## Mysterious Picture
![](/misc/Mysterious%20Picture/challenge.png)

[challenge](/misc/Mysterious%20Picture/backtoschool.jpg)

o	Step 1 : Change file type of backtoschool.png to txt and do a quick search command 

![](/misc/Mysterious%20Picture/1.png)

```
flag: NYP{yay_back_t0_sch00l}
```


## There are plenty of flags
![](/misc/There%20are%20plenty%20of%20flags/challenge.png)

![](/misc/There%20are%20plenty%20of%20flags/Flag.jpg)

o	Step 1 : Flag Semaphore


## The answer
![](/misc/The%20answer/challenge.png)

[The answer.zip](/misc/The%20answer/The%20Answer.zip)

o	Step 1 : Extract The Answer.zip and run this command on linux to get the flag
```
grep -rnw '/path_of_zip/' -e 'NYP{'
```

## Snake
![](/misc/Snake/challenge.png)

[Snake.exe](/misc/Snake/Snake.exe)

o	Step 1 : Change the filetype of Snake.exe to text file 

![](/misc/Snake/1.png)

o	Step 2 : Convert the binary to ASCII/UTF-8 character on a online converter and you will see a base64 encoded string on the header

![](/misc/Snake/2.png)

o	Step 3 : Decode the base64 character for the flag
```
flag: NYP{PYTHONISATYPEOFSNAKE}
```


## Deconstruct-Reconstruct
```
unsolved
```
![](/misc/Deconstruct-Reconstruct/challenge.png)

[Reco](/misc/Deconstruct-Reconstruct/Reco)
[nstru](/misc/Deconstruct-Reconstruct/nstru)
[ction](/misc/Deconstruct-Reconstruct/ction)


## Dont Scan Me
![](/misc/Don't%20Scan%20Me/challenge.png)

![](/misc/Don't%20Scan%20Me/Dont%20Scan%20Me.png)

o	Step 1 : Check the metadata of Don’t Scan Me.png on [www.metadata2go.com](www.metadata2go.com)

![](/misc/Don't%20Scan%20Me/1.png)

```
flag: NYP{EXIF_DATA}
```


## Musically Inclined
![](/misc/Musically%20Inclined/challenge.png)

![](/misc/Musically%20Inclined/BTS_MusicallyInclined.png)

o	Step 1 : Decode it on [https://www.dcode.fr/music-sheet-cipher](https://www.dcode.fr/music-sheet-cipher) with the character on  BTS_MusicallyInclined.png
![](/misc/Musically%20Inclined/music.png)

```
flag: NYP{YOUAREMUSICALLYTALENTED}
```


## Stegosaurus
![](/misc/Stegosaurus/challenge.png)

![](/misc/Stegosaurus/Stego.png)

![](/misc/Stegosaurus/hint.png)

o	Step 1 : Go to [https://futureboy.us/stegano/decinput.html](https://futureboy.us/stegano/decinput.html)

o	Step 2 : Find the password by taking the first character of each word from the Hint

o	Step 3 : Select Stego.jpg and enter Password as Ze3cAC
 
![](/misc/Stegosaurus/1.png)

o	Step 4 : Convert the binaries to ASCII/UTF-8 for the flag 
```
flag: NYP{ST3GAN0GRAPHY}
```

## get pawn-ed
```
unsolved
```
![](/misc/get%20pawn-ed/challenge.png)
![](/misc/get%20pawn-ed/qn.png)


## What's my Password?
![](/misc/What's%20my%20Password/challenge.png)

[secret.zip](/misc/What's%20my%20Password/secret.zip)

o	Step 1 : Brute force the zip file by using rockyou.txt and frcrackzip to find the password
```
fcrackzip -v -u -D -p rockyou.txt secret.zip
```
