import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from django.contrib.auth.models import User
from ..models import Question

def create_question(question_text, days):
    """
    与えられた引数でQuestionのインスタンスを生成する(引数の日付は現在時刻との日付差、正が未来、負が過去)
    """
    time = timezone.now() + datetime.timedelta(days=days)
    user = User.objects.create_user('test_user', 'test@sample.com', 'test_password')
    return Question.objects.create(question_text=question_text, pub_date=time,author=user)


class QuestionModelTests(TestCase):
    def test_saving_and_retrieving_post(self):
        """内容を指定してデータを保存し、すぐに取り出した時に保存した時と同じ値が返されることをテスト"""
        question = create_question(question_text="", days=0)
        question_text = "test_auestion_text"
        pub_date = timezone.now()
        question.question_text = question_text
        question.pub_date = pub_date
        question.save()

        saved_questions = Question.objects.all()
        actual_question = saved_questions[0]

        self.assertEqual(actual_question.question_text, question_text)
        self.assertEqual(actual_question.pub_date, pub_date)

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recentlyが未来の日付に対してFalseを返すこと
        """
        future_question = create_question(question_text="", days=30)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recentlyが１日より前の日付に対してFalseを返すこと
        """
        old_question = create_question(question_text="", days=-1.1)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recentlyが１日以内の日付に対してTrueを返すこと
        """
        recent_question = create_question(question_text="", days=-0.9)
        self.assertIs(recent_question.was_published_recently(), True)



