from django.contrib import admin
from .models import Parent, Student, Classroom, Book, Unit, Section, CompletedSection

admin.site.register([Parent, Classroom, Book, Unit])

class CompletedSectionsInline(admin.TabularInline):
    model = CompletedSection
    extra = 1

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    inlines = [CompletedSectionsInline]

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('section_number',)
    inlines = [CompletedSectionsInline]

