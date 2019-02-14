"导入模块"
from flask import Flask,render_template
"创建一个应用"
app =Flask(__name__)
"注册路由（URL）"
@app.route("/")
def index():
    return "首页"
@app.route("/wzk")
def wzkinfo():
    return "王增科的个人主页"
@app.route("/zyp")
def zypinfo():
    return "张宇鹏的个人主页"
@app.route("/wzk/pay")
def wzkpay():
    # return "<h1>王增科的个人网站充值页面</h1>"
    return render_template('pay.html',name="zzy")
"启动服务"
app.run()
