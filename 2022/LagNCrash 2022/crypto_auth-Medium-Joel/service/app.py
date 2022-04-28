from flask import Flask, render_template, request, make_response
from function import encrypt, decrypt

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':

        to_encrypt_text = request.form.get('send_message')

        if to_encrypt_text is None:
            message_sent = ""
        else:
            message_sent = encrypt("Sending this piece of message:"+to_encrypt_text)

        to_decrypt_text = request.form.get('receive_message')

        if to_decrypt_text is None:
            message_received = ""
        else:
            message_received = decrypt(to_decrypt_text)

    else:
        message_sent = ""
        message_received = ""
    resp = make_response(render_template('index.html', message_sent=message_sent, message_received=message_received))
    resp.set_cookie('user', encrypt("user"))
    return resp


@app.route('/flag', methods=["GET"])
def flag():
    if 'user' in request.cookies:
        # check if its admin
        cookie = request.cookies.get("user")
        if cookie == "":
            message = "Who are you ?"
        else:
            user = decrypt(cookie).split(":")[0]
            if user == 'admin':
                message = 'LNC2022{eZ_Auth_Byp@ss}'
            else:
                message = 'Go away '+user+' You are not an admin'
    else:
        message = "Who are you ?"
    return render_template('flag.html', message=message)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
