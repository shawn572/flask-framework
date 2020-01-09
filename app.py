from flask import Flask, render_template, request, redirect
import requests
import quandl
from pandas import *
from bokeh.io import show
from bokeh.models import DatetimeTickFormatter
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.resources import CDN
from datetime import datetime as dt

app = Flask(__name__)

quandl.ApiConfig.api_key = "Uh_reSthhw5fLxLWnFnF"

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        ticker = request.form['ticker']
        ticker_input = 'WIKI/' + ticker
        try:
            data = quandl.get(ticker_input, rows = 30)
            p = figure(plot_height=300,plot_width=800,x_axis_type="datetime"\
                       ,title="Stock Closing Prices for the last 30 Days in Quandl(wiki) Database"\
                       ,background_fill_color="#efefef")
            p.line(data.index, data['Close'].values)
            p.yaxis.axis_label = 'Close Price'
            p.xaxis.formatter=DatetimeTickFormatter(
            hours=["%d %B %Y"],
            days=["%d %B %Y"],
            months=["%d %B %Y"],
            years=["%d %B %Y"],
            )
            script, div = components(p)
        except:
            return render_template('about.html')
        return render_template('bokeh.html',script=script,div=div)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)
