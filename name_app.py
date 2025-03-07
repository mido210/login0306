# 명함 관리
# 명함 : 이름과 연락차 -> ({'name':'홍길동','tel':'1234'})
# 명함 리스트, 명함 추가, 명함 삭제 
from flask import Flask, render_template, redirect, request

# __name__은 현재 실행 실중인 모듈의 이름을 나타내는 내장 함수
# 모듈의 이름을 이용해서 templates, static 등을 관리한다
app = Flask(__name__)


name_cards =[{'name':'홍길동','tel':'1234'},{'name':'전우치','tel':'2345'}]

@app.route("/card/list")
def list():
	return render_template('card/list.html', name_cards=name_cards)

@app.route("/card/insert", methods=['post'])
def insert():
	name =request.form.get("name", None) 
	tel = request.form.get("tel", None)
	new_card ={'name':name, 'tel':tel}
	name_cards.append(new_card)
	return redirect("/card/list")
@app.route("/card/delate", methods=['post'])
def delate():
	name = request.form.get("name", None)
	for card in name_cards:
		if card['name']==name:
			name_cards.remove(card)
	return redirect("/card/list")

app.run(debug=True)