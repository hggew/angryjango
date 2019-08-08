from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib import admin

from apps.utils import TimeStampedModel


class UserManager(BaseUserManager):
    def create_user(self, user_id, student_id, password_question, password_answer, name, department, password=None):
        if not user_id:
            raise ValueError('아이디를 입력하세요')

        user = self.model(
            user_id=user_id,
            student_id=student_id,
            password_question=password_question,
            password_answer=password_answer,
            name=name,
            department=department
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, user_id, password=None):
        superuser = self.model(user_id=user_id)
        superuser.set_password(password)
        superuser.is_superuser = True
        superuser.is_staff = True
        superuser.save()
        return superuser


class User(AbstractBaseUser, TimeStampedModel, PermissionsMixin):
    user_id = models.CharField(max_length=64, unique=True, db_index=True)
    student_id = models.CharField(max_length=8, unique=True)
    password_question = models.CharField(max_length=64)
    password_answer = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    department = models.CharField(max_length=64)

    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = []

    objects = UserManager()


admin.site.register(User)

