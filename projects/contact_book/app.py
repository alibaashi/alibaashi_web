# app.py

from flask import Flask, render_template, request, redirect, url_for
from contact_book import add_contact, find_contact, update_contact, delete_contact

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_contact', methods=['POST'])
def add_contact_route():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    add_contact(name, phone, email)
    return redirect(url_for('index'))

@app.route('/find_contact', methods=['POST'])
def find_contact_route():
    name = request.form['name']
    contact = find_contact(name)
    if contact:
        return f"Contact found: Name - {contact['name']}, Phone - {contact['phone']}, Email - {contact['email']}"
    else:
        return "Contact not found."

@app.route('/update_contact', methods=['POST'])
def update_contact_route():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    if update_contact(name, phone, email):
        return "Contact updated successfully!"
    else:
        return "Contact not found."

@app.route('/delete_contact', methods=['POST'])
def delete_contact_route():
    name = request.form['name']
    delete_contact(name)
    return "Contact deleted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
