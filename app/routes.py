from app import app, db
from flask import render_template, redirect, request, jsonify
from app.models import User, Message

@app.route('/')
@app.route('/index')
def index():
   return render_template('index.html')

@app.route('/AddMessage',methods = ['POST', 'GET'])
def AddMessage():
   if request.method == 'POST':
       data = request.form
       user_id = data['user_id']
       content = data['content']
       paticipants = [data['participant1'],data['participant2'],data['participant3']]
       m = Message(user_id=user_id,content=content,participants=paticipants)
       db.session.add(m)
       db.session.commit()
       return 'Your message has been successfully saved'

@app.route('/GetMessage')
def GetMessage():
    global messages
    application_id = request.args.get('application_id')
    if application_id:
        messages = Message.query.filter_by(user_id=application_id)
    session_id = request.args.get('session_id')
    if session_id:
        messages = Message.query.filter_by(session_id=session_id)    
    message_id = request.args.get('message_id')
    if message_id:
        messages = Message.query.filter_by(message_id=message_id) 
    return jsonify([m.as_dict() for m in messages])

@app.route('/DeleteMessage', methods=['GET'])
def DeleteMessage():
    global messages
    application_id = request.args.get('application_id')
    if application_id:
        messages = Message.query.filter_by(user_id=application_id)
    session_id = request.args.get('session_id')
    if session_id:
        messages = Message.query.filter_by(session_id=session_id)    
    message_id = request.args.get('message_id')
    if message_id:
        messages = Message.query.filter_by(message_id=message_id)

    for m in messages:  
        db.session.delete(m)
        db.session.commit()
    return 'The message has been deleted'




