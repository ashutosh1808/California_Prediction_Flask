from flask import Flask,render_template,request
import pickle
from forex_python.converter import * 

app=Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/pred",methods=["POST"])
def pred():
	ar=float(request.form["ar"])	
	bd=int(request.form["bd"])
	bt=int(request.form["bt"])
	rc=int(request.form["rc"])
	lc=request.form["lc"]
	match lc:
		case "Chelsea":	d=[[ar,bd,bt,rc,1,0,0,0,0]]
		case "Fulham":	d=[[ar,bd,bt,rc,0,1,0,0,0]]
		case "Essex":	d=[[ar,bd,bt,rc,0,0,1,0,0]]
		case "London":	d=[[ar,bd,bt,rc,0,0,0,1,0]]
		case "Wimbledon":d=[[ar,bd,bt,rc,0,0,0,0,1]]
	#msg=str(ar)+" "+str(bd)+" "+str(bt)+" "+str(rc)+" "+str(lc)
	#"Price in GBP= £"+str(res)+" "
	with open("london.model","rb") as f:
		model=pickle.load(f)
	res=round(model.predict(d)[0],0)
	#c=CurrencyRates()
	#res_inr=c.convert('GBP','INR',res)
	per_sqft=res//ar
	msg="Prediction= "+"£"+str(res)+" "+"\n"+"Rate = "+"£"+str(per_sqft)+"/sq.ft."
	return render_template("home.html",msg=msg)

if __name__=="__main__":
	app.run(debug=True,use_reloader=True)
