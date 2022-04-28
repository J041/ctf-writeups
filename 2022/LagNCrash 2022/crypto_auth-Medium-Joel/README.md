# Crypto Auth

*Creator - Joel*

## Description

Break in and get the flag

## Distribution
- function.py
    - SHA1: 0784B1BCB30B9B387E591DA3371C6894E1BF4CA3

## Setup Guide (Optional)
1. sudo docker build -t crypto-auth:latest .
2. sudo docker run -d -p 80:5000 crypto-auth


## Solution
Solution to this challenge
1. Enter `xxadmin` in the box beside send message and click on send message
2. base64 decode the value and remove the first 32 bytes 
3. base64 encode the new value and set it as the `user` cookie value
4. Go to `/flag`
5. yay the flag!

## Flag
`LNC2022{eZ_Auth_Byp@ss}`

