from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()



class Car(models.Model):
    name = models.CharField(max_length=15)
    capacity = models.IntegerField()
    # photo = models.ImageField(upload_to='img/car')
    description = models.TextField(default='')
    year = models.PositiveIntegerField(default=0000)
    wifi = models.BooleanField(default=False)
    car_style = models.CharField(max_length=50, default='sedan')
    air_codinting = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class CarImage(models.Model):
    image = models.ImageField(upload_to='img')
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

class TourThemes(models.Model):
    group_themes = models.CharField(max_length=100)  # Added max_length
    description = models.TextField()  # Changed to TextField

    def __str__(self):
        return f"{self.group_themes}--{self.description[:8]}"


class TourType(models.Model):
    with_gid = models.BooleanField()
    description = models.TextField()  # Changed to TextField
    country = models.CharField(max_length=100)  # Added max_length

    def __str__(self):
        return f'{self.country} - With Guide: {self.with_gid}'


class TourGroupDetail(models.Model):
    group_size = models.CharField(max_length=50)  # Added max_length
    description = models.TextField()  # Changed to TextField

    def __str__(self):
        return f'{self.group_size} - {self.description[:8]}'


class Tour(models.Model):
    
    price = models.DecimalField(decimal_places=2, max_digits=10)
    # car = models.OneToOneField(Car, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    place = models.CharField(max_length=20)
    # duration = models.IntegerField(default=1)
    tour_type = models.ForeignKey(TourType, on_delete=models.CASCADE)
    themes = models.ForeignKey(TourThemes, on_delete=models.CASCADE)
    group_detail = models.ForeignKey(TourGroupDetail,on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f'{self.place} - {self.price}'

class Image(models.Model):
    img = models.ImageField(upload_to='img')
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)


class Booking(models.Model):
    first_name = models.CharField(max_length=20,default='')
    second_name = models.CharField(max_length=20,default='')
    phone_number = models.TextField(default='')
    duration = models.IntegerField(default=1)
    tour = models.ForeignKey(Tour, default=None, on_delete=models.CASCADE)
    car = models.OneToOneField(Car, default=None,on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.car}--{self.tour}'


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

    def __str__(self):
        return f'review {self.author}-{self.name}'





