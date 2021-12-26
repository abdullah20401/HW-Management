import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Teacher, Assignment, Classroom


# Create your tests here.
class AssignmentTests(TestCase):
    def setUp(self):
        self.teacher = Teacher.objects.create(
            teacher_name='Test Teacher',
            teacher_email='testteacher@email.com',
            teacher_phone='+1 234 567 8910'
        ),

        self.classroom = Classroom.objects.create(
            class_name='Test Classroom',
            class_description='This is a description for Test Classroom',
            teacher=self.teacher,
            class_syllabus=''
        ),

        self.assignment = Assignment.objects.create(
            assignment_name='Test Assignment',
            assignment_description='This is a description for Test Assignment',
            assignment_class=self.classroom,
            date_assigned=timezone.now(),
            due_date=timezone.now() - datetime.timedelta(hours=1),
            file_attachment=''
        )

    def test_time_ago_with_old_assignment(self):
        """
        time_ago() returns False for questions whose due_date
        is older than the current time.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_time_ago_with_recent_assignment(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)