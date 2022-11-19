from django.db import models
from datetime import date

class Users(models.Model):

    username = models.TextField(max_length=20, primary_key= True)
    password = models.TextField(max_length=20)
    e_mail = models.EmailField()
    begin_date = models.DateTimeField()

class Commentary(models.Model):

    commentarist = models.TextField(max_length=20)
    text_commentary = models.TextField(max_length= 400)
    date_commentary = models.DateTimeField()

class Post(models.Model):

    TRAVEL,AR,CL = 'TR','AR','CL'
    CUYO, PATAGONIA, COSTA, BUENOS_AIRES, CENTRO = 'CY','PAT','MDP','BSAS','COB'
    PARQUES, LAGOS, RUTAS, MONTANIAS = 'PN','LG','RN','MNT'
    IDEAS, RATA_TIPS = 'ID','TIP'

    TAGS_CHOICES = [(TRAVEL, 'Travel'),
                    (AR, 'Argentina'), (CL, 'Chile'),
                    (CUYO, 'Cuyo'), (PATAGONIA, 'Patagonia'), (COSTA, 'Costa Atlántica'),
                    (BUENOS_AIRES, 'Buenos Aires'), (CENTRO, 'Centro'),
                    (PARQUES, 'Parques'), (LAGOS, 'Lagos'), (RUTAS, 'Rutas'), (MONTANIAS, 'Montañas'),
                    (IDEAS, 'Ideas'), (RATA_TIPS, 'Rata-tips')]

    tag1 = models.CharField(max_length=4, choices=TAGS_CHOICES)
    tag2 = models.CharField(max_length=4, choices=TAGS_CHOICES)
    url = models.CharField(max_length=50)
    title = models.TextField(max_length=50)
    subtitle = models.TextField(max_length=80)
    image = models.CharField(max_length=50)
    image_alt = models.CharField(max_length=50)
    image_title = models.CharField(max_length=50)
    readmore_avaliable = models.BooleanField()
    description = models.TextField(max_length=300)
    date = models.DateField(default=date.today())



