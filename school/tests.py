from django.contrib.auth.models import Group
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from school.models import Lesson, Course, Subscription
from users.models import User


class SchoolTestCase(APITestCase):

    def setUp(self) -> None:

        # Grope "Moderator"
        self.group_moderator = Group.objects.create(name="moderator")

        # Moderator
        self.moderator = User.objects.create(
            email="moderator@test.com",
            is_staff=False,
            is_active=True,
        )
        self.moderator.set_password('test')
        self.moderator.groups.add(self.group_moderator)
        self.moderator.save()

        # User_1
        self.user_1 = User.objects.create(
            email="user1@test.com",
            is_staff=False,
            is_active=True,
        )
        self.user_1.set_password('test')
        self.user_1.save()

    def test_create_lesson(self):

        """Создание урока"""

        self.client.force_authenticate(user=self.user_1)

        data = {
            'title': 'create_lesson_test',
        }
        response = self.client.post(
            reverse("school:lesson_create"),
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {
                'id': 1,
                'title': 'create_lesson_test',
                'img': None,
                'video': None,
                'description': None,
                'course': None,
                'owner': self.user_1.id
            }
        )

        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_list_lessons(self):

        """Вывод списка уроков"""

        self.client.force_authenticate(user=self.user_1)

        lesson = Lesson.objects.create(
            title='title_list_lesson'
        )

        response = self.client.get(
            reverse("school:lesson_list")
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        'id': lesson.id,
                        'title': 'title_list_lesson',
                        'img': None,
                        'video': None,
                        'description': None,
                        'course': None,
                        'owner': None
                    }
                ]
            }
        )

    def test_retrieve_lesson(self):

        """Вывод урока"""

        self.client.force_authenticate(user=self.user_1)

        lesson = Lesson.objects.create(
            title='title_retrieve_lesson',
            owner=self.user_1
        )

        response = self.client.get(
            reverse("school:lesson_retrieve", kwargs={'pk': lesson.id})
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {
                'id': lesson.id,
                'title': 'title_retrieve_lesson',
                'img': None,
                'video': None,
                'description': None,
                'course': None,
                'owner': self.user_1.id
            }
        )

    def test_update_lesson(self):

        """Редактирование урока"""

        self.client.force_authenticate(user=self.user_1)

        lesson = Lesson.objects.create(
            title='title_retrieve_lesson',
            owner=self.user_1
        )

        data = {
            'title': 'title_update_lesson',
        }

        response = self.client.patch(
            reverse("school:lesson_update", kwargs={'pk': lesson.id}),
            data=data

        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {
                'id': lesson.id,
                'title': 'title_update_lesson',
                'img': None,
                'video': None,
                'description': None,
                'course': None,
                'owner': self.user_1.id
            }
        )

        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_destroy_lesson(self):

        """Удаление урока"""

        self.client.force_authenticate(user=self.user_1)

        lesson = Lesson.objects.create(
            title='title_destroy_lesson',
            owner=self.user_1
        )

        response = self.client.delete(
            reverse("school:lesson_destroy", kwargs={'pk': lesson.id})
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_create_subscription(self):
        """Создание подписки"""

        self.client.force_authenticate(user=self.moderator)

        course = Course.objects.create(
            title='title',
            owner=self.moderator
        )

        data = {
            'user': self.moderator.id,
            'course': course.id,
            'is_active': True
        }
        response = self.client.post(
            reverse("school:subscription_create"),
            data=data
        )

        print(response.json())

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {
                'pk': 1,
                'user': self.moderator.id,
                'course': 1,
                'is_active': True
            }
        )

        self.assertTrue(
            Subscription.objects.all().exists()
        )

    def test_destroy_subscription(self):

        """Удаление подписки"""

        self.client.force_authenticate(user=self.moderator)

        course = Course.objects.create(
            title='title',
            owner=self.moderator
        )

        subscription = Subscription.objects.create(
            user=self.moderator,
            course=course
        )

        response = self.client.delete(
            reverse("school:subscription_destroy", kwargs={'pk': subscription.id})
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
