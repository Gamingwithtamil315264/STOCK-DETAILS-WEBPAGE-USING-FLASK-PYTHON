from flask import Flask,render_template,request,send_file
import os
import json
import plotly.graph_objects as go
import yfinance as yf
import pandas as pd
import plotly
import plotly.express as px
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('stock.html')
@app.route('/company',methods=['GET', 'POST'])
def submitted():
    k=[]
    if request.method == 'POST':
        f=request.form['fname']
        if f!="":
            h=f.upper()+".NS"
            dhr = yf.Ticker(h)
            info = dhr.info
            del info['longBusinessSummary']
            del info['companyOfficers']
            i=info.keys()
            print(info)
            for ik in i:
                k.append((ik,info[ik]))
            print(k)
            d = dhr.history(period='max')
            d.reset_index(inplace=True)
            full_graph_data = {
                "date": d["Date"].dt.strftime('%Y-%m-%d').tolist(),
                "close": d["Close"].tolist()
            }
            return render_template('stock.html',fname=f.upper(),k=k,full_graph_data=json.dumps(full_graph_data))
        return render_template('stock.html')
if __name__=="__main__":
    app.run(debug=True)
