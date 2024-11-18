from rest_frameworks import serializers
from .models import Mentor

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'