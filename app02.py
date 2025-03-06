# 로그인 화면 보여주기
# 로그인 처리하기 : spring/1234
# 로그인 성공화면

from flask import Flask, render_template,request,redirect

app=Flask(__name__)

@app.route("/login",methods=['get'])
def login_get():
	state = request.args.get('state',None)
	message = "로그인에 실패했습니다" if state!=None else ""
	return render_template("login.html", message=message)

@app.route("/login",methods=['post'])
def login_post():
	username = request.form.get('username')
	password = request.form.get('password')
	if username =='spring'and password=='1234':
		return redirect("/success")
	else:
		return redirect("/login?state=fail")
@app.route("/success")
def success():
	return render_template("/success.html")


app.run(debug=True)