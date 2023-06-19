import pickle


with open("london.model","rb") as f:	model=pickle.load(f)


ar=float(input("enter area: "))
bd=int(input("enter no of bedrooms: "))
bt=int(input("enter no of bathrooms: "))
rc=int(input("enter no of receptions: "))
ch=input("chelsea 0-no 1-yes: ")
es=input("essex 0-no 1-yes: ")
fu=input("fulham 0-no 1-yes: ")
lo=input("london 0-no 1-yes: ")
wi=input("wimbledon 0-no 1-yes: ")
d=[[ar,bd,bt,rc,ch,es,fu,lo,wi]]
res=model.predict(d)
print(round(res[0],2))