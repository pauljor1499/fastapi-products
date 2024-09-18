from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://admin:admin@cluster0.aeltnpt.mongodb.net/")  # Replace with your MongoDB connection string
db = client['test-product']  # Create or connect to a database
collection = db['products']  # Create or connect to a collection
