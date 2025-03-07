from flask import Flask, request,redirect,render_template
import datetime 

app=Flask(__name__)

todos = [ {'tno':1,'title':'치킨데이','date':'2025-03-07','finish':False}
				 ,{'tno':2,'title':'청소','date':'2025-03-10','finish':True}
				]
tno =3
@app.route("/todo/list")
def list():
	return render_template("todo/list.html",todos=todos)

@app.route("/todo/insert", methods=['post'])
def insert():
	global tno
	title=request.form.get('title',None)
	# date_str= datetime.datetime.now().strftime("%Y-%m-%d")
	date_str= request.form.get('date')
	new_todo= {'tno':tno, 'title':title, 'date': date_str,'finish': False}
	todos.append(new_todo)
	tno+=1
	return redirect("/todo/list")

@app.route("/todo/toggle", methods=['post'])
def toggle():
	tno = int(request.form.get('tno'))
	for todo in todos:
		if todo['tno']==tno:
			todo['finish'] = not todo['finish']
	return redirect("/todo/list")

@app.route("/todo/delete", methods=['post'])
def delete():
	tno = int(request.form.get('tno'))
	for todo in todos:
		if todo['tno']==tno:
			todos.remove(todo)
	return redirect("/todo/list")


app.run(debug=True)