from django.db import models
from configurations.models import RoomType, RoomStatus, Location
from django.contrib.auth.models import User
class Room(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # إضافة حقل المستخدم
    room_no = models.CharField(max_length=10, unique=True)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    room_status = models.ForeignKey(RoomStatus, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    number_of_beds = models.IntegerField()
    is_available = models.BooleanField(default=True)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.room_no} - {self.room_status} - {self.number_of_beds} beds"
