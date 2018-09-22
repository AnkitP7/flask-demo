'''
Author: Ankit Patel
This file defines the methods that are used for routing to app. functions
'''
from flask import Flask,render_template,redirect,url_for,request
import requests,json
app=Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template("index.html")


@app.route('/search',methods=['GET'])
def search():
    if(request.method == "GET"):
        city=request.args.get("city")
        '''Define your own key from apixu.com
           Warning: Always define API_KEYS in a seperate file.
           The API_KEY declared here is not recommended and should never be declared directly in 
           production enviroment
        '''
        API_KEY="---"
        url="https://api.apixu.com/v1/current.json?key=%s&q=%s"%(API_KEY,city)
        response=requests.get(url)
        cityDetails=response.json()
        return render_template("search.html",cityDetails=cityDetails)


@app.route('/about')
def about():
    return render_template('about.html')


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', title="404 Not Found"), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html', title="500 Internal Error"), 500


if __name__ == "__main__":
    app.run(debug="True")
