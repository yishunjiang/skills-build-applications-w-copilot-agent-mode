from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    email = serializers.EmailField()

class TeamSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    members = serializers.ListField()

class ActivitySerializer(serializers.Serializer):
    id = serializers.CharField()
    user_id = serializers.CharField()
    type = serializers.CharField()
    duration = serializers.IntegerField()

class LeaderboardSerializer(serializers.Serializer):
    id = serializers.CharField()
    user_id = serializers.CharField()
    points = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()