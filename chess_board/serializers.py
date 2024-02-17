from rest_framework import serializers


class PositionsSerializer(serializers.Serializer):
    Knight = serializers.CharField(required=True)
    Queen = serializers.CharField(required=True)
    Bishop = serializers.CharField(required=True)
    Rook = serializers.CharField(required=True)