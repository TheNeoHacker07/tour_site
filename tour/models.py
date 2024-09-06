from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Car(models.Model):
    name = models.CharField(max_length=15)
    capacity = models.IntegerField()
    photo = models.ImageField(upload_to='img/car')
    description = models.TextField()
    year = models.PositiveIntegerField()
    wifi = models.BooleanField()
    car_type = models.CharField(max_length=50)
    air_codinting = models.BooleanField()

    def __str__(self):
        return self.name


class TourThemes(models.Model):
    group_themes = models.CharField()
    description = models.TimeField()

    def __str__(self):
        return f"{self.group_size}--{self.description[:8]}"


class TourType(models.Model):
    with_gid = models.BooleanField()
    description = models.TimeField()
    country  = models.CharField()

    def __str__(self):
        return self.with_gid

class TourGroupDetail(models.Model):
    group_size = models.CharField()
    description = models.TimeField()


class Tour(models.Model):
    image = models.ImageField(upload_to='img/tour')
    price = models.DecimalField(decimal_places=2, max_digits=10)
    car = models.OneToOneField(Car, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    place = models.CharField(max_length=20)
    duration = models.IntegerField()
    tour_type = models.ForeignKey(TourType, on_delete=models.DO_NOTHING)
    themes = models.ForeignKey(TourThemes, on_delete=models.DO_NOTHING)
    group_detail = models.ForeignKey(TourGroupDetail, on_delete=models.DO_NOTHING)
    start = models.DateTimeField()
    end = models.DateTimeField()
    
    def __str__(self):
        return f'{self.user}-{self.place}'



class Booking(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}--{self.tour}'


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    name = models.CharField(max_length=30)
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    mark = models.PositiveIntegerField(choices=RATING_CHOICES)


    def __str__(self) -> str:
        return f'review {self.user}-{self.name}'




