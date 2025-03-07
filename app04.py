# 1.로그인 2. 숫자 2개 입력 3덧셈 4 결과
from flask import Flask, request,redirect, render_template
app = Flask(__name__)
# hap=0
@app.route("/login", methods=['get'])
def longin_get():
	state= request.args.get("state",None)
	message="로그인에 실패했습니다" if state!=None else ""
	return render_template("login2.html",message=message)

@app.route("/login", methods=['post'])
def login_post():
	username=request.form.get('username')
	password=request.form.get('password')
	if username=='spring'and password=='1234':
		return redirect("/success")
	else:
		return redirect("/login?state=fail")

@app.route("/success", methods=['get'])
def success_get():
	return render_template("success2.html")


@app.route("/success", methods=['post'])
def success_post():
	# global hap
	value = int(request.form.get('value'))
	value2 =int(request.form.get('value2'))
	hap =  value+ value2
	# 새로운 작업으로 보낸다
	return redirect(f"/result?hap={hap}")

@app.route('/result')
def result():
	hap = request.args.get('hap')
	return render_template("result2.html",hap=hap)

app.run(debug=True)