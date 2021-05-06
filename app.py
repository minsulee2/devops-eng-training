from flask import Flask, render_template, request
from functions import add_function, subtract_function, multiply_function, division_function
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/healthz", methods=["GET"])
def healthCheck():
    return "", 200


# TODO(everyone): GET 메소드로 더하기, 빼기, 곱하기, 나누기 함수 라우트 완성하기
@app.route("/add", methods=["GET"])
def add():
    num1 = request.args.get("num1")
    num2 = request.args.get("num2")
    result = add_function(num1, num2)
    return num1 + "+" + num2 + "=" + result


@app.route("/subtract", methods=["GET"])
def subtract():
    num1 = request.args.get("num1")
    num2 = request.args.get("num2")
    result = subtract_function(num1, num2)
    return num1 + "-" + num2 + "=" + result


@app.route("/multiply", methods=["GET"])
def multiply():
    num1 = request.args.get("num1")
    num2 = request.args.get("num2")
    result = multiply_function(num1, num2)
    return num1 + "*" + num2 + "=" + result


@app.route("/division", methods=["GET"])
def division():
    num1 = request.args.get("num1")
    num2 = request.args.get("num2")
    result = division_function(num1, num2)
    return num1 + "/" + num2 + "=" + result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
