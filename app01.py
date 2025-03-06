from flask import Flask, render_template, request,redirect
# 객체 : 데이터 + 함수
# 클래스 : 객체를 만드는 설계도. 대문자로 시작/ 파이썬 클래스들을 소문자 
# 클래스를 가지고 객체를 만드는 함수가 클래스 이름과 같다 : 생성자(constructor)
app=Flask(__name__)

nums=[]
hap=0
@app.route("/nums", methods=['get'])
def input():
	return render_template("input.html")

@app.route("/nums", methods=['post'])
def process():
	global hap
	value = int(request.form.get('value'))
	value2 = int(request.form.get('value2'))
	hap = value+value2
	nums.append(value)
	return redirect("/result")

	
@app.route("/result")
def result():
	return render_template("result.html", nums=nums,hap=hap)
app.run(debug=True)