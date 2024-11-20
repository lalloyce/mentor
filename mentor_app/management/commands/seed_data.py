from django.core.management.base import BaseCommand
from django.utils import timezone
from mentor_app.models import Mentor, Course, Event, Testimonial, Newsletter
from django.contrib.auth.models import User
from django.core.files import File
import random
from datetime import timedelta
import os

class Command(BaseCommand):
    help = 'Seeds the database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')
        
        # Create superuser if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write('Superuser created')

        # Create Mentors
        mentor_data = [
            {
                'name': 'John Smith',
                'expertise': 'Web Development',
                'experience': 8,
                'email': 'john.smith@example.com',
                'bio': 'Senior web developer with 8+ years of experience in full-stack development. Specialized in React and Django.',
                'social_twitter': 'https://twitter.com/johnsmith',
                'social_linkedin': 'https://linkedin.com/in/johnsmith',
                'is_featured': True
            },
            {
                'name': 'Sarah Johnson',
                'expertise': 'Data Science',
                'experience': 6,
                'email': 'sarah.j@example.com',
                'bio': 'Data scientist with expertise in machine learning and AI. Previously worked at Google and Amazon.',
                'social_twitter': 'https://twitter.com/sarahj',
                'social_linkedin': 'https://linkedin.com/in/sarahj',
                'is_featured': True
            },
            {
                'name': 'Michael Chen',
                'expertise': 'Mobile Development',
                'experience': 7,
                'email': 'michael.c@example.com',
                'bio': 'iOS and Android developer with a passion for creating beautiful mobile experiences.',
                'social_twitter': 'https://twitter.com/michaelc',
                'social_linkedin': 'https://linkedin.com/in/michaelc',
                'is_featured': True
            },
            {
                'name': 'Emma Wilson',
                'expertise': 'UI/UX Design',
                'experience': 5,
                'email': 'emma.w@example.com',
                'bio': 'Creative designer focusing on user-centered design principles and modern UI patterns.',
                'social_twitter': 'https://twitter.com/emmaw',
                'social_linkedin': 'https://linkedin.com/in/emmaw',
                'is_featured': False
            },
        ]

        for data in mentor_data:
            Mentor.objects.get_or_create(
                email=data['email'],
                defaults=data
            )
        self.stdout.write('Mentors created')

        # Create Courses
        mentors = Mentor.objects.all()
        course_data = [
            {
                'title': 'Modern Web Development with React & Django',
                'description': 'Learn to build full-stack web applications using React for the frontend and Django for the backend.',
                'category': 'web_dev',
                'price': 499.99,
                'duration': 12,
                'students_enrolled': 156,
                'rating': 4.8,
                'is_featured': True
            },
            {
                'title': 'Data Science Fundamentals',
                'description': 'Master the basics of data science, including Python, pandas, and machine learning fundamentals.',
                'category': 'data_science',
                'price': 599.99,
                'duration': 10,
                'students_enrolled': 203,
                'rating': 4.9,
                'is_featured': True
            },
            {
                'title': 'iOS App Development with Swift',
                'description': 'Create beautiful iOS applications using Swift and modern development practices.',
                'category': 'mobile_dev',
                'price': 449.99,
                'duration': 8,
                'students_enrolled': 128,
                'rating': 4.7,
                'is_featured': True
            },
            {
                'title': 'UI/UX Design Principles',
                'description': 'Learn the fundamentals of user interface and user experience design.',
                'category': 'design',
                'price': 399.99,
                'duration': 6,
                'students_enrolled': 175,
                'rating': 4.6,
                'is_featured': False
            },
            {
                'title': 'Digital Marketing Essentials',
                'description': 'Master the fundamentals of digital marketing, including SEO, social media, and content marketing.',
                'category': 'marketing',
                'price': 299.99,
                'duration': 4,
                'students_enrolled': 245,
                'rating': 4.5,
                'is_featured': False
            },
        ]

        for data in course_data:
            mentor = random.choice(mentors)
            Course.objects.get_or_create(
                title=data['title'],
                defaults={**data, 'mentor': mentor}
            )
        self.stdout.write('Courses created')

        # Create Events
        event_data = [
            {
                'title': 'Web Development Workshop',
                'description': 'Hands-on workshop covering the latest web development technologies and practices.',
                'date': timezone.now() + timedelta(days=15),
                'location': 'Online',
                'max_participants': 50,
                'current_participants': 32,
                'is_featured': True
            },
            {
                'title': 'Data Science Conference',
                'description': 'Annual conference featuring talks from industry experts in data science and AI.',
                'date': timezone.now() + timedelta(days=30),
                'location': 'San Francisco, CA',
                'max_participants': 200,
                'current_participants': 145,
                'is_featured': True
            },
            {
                'title': 'Mobile Dev Meetup',
                'description': 'Monthly meetup for mobile developers to network and share knowledge.',
                'date': timezone.now() + timedelta(days=7),
                'location': 'Online',
                'max_participants': 100,
                'current_participants': 78,
                'is_featured': False
            },
        ]

        for data in event_data:
            event, created = Event.objects.get_or_create(
                title=data['title'],
                defaults=data
            )
            if created:
                event.mentors.set(random.sample(list(mentors), 2))
        self.stdout.write('Events created')

        # Create Testimonials
        testimonial_data = [
            {
                'name': 'Alex Thompson',
                'position': 'Software Engineer',
                'company': 'Google',
                'content': 'The web development course was exactly what I needed to transition into tech. Great instructors and practical projects!',
                'rating': 5,
                'is_featured': True
            },
            {
                'name': 'Lisa Chen',
                'position': 'Data Analyst',
                'company': 'Amazon',
                'content': 'The data science program provided me with the skills I needed to land my dream job. Highly recommended!',
                'rating': 5,
                'is_featured': True
            },
            {
                'name': 'James Wilson',
                'position': 'Mobile Developer',
                'company': 'Apple',
                'content': 'Outstanding mobile development course. The hands-on projects were particularly valuable.',
                'rating': 4,
                'is_featured': True
            },
            {
                'name': 'Maria Garcia',
                'position': 'UX Designer',
                'company': 'Microsoft',
                'content': 'The UI/UX design course was comprehensive and well-structured. It helped me improve my design skills significantly.',
                'rating': 5,
                'is_featured': True
            },
        ]

        for data in testimonial_data:
            Testimonial.objects.get_or_create(
                name=data['name'],
                defaults=data
            )
        self.stdout.write('Testimonials created')

        # Create Newsletter Subscriptions
        newsletter_emails = [
            'subscriber1@example.com',
            'subscriber2@example.com',
            'subscriber3@example.com',
            'subscriber4@example.com',
        ]

        for email in newsletter_emails:
            Newsletter.objects.get_or_create(email=email)
        self.stdout.write('Newsletter subscriptions created')

        self.stdout.write(self.style.SUCCESS('Successfully seeded database'))
