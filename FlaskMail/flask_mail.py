# __author__ = 'Rakesh Kumar Gupta'

from flask import Flask
from flask_mail import Mail, Message

# Initialize the app.
app = Flask(__name__)
app.config.update(
    DEBUG=True,
    # EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME='kumarrakesh@gmail.com',
    MAIL_PASSWORD='123456789',
    MAIL_DEBUG=True
)
mail = Mail(app)


# On accessing 127.0.0.1:<port>/ a mail will be sent to the recipients mail id.
@app.route("/")
def send():
    msg = Message("Hi! Welcome to Flask Mail!", sender='kumarrakesh@gmail.com', recipients=['raka06199@gmail.com'])
    msg.body = "This is the email body"
    mail.send(msg)
    print("Mail sent")
    return "Please check you email,Sent"


@app.route("/image")
def send_image_body():
    msg = Message("Hi! Welcome to Flask Mail!", sender='kumarrakesh@gmail.com', recipients=['raka06199@gmail.com'])
    msg.body = "This is the email body"

    msg.html = """   

    <!DOCTYPE html>
    <html>
    <head>
        <title>Email Template</title>
        <link href="https://fonts.googleapis.com/css?family=Niramit" rel="stylesheet">
        <style>
            .paragraph{
        font-family: 'Niramit', sans-serif;
        font-style: 50px

    }
    .button {
        background-color: #4CAF50; /* Green */
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
    }

    .button3 {background-color: #f44336;} /* Red */ 

        </style>

    </head>
    <body style="margin: 0; ">

        <table align="center" border="0" cellpadding="20" cellspacing="0" >
            <tr><td>
        <table align="center" border="0" cellspacing="0" width="300">
            <tr>
                <td align="center">
                    <h1 class="paragraph" style="font-size: 50px">Universe</h1>    
                    <img src="https://pbs.twimg.com/media/C_kwC7GWAAE-uyY.jpg" alt= "Creating Email Magic" width="900" height="300">
                </td>
            </tr>
            <tr>
                <td bgcolor="#ffffff" style="padding-top: 20px">
                    <table border="0" cellpadding="0" cellspacing="0" width="100%">
                <tr>
                    <td align="center">
                        <h1 class="paragraph">Mankind was born on Earth. It was never meant to die here.</h1>
                    </td>
                </tr>
                <tr>
                    <td align="center">
                    <p class="paragraph">“We used to look up at the sky and wonder at our place in the stars, now we just look down and worry about our place in the dirt.”  <b>- Cooper</b> </p>
                    </td>
                </tr>

             <tr>
                <td align="center">
                    <img src="https://vignette.wikia.nocookie.net/interstellarfilm/images/3/30/Imax-poster-for-interstellar.jpeg/revision/latest?cb=20141003183300" alt= "Creating Email Magic" width="250" height="370">

            </td>
        </tr>

        <tr>
            <td align="center" style="padding-top: 50px">

            <font style="font-family: 'Niramit', sans-serif;font-style: 50px">
            In the future, Earth is slowly becoming uninhabitable. Ex-NASA pilot Cooper, along with a team of researchers, is sent on a planet exploration mission to report which planet can sustain life.
            </font>
            </td>
        </tr>

        <tr>
        <td align="center">
            <img src="https://coverfiles.alphacoders.com/449/44921.jpg" alt= "Creating Email Magic" width="900" height="300">

        </td>
        </tr>
        </td>
    </tr>
    </table>
    </table>

    <div align="center" style="padding-top: 20px">
    <a href="https://in.bookmyshow.com/vadodara">
        <button class="button button3" value="Book Tickets!" onclick="window.open('https://in.bookmyshow.com/vadodara')">Book Tickets!</button>
    </a> 
    </div>

    </body>
    </html>

    """

    mail.send(msg)
    print("Mail sent")
    return "Sent"


if __name__ == "__main__":
    app.run()
