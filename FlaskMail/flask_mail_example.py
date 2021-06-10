from flask import Flask
from flask import render_template
from flask_mail import Mail
from flask_mail import Message

mail_user_name = "rakesh.sit045@gmail.com"
sender_mail = "2702rakesh@gmail.com"
sender_trishala_mail = "trishla.singh35@gmail.com"
sender_raka_mail = "raka06184@gmail.com"
mail_password = "Rakesh*****@*****"

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = mail_user_name
app.config['MAIL_PASSWORD'] = mail_password
app.config['MAIL_DEFAULT_SENDER'] = mail_user_name

mail = Mail(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/send_mail')
def send_mail():
    try:
        msg = Message(
            'Message example',
            recipients=[sender_raka_mail]
        )
        msg.body = 'message attachment test'
        msg.html = render_template('mail-template.html')
        with app.open_resource("s1.png") as fp:
            msg.attach("s1.jpg", "image/jpg", fp.read())
        mail.send(msg)
    except Exception as e:
        print(e)
    return render_template("send_mail.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run()
