from django.test import TestCase
from rest_framework.test import APIClient

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_users_endpoint(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)

    def test_teams_endpoint(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, 200)

    def test_activity_endpoint(self):
        response = self.client.get('/api/activity/')
        self.assertEqual(response.status_code, 200)

    def test_leaderboard_endpoint(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, 200)

    def test_workouts_endpoint(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, 200)