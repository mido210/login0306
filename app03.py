#하나의 작업은 같은 주소 
# /login
# -get : render_template
# -post: 처리한 다음 redirect
#  성공 - /success로 보내자
#  실패 - /login으로 보내자 
# 				-그냥 /login으로 보내면 로그인 주소를 타이핑해서 들어온 것과 로그인에 실패한 것이 구별이 안된다
#         -/login?state=fail로 이동시키자 
#         -request.args.get('state')
# /success render_template
from flask import Flask, render_template,request,redirect
app = Flask(__name__)

@app.route("/login",methods=['get'])
def login_get():
	state = request.args.get('state',None)
	message = '로그인에 실패했습니다' if state!=None else ""
	return render_template("login.html")



@app.route("/login",methods=['post'])
def login_post():
	username=request.form.get('username')
	password=request.form.get('password')
	if username =='spring'and password=='1234':
		return redirect("/success")
	else:
		return redirect("/login?stape=fail")
@app.route("/success")
def success():
	return render_template("success.html")





app.run(debug=True)