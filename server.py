# the next two lines always need to be atop this server.py file 
from collections import UserList
from flask import Flask, render_template,  redirect, session # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'ESR4T4RWT2345tyu' 


# @app.route('/')          
# def welcome():
#     return render_template("index.html", horizDispCount = 1, vertDispCount = 1, color1 = "red", color2 = "black", displayValMsg = defaultValidationMsg, displayValStyle = defaultValStyle)

@app.route('/')
def countEmUp():
    if "counterCount" not in session: 
        session['counterCount'] = 0
    else:
        session['counterCount'] += 1
    return render_template("index.html")

@app.route('/destroy_session')
def killTheCount():
    session.pop('counterCount')		# clears a specific key
    return redirect('/')




"""DON'T TOUCH BELOW :-) below always needs to be at the bottom of the script, yes!"""
# below is stuff you oughta have, per TA Cameron Smith, from Coding Dojo: 

@app.route('/', defaults={'cookies': ''})
@app.route('/<path:cookies>')
def catch_all(cookies):
    return 'Sorry! No response here. Try url again.'

# below is flask boiler plate; exclude it and stuff won't work    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

