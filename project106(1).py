import csv
import numpy as n
import plotly_express as px
def plotGraph(data):
    with open(data) as csvFile:
        csvReader=csv.DictReader(csvFile)
        p=px.scatter(csvReader,x="Coffee in ml",y="sleep in hours")
        p.show()
def getDataSource(dp):
    CoffeeTime=[]
    SleepTime=[]
    with open(dp) as csvFile:
        csvReader=csv.DictReader(csvFile)
        for row in csvReader:
            CoffeeTime.append(float(row["Coffee in ml"]))
            SleepTime.append(float(row["sleep in hours"]))
        return{"x":CoffeeTime, "y":SleepTime}
def findCorelation(ds):
    corelation=n.corrcoef(ds["x"],ds["y"])
    print(" corelation between coffee time and sleep time is ==>"+str(corelation[-1,1]))
def setup():
    data="csv4.csv"
    ds=getDataSource(data)
    findCorelation(ds)
    plotGraph(data)
setup()