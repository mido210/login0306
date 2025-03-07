from flask import Flask, render_template, request,redirect
app = Flask(__name__)

name_cards=[{'cno':1,'name':'spring','tel':'1234'},{'cno':2,'name':'summer','tel':'2345'}]
cno=3

@app.route("/card/list")
def list():
	error=request.args.get('error')
	message=''
	if error == 'insert':
		message='연락처가 이미 존재합니다'
	elif error== 'delete':
		message='연락처를 찾을 수 없습니다'
	return render_template("card2/list.html", name_cards=name_cards, message=message)



@app.route("/card/insert", methods=['post'])
def insert():
	global cno
	
	name=request.form.get('name', None)
	tel= request.form.get('tel', None)
	# 중복이면 에러처리 
	# 중복된 명함이 있다면 /card/list로 이동(에러 코드를 포함)
	for card in name_cards:
		if card['name']==name and card['tel']==tel:
			return redirect("/card/list?error=insert")
	new_card = {'cno':cno, 'name':name, 'tel':tel}
	name_cards.append(new_card)
	cno+=1
	return redirect("/card/list")


@app.route("/card/delete", methods=['post'])
def delete():
	# 없는 경우 -> 오류처리
	cno = int(request.form.get("cno", None))
	for card in name_cards:
		if card['cno']==cno:
			name_cards.remove(card)
			return redirect("/card/list")
	return redirect("/card/list?error=delete")






app.run(debug=True)