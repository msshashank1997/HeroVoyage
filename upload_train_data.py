import csv
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# MongoDB connection
client = MongoClient(os.getenv('MONGO_URI'))
db = client.hero_voyage
transports_collection = db.transports

def upload_train_data():
    """Uploads train data from train_data.csv to MongoDB."""
    with open('train_data.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['available_seats'] = int(row['available_seats'])  # Convert to integer
            transports_collection.update_one(
                {'train_number': row['train_number']},
                {'$set': row},
                upsert=True
            )
    print("Train data uploaded to MongoDB.")

def test_test_data():
    """Fetch and display train data from MongoDB."""
    try:
        # Fetch all documents from the transports collection
        trains = transports_collection.find()
        print("Train data from MongoDB:")
        for train in trains:
            print(train)  # Print each document (train data)
    except Exception as e:
        print(f"An error occurred while testing train data: {e}")

if __name__ == '__main__':
    print("Choose an option:")
    print("1. Upload train data")
    print("2. Test train data")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        upload_train_data()
    elif choice == '2':
        test_test_data()
    else:
        print("Invalid choice. Exiting.")