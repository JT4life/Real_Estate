from django.contrib.auth.models import User
from django.utils import timezone

from django.db import models

# Create your models here.
class agent(models.Model):
    name=models.CharField(max_length=20,db_index=True,unique=True)
    image=models.ImageField(upload_to='static/agent',blank=True)
    email=models.EmailField(blank=False)
    phone=models.CharField(max_length=10)
    office_address=models.CharField(max_length=50,default='my',blank=True)
    nick_name=models.CharField(max_length=25)
    def __str__(self):
        return self.name


class properties(models.Model):
    TYPE_CHOICES=(
        ('house',"HOUSE"),
        ('apartments','Apartments')
    )
    STATE_CHOICES= (('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'))
    BED_CHOICES=(
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
    )
    BATH_CHOICES=(
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    PURPOSE_CHOICES=(
        ('rent','Rent'),
        ('sale','Sale')
    )
   # id=models.AutoField(unique=True)
    agent_name=models.ForeignKey(agent,on_delete=models.CASCADE,related_name='property',default='Tess')
    type=models.CharField(max_length=20,choices=TYPE_CHOICES,default='house')
    purpose=models.CharField(max_length=20 ,choices=PURPOSE_CHOICES,default='rent')
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=30,choices=STATE_CHOICES,default='AL')
    zipCode=models.CharField(max_length=5)
    bed=models.IntegerField(choices=BED_CHOICES,default=1)
    bath=models.IntegerField(choices=BATH_CHOICES,default=1)
    area=models.IntegerField()
    price=models.IntegerField()
    details=models.CharField(max_length=50)
    images=models.ImageField(upload_to='static/images',blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.id)+'  '+self.address



class user_request(models.Model):
    agent_name = models.ForeignKey(agent, on_delete=models.CASCADE, related_name='user_request',default=1)
    property_id = models.ForeignKey(properties, on_delete=models.CASCADE, related_name='requested', default=1)

    full_name=models.CharField(max_length=20)
    email=models.EmailField(blank=False)
    message=models.TextField()
    def __str__(self):
        return self.full_name

class saved(models.Model):
    user_name=models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_name')
    property_id = models.ForeignKey(properties, on_delete=models.CASCADE, related_name='saved', default=1)

