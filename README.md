
        MESSAGING APP
------------------------------ 


INTRODUCTION
------------
This app allows users to share their friends with messages, view messages received for them, and delete as needed. Right now you can find almost only server-side code here, except for a single html page with no graphic design. But of course adding html pages and graphic design is very easy..

INSTALLATION
------------
I developed this app in Python using Flask - a great web development environment used in Python.<br>
It is very easy to start using flask, and these are the required installations (for command-line execution)<br>
First of all I recommend creating a virtual environment as follows:<br>
<python -m venv [verv_name_of_your_choice]><br>
Now you have to activate it like this:<br>
<[your_venv_name]\Scripts\activate><br>
Now you only have to install flask:<br>
<pip install flask><br>
That's it. You're in!<br>

Note! In this app I use a database to store the data (SQlite). I'm sure there are many more ways to do this, but I chose this way ...<br>
To use sqlite you will need to perform the following installations:<br>
<(venv) $ pip install flask-sqlalchemy><br>
<(venv) $ pip install flask-migrate><br>

USING THIS APP
----------------
This guide I prefer to write in the form of questions and answers for ease of reading ...<br>
Q. How to send a message?<br>
A. When you navigate to the address http://{host_ip}:{port}/ Or alternatively to the address http://{host_ip}:{port}/index, You will get an html page where you can enter the message content and recipient names. Clicking the submit button activates the <AddMessage> function that creates a new message and stores it in the database.<br>
Q. How to get messages?
A. The messages can be received in 3 forms:
- By application_id (which is actually the user_id. That is, if we had a button navigating to that address, the caption was: "Get all your messages") 
http://{host_ip}:{port}/GetMessage?application_id=
- By session_id 
http://{host_ip}:{port}/GetMessage?session_id=
- And according to the message_id - that is to receive a specific message
http://{host_ip}:{port}/GetMessage?message_id=
Q. How to delete messages?
A. That's easy:
- http://{host_ip}:{port}/DeleteMessage?application_id= 
To delete all messages from a particular user
- http://{host_ip}:{port}/DeleteMessage?session_id= 
To delete all messages by session_id
- http://{host_ip}:{port}/DeleteMessage?message_id= 
To delete one specific message

DESIGN DECISIONS
----------------
In fact, the only thing I wasn't sure about was this:
Setting the session_id for user - I thought of doing this by combining the time, date, and user_id. But if so - the same user's access from multiple computers should not be allowed ,to make sure the session number remains unique. (Because this allows only one specific user login at a specific date and time)
So, when a user requests or deletes all messages with a certain session_id, it usually means - all my messages, from current sign in to the app.
Because at this stage, there is no application sign-in form - I left it that way. But of course this should be addressed.

And here are 6 things to do (And I'm definitely going to do that soon ..) to make this code (almost) perfect:
--------------------------------------------------------------------------------------------------------
1. Lazy loading. After all, you do not want to allow your user to request a huge amount of messages from the server..
2. Use LoginManager to keep the user_id even when moving between pages. And, in general, to allow sign_ins and sign-ups.
3. Using wtf-flask to simplify all file handling, fields validation testing, etc.
4. And of course, a little graphic design will be very effective here ...

***Keren Menachem***
