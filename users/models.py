from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.core.validators import RegexValidator

SEX_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

BREED_CHOICES = (
    ('American Bulldog', 'American Bulldog'),
    ('Australian Shepherd', 'Australian Shepherd'),
    ('Basset Hound', 'Basset Hound'),
    ('Beagle', 'Beagle'),
    ('Border  Collie', 'Border  Collie'),
    ('Boston  Terrier', 'Boston  Terrier'),
    ('Boxer', 'Boxer'),
    ('Chihuahua', 'Chihuahua'),
    ('Cocker Spaniel', 'Cocker Spaniel'),
    ('Collie', 'Collie'),
    ('Corgi', 'Corgi'),
    ('Dachshund', 'Dachshund'),
    ('Dalmatian', 'Dalmatian'),
    ('Doberman Pinscher', 'Doberman Pinscher'),
    ('French Bulldog', 'French Bulldog'),
    ('German Shepherd', 'German Shepherd'),
    ('Golden Retriever', 'Golden Retriever'),
    ('Great Dane', 'Great Dane'),
    ('Greyhound', 'Greyhound'),
    ('Husky', 'Husky'),
    ('Italian Greyhound', 'Italian Greyhound'),
    ('Jack Russell Terrier', 'Jack Russell Terrier'),
    ('Labrador Retriever', 'Labrador Retriever'),
    ('Maltese', 'Maltese'),
    ('Mastiff', 'Mastiff'),
    ('Papillon', 'Papillon'),
    ('Pit Bull Terrier', 'Pit Bull Terrier'),
    ('Pomeranian', 'Pomeranian'),
    ('Poodle', 'Poodle'),
    ('Pug', 'Pug'),
    ('Rottweiler', 'Rottweiler'),
    ('Schnauzer ', 'Schnauzer '),
    ('Sheltie', 'Sheltie'),
    ('Shih Tzu', 'Shih Tzu'),
    ('Weimaraner', 'Weimaraner'),
    ('Yorkie', 'Yorkie'),
)

CITY_CHOICES = (
    ('Kanpur', 'Kanpur'),
    ('Visakhapatnam', 'Visakhapatnam'),
    ('Surat', 'Surat'),
    ('Chennai', 'Chennai'),
    ('Hyderabad', 'Hyderabad'),
    ('Pune', 'Pune'),
    ('Bangalore', 'Bangalore'),
    ('Kolkata', 'Kolkata'),
    ('Mumbai', 'Mumbai'),
    ('Delhi', 'Delhi'),
)

COLOR_CHOICES = (
    ('Black', 'Black'),
    ('Brindle', 'Brindle'),
    ('Brown/Chocolate', 'Brown/Chocolate'),
    ('Gray/Blue/Silver/Salt & Pepper', 'Gray/Blue/Silver/Salt & Pepper'),
    ('Merle', 'Merle'),
    ('Red/Golden/Orange/Chestnut', 'Red/Golden/Orange/Chestnut'),
    ('Silver & Tan (Yorkie colors)', 'Silver & Tan (Yorkie colors)'),
    ('Tan/Yellow/Fawn', 'Tan/Yellow/Fawn'),
    ('Tricolor (Tan/Brown & Black & White', 'Tricolor (Tan/Brown & Black & White'),
    ('White', 'White'),
)


class CustomUser(AbstractUser):
    # add additional fields in here
    name = models.CharField(max_length=150)
    picture = models.FileField(null=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50, choices=CITY_CHOICES)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{10,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.name


class Pet(models.Model):
    photo = models.FileField(null=True)
    name = models.CharField(max_length=50)
    uid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    breed = models.CharField(max_length=50, choices=BREED_CHOICES)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    age = models.PositiveIntegerField(default=0)
    color = models.CharField(max_length=50, choices=COLOR_CHOICES)
    needs = models.BooleanField(default=False)
    bonded = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dashboard')
