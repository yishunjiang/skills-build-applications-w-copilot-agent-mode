from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["octofit_db"]

# Collections
users_collection = db["users"]
teams_collection = db["teams"]
activity_collection = db["activity"]
leaderboard_collection = db["leaderboard"]
workouts_collection = db["workouts"]