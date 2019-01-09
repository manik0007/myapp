from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import json
import sys
try:
    import urllib.request as urllib3
except ImportError:
    import urllib3
import requests
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import urllib.request 
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
    email = TextField('Email:', validators=[validators.required()])
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
     
    print (form.errors)
    if request.method == 'POST':
        email=request.form['email']
        print (email)
     
    if form.validate():
    # Save the comment here.
        


        flag=0
        var=""
        try:
            link="http://142.93.220.192:8080/v1/json/"+email
            print(link)
            req = urllib2.Request(link)
            resp = urllib2.urlopen(req)
            respData = json.loads(resp.read())
            deliver=respData['deliverable']
            if(deliver==0):
                flash('Mail to this email is deliverable: false' )
            if(deliver==1):
                flash('Mail to this email is deliverable: true' )
            
            
            




            
        finally :
            pass







        
    else:
        flash('All the form fields are required. ')
     
    return render_template('hello.html', form=form)
 
if __name__ == "__main__":
    app.run()
