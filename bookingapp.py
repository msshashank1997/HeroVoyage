from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_pymongo import PyMongo
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os
import random
import csv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'testing_secret_key')  # Default key for testing
app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'mongodb://localhost:27017/hero_voyage')  # Default URI for testing

mongo = PyMongo(app)

# MongoDB Collections
users_collection = mongo.db.users
transports_collection = mongo.db.transports
bookings_collection = mongo.db.bookings

@app.route('/')
def home():
    return render_template('index.html', title='Hero-Voyage')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        role = request.form['role']
        existing_user = users_collection.find_one({'username': username})
        if existing_user:
            flash('Username already exists')
            return redirect(url_for('register'))
        users_collection.insert_one({'username': username, 'password': password, 'role': role})
        flash('Registered successfully! Please login.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users_collection.find_one({'username': username})
        if user and check_password_hash(user['password'], password):
            session['user_id'] = str(user['_id'])
            session['username'] = user['username']
            session['role'] = user['role']
            flash('Logged in successfully!')
            if user['role'] == 'admin':
                return redirect(url_for('admin_panel'))
            elif user['role'] == 'driver':
                return redirect(url_for('driver_panel'))
            else:
                return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out')
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session or session['role'] != 'user':
        return redirect(url_for('login'))
    transports = list(transports_collection.find())
    return render_template('dashboard.html', transports=transports)

@app.route('/admin')
def admin_panel():
    if 'user_id' not in session or session['role'] != 'admin':
        return redirect(url_for('login'))
    transports = transports_collection.find()
    return render_template('admin.html', transports=transports)

@app.route('/driver')
def driver_panel():
    if 'user_id' not in session or session['role'] != 'driver':
        return redirect(url_for('login'))
    transports = list(transports_collection.find())
    return render_template('driver.html', transports=transports)

@app.route('/book-ticket/<train_number>', methods=['GET', 'POST'])
def book_ticket(train_number):
    selected_train = transports_collection.find_one({'train_number': train_number})
    if request.method == 'POST':
        seats_to_book = int(request.form['seats'])
        available_seats = int(selected_train['available_seats'])
        if seats_to_book <= available_seats:
            # Update available seats in the database
            transports_collection.update_one(
                {'train_number': train_number},
                {'$set': {'available_seats': available_seats - seats_to_book}}
            )
            
            # Generate a random coach name (e.g., C1, C2, C3)
            coach_number = f"C{random.randint(1, 5)}"
            
            # Generate random seat numbers between 1 and 60
            seat_numbers = random.sample(range(1, 61), seats_to_book)
            seat_numbers_str = ', '.join(map(str, seat_numbers))
            
            flash(f"Booking successful! {seats_to_book} seat(s) booked.")
            return redirect(url_for('generate_receipt', train_number=train_number, seats=seats_to_book, coach=coach_number, seat_numbers=seat_numbers_str))
        else:
            flash(f"Not enough seats available. Only {available_seats} seat(s) left.")
    return render_template('book_ticket.html', train=selected_train)

@app.route('/generate-receipt')
def generate_receipt():
    train_number = request.args.get('train_number')
    seats = request.args.get('seats')
    coach_number = request.args.get('coach', 'C1')
    seat_numbers = request.args.get('seat_numbers', '1, 2')

    # Fetch the train details from the database using the train number
    train = transports_collection.find_one({'train_number': train_number})
    train_name = train['train_name'] if train else 'Unknown Train'
    receipt = {
        'train_name': train_name,
        'train_number': train_number,
        'seats': seats,
        'coach_number': coach_number,
        'seat_numbers': seat_numbers
    }
    return render_template('receipt.html', receipt=receipt)

if __name__ == '__main__':
    print("✅ Starting Hero-Voyage Flask App...")
    app.run(debug=True, use_reloader=False, port=4000)