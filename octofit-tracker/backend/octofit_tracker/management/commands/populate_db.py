import json
from pymongo import MongoClient
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        client = MongoClient("mongodb://localhost:27017/")
        db = client["octofit_db"]

        with open('octofit_tracker/test_data.json') as f:
            data = json.load(f)

        db.users.insert_many(data['users'])
        db.teams.insert_many(data['teams'])
        db.activity.insert_many(data['activities'])
        db.leaderboard.insert_many(data['leaderboard'])
        db.workouts.insert_many(data['workouts'])

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
