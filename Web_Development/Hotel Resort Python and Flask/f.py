from flask import Flask, render_template, request
from datetime import datetime
import re
import csv
import time

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')
	

@app.route('/attractions')
def attractions():
	return render_template('attractions.html')
	

@app.route('/about')
def about():
	return render_template('about.html')


# admin can see booking info	
@app.route('/admin')
def admin():
    return render_template('bookingInfo.html')
	
@app.route('/admin/info')
def info():
	fileName = 'static\\booking.csv'
	bookingForm = readFile(fileName)
	writeFile(bookingForm,fileName)
	return render_template('bookingDetails.html',bookingForm=bookingForm)
	
	
@app.route('/bookingForm')
def bookingForm():
	return render_template('bookingForm.html')
	
@app.route('/booking', methods=['POST'])
def booking():
	#fileName = 'static\\booking.csv'
	#bookingForm = readFile(fileName)
	name = request.form[('name')]
	email = request.form[('email')]
	sDate = request.form[('arrival')]
	eDate = request.form[('depart')]
	confirmed = ('no')
	newEntry =[name,email,sDate,eDate,confirmed]
	fileName = 'static\\booking.csv'
	bookingForm = readFile(fileName)
	bookingForm.append(newEntry)
	writeFile(bookingForm,fileName)
	return render_template('details.html',name=name,email=email,sDate=sDate,eDate=eDate,confirmed=confirmed)

@app.route('/comments')
def comments():
    #read the skills list from file
    fileName = 'static\\comments.csv'
    commentList = readFile(fileName)
    return render_template('comments.html',commentList=commentList)
	
	
@app.route('/comments', methods = ['POST'])
def addComment():
    #read the skills list from file
    fileName = 'static\\comments.csv'
    commentList = readFile(fileName)
    # add an entry to the skills list
    newName = request.form[('name')]
    newComment = request.form[('comment')]
    newEntry=[newName, newComment]
    commentList.append(newEntry)
    #save the skills list to the file
    writeFile(commentList, fileName)
    return render_template('comments.html',commentList=commentList)

@app.route('/comment')	
def event():
	fileName = 'static\\list.csv'
	events = readFile(fileName)
	return render_template('comment.html',events=events)

	
@app.route('/addComment', methods = ['post'])
def addEvent():
	#add an event
	event = request.form[('event')]
	comment = request.form[('comment')]
	now = datetime.now()
	format = " (%d-%m-%Y %H:%M)"
	now = now.strftime(format)
	newEvent = [event,comment,now]
	fileName = 'static\\list.csv'
	events = readFile(fileName)
	events.append(newEvent)
	writeFile(events, fileName)
	return render_template('comment.html', events=events)

@app.route('/clearComments', methods = ['POST'])
def clearComments():
    fileName = 'static\\list.csv'
    events = readFile(fileName)
    f = open(fileName, 'w')
    f.close()
    return  render_template('comment.html', events=events)
	
def readFile(aFile):
#read a file and return a list
    with open(aFile, 'r') as inFile: 
        reader = csv.reader(inFile)
        aList = [row for row in reader]
    return aList

def writeFile(aList, aFile):
#write a list to file
    with open(aFile, 'w', newline='') as outFile:
        writer = csv.writer(outFile)
        print(aList)
        writer.writerows(aList)      
    return	
	
if __name__ == '__main__':
    app.run(debug = True)
