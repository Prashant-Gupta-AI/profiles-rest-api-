from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for tesing our APIview"""

    name = serializers.CharField(max_length=10)