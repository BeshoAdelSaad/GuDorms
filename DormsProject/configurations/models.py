from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

class BaseModel(models.Model):
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # إضافة حقل المستخدم

    class Meta:
        abstract = True


class Location (BaseModel):
    """
    Represents the physical locations where the rooms are situated.
    """
      
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"
        ordering = ['name']

    def __str__(self):
        return self.name
    

class RateCode (BaseModel):

    name = models.CharField(max_length=150)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Rate Code"
        verbose_name_plural = "Rate Codes"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.id} - {self.name}"



class ActualStatuses (BaseModel):

    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Actual Status"
        verbose_name_plural = "Actual Statuses"
        ordering = ['name']

    def __str__(self):
        return self.name
    

class Penalities (BaseModel):

    name = models.CharField(max_length=255)
    penalty_number = models.IntegerField()
    value = models.IntegerField()

    class Meta:
        verbose_name = "Penalty"
        verbose_name_plural = "Penalties"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} (Code: {self.penalty_number}, Value: {self.value})"
    

class RoomType (BaseModel):
    """
    Represents the type of rooms (e.g., Single, Double).
    """

    name = models.CharField(max_length=255, unique=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Room Type"
        verbose_name_plural = "Room Types"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} - {self.location}"

class RoomStatus (BaseModel):
   
    """
    Represents the Room of Status (e.g., VC, VD, O.O.O,).
    """
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Room Status"
        verbose_name_plural = "Room Statuses"
        ordering = ['name']
    
    def __str__(self):
        return self.name
