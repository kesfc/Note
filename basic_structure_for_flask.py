# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 16:44:53 2022

@author: kevin
"""

from flask import Flask

app = Flask(__name__) #referencing this file
@app.route('/') #pass teh url string here
def index():
    return "hello"
#this line can also be:
    #return render_template('index.html')
    #index.html is the html file already been created.
    
#define function for the route
if __name__ == "__main__":
    app.run()
