from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Mentor, Course, Event, Testimonial
from .serializers import MentorSerializer
from django.db.models import Count, Avg, Sum
from django.utils import timezone

def home(request):
    # Get featured courses
    featured_courses = Course.objects.filter(is_featured=True)[:3]
    
    # Get featured mentors
    featured_mentors = Mentor.objects.filter(is_featured=True)[:3]
    
    # Get upcoming events
    upcoming_events = Event.objects.filter(
        date__gte=timezone.now(),
        is_featured=True
    ).order_by('date')[:3]
    
    # Get featured testimonials
    testimonials = Testimonial.objects.filter(is_featured=True)[:4]
    
    # Calculate statistics
    stats = {
        'students': Course.objects.aggregate(total=Sum('students_enrolled'))['total'] or 0,
        'courses': Course.objects.count(),
        'events': Event.objects.count(),
        'mentors': Mentor.objects.count()
    }
    
    context = {
        'featured_courses': featured_courses,
        'featured_mentors': featured_mentors,
        'upcoming_events': upcoming_events,
        'testimonials': testimonials,
        'stats': stats
    }
    return render(request, 'index.html', context)

class Mentorview(viewsets.ModelViewSet):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

def about(request):
    mentors = Mentor.objects.all()
    testimonials = Testimonial.objects.filter(is_featured=True)[:6]
    stats = {
        'students': Course.objects.aggregate(total=Sum('students_enrolled'))['total'] or 0,
        'courses': Course.objects.count(),
        'events': Event.objects.count(),
        'mentors': Mentor.objects.count()
    }
    context = {
        'mentors': mentors,
        'testimonials': testimonials,
        'stats': stats
    }
    return render(request, 'about.html', context)

def courses(request):
    category = request.GET.get('category')
    search = request.GET.get('search')
    sort = request.GET.get('sort', '-created_at')
    
    courses = Course.objects.all()
    
    if category:
        courses = courses.filter(category=category)
    if search:
        courses = courses.filter(title__icontains=search) | courses.filter(description__icontains=search)
    
    courses = courses.order_by(sort)
    
    categories = Course.CATEGORY_CHOICES
    context = {
        'courses': courses,
        'categories': categories,
        'current_category': category,
        'current_sort': sort
    }
    return render(request, 'courses.html', context)

def trainers(request):
    mentors = Mentor.objects.annotate(
        course_count=Count('courses'),
        avg_rating=Avg('courses__rating')
    )
    context = {'mentors': mentors}
    return render(request, 'trainers.html', context)

def events(request):
    upcoming_events = Event.objects.filter(date__gte=timezone.now()).order_by('date')
    past_events = Event.objects.filter(date__lt=timezone.now()).order_by('-date')
    context = {
        'upcoming_events': upcoming_events,
        'past_events': past_events
    }
    return render(request, 'events.html', context)

def pricing(request):
    courses_by_category = {}
    for category_code, category_name in Course.CATEGORY_CHOICES:
        courses_by_category[category_name] = Course.objects.filter(category=category_code)
    context = {'courses_by_category': courses_by_category}
    return render(request, 'pricing.html', context)

def contact(request):
    if request.method == 'POST':
        # Handle contact form submission
        pass
    return render(request, 'contact.html')

def course_details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    related_courses = Course.objects.filter(category=course.category).exclude(id=course.id)[:3]
    context = {
        'course': course,
        'related_courses': related_courses
    }
    return render(request, 'course-details.html', context)

def starter_page(request):
    return render(request, 'starter-page.html')
