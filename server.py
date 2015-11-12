from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "Secret"
import re
name_regex = re.compile(r'^[a-zA-Z]*$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():  
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def form_fields():
	if len(request.form['email']) < 1 or len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1 or len(request.form['password']) < 1 or len(request.form['confirm_password']) < 1:
		flash('Please input required fields.')
	elif str.isalpha('first_name') == False or str.isalpha('last_name') == False:
		flash('First or last name cannot contain numbers!')
	elif len(request.form['password']) < 8 or len(request.form['confirm_password']) < 8:
		flash('Password must be more than 8 letters.')
	elif not EMAIL_REGEX.match(request.form['email']):
		flash('Invalid email address!')
	elif request.form['password'] != request.form['confirm_password']:
		flash('Passwords do not match!')
	else:
		flash('Success!')
	return redirect('/')


app.run(debug=True)