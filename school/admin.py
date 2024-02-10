from django.contrib import admin

from school.models import Course, Lesson, Payments, Subscription


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'owner', 'price')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'course', 'owner', 'video', 'price')


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'course', 'lesson', 'date', 'pay', 'method')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'course', 'is_active')
