from django.db import models
from django.utils import timezone

class Parent(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Book(models.Model):
    book_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.book_name

class Unit(models.Model):
    unit_number = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.book.book_name + " - Unit " + str(self.unit_number)

class Section(models.Model):
    section_number = models.IntegerField()
    unit = models.ForeignKey(Unit, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.unit.book.book_name + " - Unit " + str(self.unit.unit_number) + "." + str(self.section_number)

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    grade = models.IntegerField()
    date_of_birth = models.DateField(default=timezone.now)
    awana_bucks = models.IntegerField(default=0)
    parent = models.ForeignKey(Parent, on_delete=models.DO_NOTHING)
    completed_sections = models.ManyToManyField(Section, default=None, through='CompletedSection')

    def __str__(self):
        return self.first_name + " " + self.last_name
    

class CompletedSection(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    section = models.ForeignKey(Section, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['section__unit__book__book_name', 'section__unit__unit_number', 'section__section_number']


    def __str__(self) -> str:
        return ""
    
class Classroom(models.Model):
    class_name = models.CharField(max_length=100)
    year = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
