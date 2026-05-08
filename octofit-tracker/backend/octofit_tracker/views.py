from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from .models import users_collection, teams_collection, activity_collection, leaderboard_collection, workouts_collection

CODESPACE_URL = "http://localhost:8000"  # Replace with your actual codespace URL

class UserListView(APIView):
    def get(self, request):
        users = list(users_collection.find())
        return JsonResponse({"codespace_url": CODESPACE_URL, "data": UserSerializer(users, many=True).data})

class TeamListView(APIView):
    def get(self, request):
        teams = list(teams_collection.find())
        return JsonResponse({"codespace_url": CODESPACE_URL, "data": TeamSerializer(teams, many=True).data})

class ActivityListView(APIView):
    def get(self, request):
        activities = list(activity_collection.find())
        return JsonResponse({"codespace_url": CODESPACE_URL, "data": ActivitySerializer(activities, many=True).data})

class LeaderboardListView(APIView):
    def get(self, request):
        leaderboard = list(leaderboard_collection.find())
        return JsonResponse({"codespace_url": CODESPACE_URL, "data": LeaderboardSerializer(leaderboard, many=True).data})

class WorkoutListView(APIView):
    def get(self, request):
        workouts = list(workouts_collection.find())
        return JsonResponse({"codespace_url": CODESPACE_URL, "data": WorkoutSerializer(workouts, many=True).data})