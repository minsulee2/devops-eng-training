from flask import Flask, render_template, request
from functions import add, subtract, multiply, divide

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/healthz", methods=["GET"])
def healthCheck():
    return "", 200


# TODO(everyone): GET 메소드로 더하기, 빼기, 곱하기, 나누기 함수 라우트 완성하기
@app.route("/add")
def operate_add():
    num1, num2 = request.args.get('num1'), request.args.get('num2')
    return add(num1, num2)


@app.route("/subtract")
def operate_subtract():
    num1, num2 = request.args.get('num1'), request.args.get('num2')
    return subtract(num1, num2)


@app.route("/multiply")
def operate_multiply():
    num1, num2 = request.args.get('num1'), request.args.get('num2')
    return multiply(num1, num2)


@app.route("/divide")
def operate_divide():
    num1, num2 = request.args.get('num1'), request.args.get('num2')
    return divide(num1, num2)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3000', debug=True)
