from flask import Flask,render_template
app =Flask(__name__)
@app.route("/")
def index():
    return "首页"
@app.route("/wzk")
def wzkinfo():
    return "王增科的个人主页"
@app.route("/wzk/pay")
def wzkpay():
    return render_template('pay.html',name="zzy")
app.run()