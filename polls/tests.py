import datetime
from django.utils import timezone
from django.test import TestCase

from .models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date is in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date is mode than 1 day ago
        """
        time_older_than_one_day = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time_older_than_one_day)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_publichsed_recently() returns True for questions whse pub_date is less than 1 day ago
        """
        time_less_than_one_day_ago = timezone.now() - datetime.timedelta(hours=15)
        recent_question = Question(pub_date=time_less_than_one_day_ago)
        self.assertIs(recent_question.was_published_recently(), True)

