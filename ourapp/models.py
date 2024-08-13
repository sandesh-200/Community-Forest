from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator
#Following are models
class AllUser(models.Model):
    first_name = models.CharField(max_length=200,blank=False,null=False)
    middle_name = models.CharField(max_length=200,blank=True,null=True)
    last_name = models.CharField(max_length=200,blank=False,null=False)
    MUNICIPALITY_CHOICE = [('अर्जुनधारा','अर्जुनधारा'),
                           ('कन्काई','कन्काई')
                           ]
    WARD_CHOICE = [
    ('3', '3'), 
    ('4', '4'), 
    ('5', '5'), 
    ('7', '7'), 
    ('8', '8')
]

    TOLE_CHOICE = TOLE_CHOICE =[
    ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
    ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'),
    ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'),
    ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'),
    ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'),
    ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30')
]

    municipality = models.CharField(max_length=200,choices=MUNICIPALITY_CHOICE,blank=False,null=False)
    ward = models.CharField(max_length=50,choices=WARD_CHOICE,blank=False,null=False)
    tole = models.CharField(max_length=50,choices=TOLE_CHOICE,blank=False,null=False)
    member_number = models.IntegerField(
    validators=[
        MinValueValidator(1000),
        MaxValueValidator(9999)
    ],
    blank=False,
    null=False,
    primary_key=True
)
    phone = PhoneNumberField(default='+977')
    MEMBER_TYPE_OPTION = [('क वर्ग','क वर्ग'),
                          ('ख वर्ग','ख वर्ग')]
    member_type = models.CharField(max_length=50,choices=MEMBER_TYPE_OPTION,blank=False,null=False)
    approved_by = models.CharField(max_length=200,blank=False,null=False,default='')
    APPROVED_BY_CHOICES=[('अध्यक्ष','अध्यक्ष'),
    ('उपाध्यक्ष','उपाध्यक्ष')]
    approved_by_position = models.CharField(choices=APPROVED_BY_CHOICES,max_length=100,default='')
    date_approved = models.DateField(blank=False,null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} को खाता"
    
class Karyasamiti(models.Model):
    name = models.CharField(max_length=200,blank=False,null=False)
    image = models.ImageField(upload_to='karyasamiti_images')
    def __str__(self):
        return self.name
    
class SallakarSamiti(models.Model):
    name = models.CharField(max_length=200,blank=False,null=False)
    image = models.ImageField(upload_to='karyasamiti_images')
    def __str__(self):
        return self.name
    
class ChetriyaSamiti(models.Model):
    name = models.CharField(max_length=200,blank=False,null=False)
    image = models.ImageField(upload_to='chetriyasamiti_images')
    AREA_CHOICES = [(i, str(i)) for i in range(1, 6)]
    area = models.CharField(max_length=50,choices=AREA_CHOICES)
    def __str__(self):
        return self.name
    
class ToleSamiti(models.Model):
    name = models.CharField(max_length=200,blank=False,null=False)
    image = models.ImageField(upload_to='tolesamiti_images')
    TOLE_CHOICES = [(i, str(i)) for i in range(1, 31)]
    tole = models.CharField(max_length=50,choices=TOLE_CHOICES)
    def __str__(self):
        return self.name

class LekhaSamiti(models.Model):
    name = models.CharField(max_length=200,blank=False,null=False)
    image = models.ImageField(upload_to='lekhasamiti_images')
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=200,blank=False,null=False)
    phone = PhoneNumberField(default='+977')
    message = models.TextField(blank=False,null=False)

    def __str__(self):
        return f"Message from {self.name}"
    
class News(models.Model):
    title = models.CharField(max_length=500)
    news = models.FileField(upload_to='news')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Notice(models.Model):
    title = models.CharField(max_length=500)
    notice = models.FileField(upload_to='notice')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Report(models.Model):
    title = models.CharField(max_length=500)
    report = models.FileField(upload_to='report')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

    



    






