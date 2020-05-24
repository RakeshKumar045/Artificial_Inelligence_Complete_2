from flask import Flask, render_template, url_for, redirect, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


@app.route('/index')
def index_home():
    return render_template('index.html')


@app.route('/predict', methods=['GET'])
def predict():
    print("hi 3")

    predicted_age_of_marriage = [[int(request.args['gender']),
                                  int(request.args['religion']),
                                  int(request.args['caste']),
                                  int(request.args['mother_tongue']),
                                  int(request.args['country']),
                                  int(request.args['height_cms']),
                                  ]]

    print(predicted_age_of_marriage)
    # return str(round(predicted_age_of_marriage[0], 2))
    return "Hello, Rakesh"


@app.route("/tensorbroad_pb_android", methods=['GET', 'POST'])
def salvador():
    return "Hello, Rakesh"


# Defaul method is GET
@app.route('/test1/<userName>')
def homepage(userName):
    print("Browser Data : ", userName)
    return render_template("/TestMain.html", name=userName)


@app.route("/test2/<name>")
def test_first(name):
    return "my name is " + name


@app.route("/test3/<int:value>")
def m1(value):
    return "result is %d" % value


# It's not working , check it later.
@app.route("/test4/<float:value>")
def m2(value):
    return " result for float : %f" + value


@app.route("/test5/")
def m3():
    return "working /test5/"


# difference b/w m3 and m4 are "/test5/ : work for both(/test5 or /test5/)" , "/test6 : work only("/test6)"

@app.route("/test6")
def m4():
    return "working /test6"


@app.route("/admin")
def hello_admin():
    return "Hello Admin Rakesh"


# hint http://127.0.0.1:2000/guest raka (output : Hello Guest is : raka)
@app.route("/guest <guestInput>")
def guest_admin(guestInput):
    return "Hello Guest is  : " + guestInput


@app.route("/user/<name>")
def dynamicValue(name):
    if name == "admin":
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("guest_admin", guestInput=name))


@app.route("/test7", methods=["POST"])
def dictionApiTesting():
    dic_val = {"Rakesh": "Kumar", "Age": 27, "Lcation": "Kochas"}
    return render_template("/TestMain.html", result=dic_val)


@app.route("/test8", methods=["GET", "POST"])
def returnJsonVlaue():
    dic_val = {"Rakesh": "Kumar", "Age": 27, "Lcation": "Kochas"}
    return jsonify(dic_val)


if __name__ == "__main__":
    app.run(port=2000, debug=True)
