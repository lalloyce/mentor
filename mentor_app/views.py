from django.shortcuts import render
from .serializers import MentorSerializer
from mentor.models import Mentor
from rest_frameworks import viewsets

# Create your views here.
def home(request):
    return render(request, 'index.html')

class Mentorview(viewsets.ModelViewSet):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer







