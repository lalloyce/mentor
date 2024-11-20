from django.contrib import admin
from .models import Mentor, Course, Event, Testimonial, Newsletter

# Register your models here.

@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('name', 'expertise', 'experience', 'email', 'is_featured')
    list_filter = ('expertise', 'is_featured')
    search_fields = ('name', 'email', 'expertise')
    list_editable = ('is_featured',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'mentor', 'price', 'students_enrolled', 'rating', 'is_featured')
    list_filter = ('category', 'is_featured', 'mentor')
    search_fields = ('title', 'description', 'mentor__name')
    list_editable = ('is_featured',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'current_participants', 'max_participants', 'is_featured')
    list_filter = ('is_featured', 'date', 'location')
    search_fields = ('title', 'description', 'location')
    list_editable = ('is_featured',)
    filter_horizontal = ('mentors',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'company', 'rating', 'is_featured')
    list_filter = ('rating', 'is_featured', 'company')
    search_fields = ('name', 'company', 'content')
    list_editable = ('is_featured',)

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('email',)
    list_editable = ('is_active',)
