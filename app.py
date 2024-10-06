from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# show redirection hyperlinks to respective login pages 
@app.route("/")
def myindex():

    return render_template('main.html')

# simplicity purposes temp user and password dict to simulate user credential DB validation
users_db = {
    'batman': '1234',
    'superman': '1234', 
    'iceman': '1234'
    
}

failcredential = 'Credential Not Match'

# perform username and password checks
def passwdcheck(myname, mypwd):
    
    # username not matched return False
    if myname not in users_db:
            return False

    else:
        # password not matched return False
        if users_db[myname] != mypwd:
            return False
        else:
            return True

# login route to handle user credential submittion and checking; hx-response-error
@app.route('/login_prompt', methods=['POST','GET'])
def login_p():
    
    if request.method == 'POST':
        
        # get and record username and password submitted by form
        myname = request.form['Username']
        mypwd = request.form['password']
        
        # username or password not matched return HTTP 401 and message
        if passwdcheck(myname, mypwd) == False:
            return render_template('fail.html', info=failcredential), 401
        else:
            if passwdcheck(myname, mypwd) == False:
                return render_template('fail.html', info=failcredential), 401
            else:
                # username and password matched, return success greetings with username variable
                return render_template('success.html', name=myname)

    return render_template('login_prompt.html')

# login route to handle user credential submittion and checking; hx-target-error
@app.route('/login_swap', methods=['POST','GET'])
def login_s():
    
    
    if request.method == 'POST':
        
        # get and record username and password submitted by form
        myname = request.form['Username']
        mypwd = request.form['password']
        
        # username or password not matched return HTTP 401 and message
        if passwdcheck(myname, mypwd) == False:
            return render_template('fail.html', info=failcredential), 401
        else:
            if passwdcheck(myname, mypwd) == False:
                return render_template('fail.html', info=failcredential), 401
            else:
                # username and password matched, return success greetings with username variable
                return render_template('success.html', name=myname)

    return render_template('login_swap.html')