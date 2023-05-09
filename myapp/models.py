from django.db import models


class Contactus(models.Model):
    name= models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    subject= models.CharField(max_length=50)
    message= models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    

class Registration(models.Model):
    IMAGE = models.ImageField(upload_to='static/image/registration_images/')
    FULL_NAME = models.CharField(max_length=100)
    EMAIL = models.EmailField()
    PHONE_NUMBER = models.CharField(max_length=15)
    CITY = models.CharField(max_length=50)
    STATE_CHOICES = (
        ('Andaman and Nicobar', 'Andaman and Nicobar'),
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chandigarh', 'Chandigarh'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'),
        ('Daman and Diu', 'Daman and Diu'),
        ('Delhi', 'Delhi'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jammu and Kashmir', 'Jammu and Kashmir'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Ladakh', 'Ladakh'),
        ('Lakshadweep', 'Lakshadweep'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Puducherry', 'Puducherry'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal'),
    )
    STATE = models.CharField(max_length=30, choices=STATE_CHOICES)
    TRADE_CHOICES = (
        ('Electrician', 'Electrician'),
        ('Plumber', 'Plumber'),
    )
    TRADE = models.CharField(max_length=20, choices=TRADE_CHOICES)

    def __str__(self):
        return self.FULL_NAME
