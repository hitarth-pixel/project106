import numpy as p1
import plotly_express as p2
import csv

def plotGraph(d):
    with open(d) as csvFile:
        r=csv.DictReader(csvFile)
        g=p2.line(r,x="Marks In Percentage",y="Days Present",color="Roll No")
        g.show()
def getDataSource(ds):
    StuSco=[]
    StuPre=[]
    with open(ds) as csvFile:
        r=csv.DictReader(csvFile)
        for row in r:
            StuPre.append(float(row["Days Present"]))
            StuSco.append(float(row["Marks In Percentage"]))
        return{"x":StuPre,"y":StuSco}
def findCorelation(dts):
    corelation=p1.corrcoef(dts["x"],dts["y"])
    print("corelation b/w students marks and their no. of days present ==> "+str(corelation[-1,1]))
def setup():
    d="csv3.csv"
    plotGraph(d)
    dts=getDataSource(d)
    findCorelation(dts)
setup()
