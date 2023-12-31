from django.db import models
from datetime import datetime
from django.contrib.auth.hashers import make_password, check_password


class Modele(models.Model):
    age_minimum= models.IntegerField()
    airbag =  models.CharField(max_length=50)
    capacitie = models.FloatField()
    attach_cat = models.CharField(max_length=40)
    clim = models.BooleanField()
    denomination = models.IntegerField()
    marque = models.CharField(max_length=40)
    nb_passag = models.IntegerField()
    nb_perms = models.IntegerField()
    type = models.CharField(max_length=50)
    version= models.IntegerField()
    cat = models.CharField(max_length=60)
    def __str__(self):
        return f"{self.version}"

class Agence(models.Model):
    description =  models.CharField(max_length=50)
    prove = models.CharField(max_length=500)
    slug = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.description}"

class Voiture(models.Model):
    matricule = models.CharField(max_length=50)
    modele = models.ForeignKey(Modele,on_delete=models.CASCADE)
    Agence = models.ForeignKey(Agence,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.matricule}"
class Client(models.Model):
    nom = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    car = models.ManyToManyField(Voiture,through='Reservation')
class Reservation(models.Model):
    voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    dateStart = models.DateTimeField(default=datetime.now, blank=True)
    dateEnd = models.DateTimeField(default=datetime.now, blank=True)
    tarif = models.CharField(max_length=50)
    statusPayment = models.BooleanField(default=False)





class Voiture1(models.Model):
    Nom = models.CharField(max_length=50)
    Description = models.CharField(max_length=1000)
    Daily_rate = models.IntegerField(default=0)
    Bdy = models.CharField(max_length=50)
    Siege = models.IntegerField(null=True)
    Porte = models.IntegerField(null=True)
    Bagage = models.IntegerField(null=True)
    Carburants = models.CharField(max_length=50)
    Moteur = models.IntegerField(null=True)
    Anne = models.IntegerField(null=True)
    Kilometrage = models.IntegerField(null=True)
    transmission = models.CharField(max_length=50)
    dure  = models.CharField(max_length=50)
    Fueleco = models.FloatField(null=True)
    color_exterieur=models.CharField(max_length=50)
    color_inter = models.CharField(max_length=50)
    BL = models.BooleanField(default=False,null=True)
    MP = models.BooleanField(default=False,null=True)
    CL = models.BooleanField(default=False,null=True)
    Sunroof = models.BooleanField(default=False,null=True)
    photo1 = models.ImageField()
    photo2 = models.ImageField()
    photo3 = models.ImageField()
    photo4 = models.ImageField()

    def __str__(self):
        return f"{self.Nom}"

class Client1(models.Model):
    Username = models.CharField(max_length=50)
    email = models.EmailField(unique=True,null=True)
    Pswd = models.CharField(max_length=255)
    Phone = models.IntegerField(null=True)
    Language = models.CharField(max_length=50,null=True)
    HourFormat = models.CharField(max_length=40,null=True)

    def save(self, *args, **kwargs):
        self.Pswd = make_password(self.Pswd)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.Pswd)
    def __str__(self):
        return f"{self.email}"

class Reservation1(models.Model):
    voiture = models.ForeignKey(Voiture1,on_delete=models.CASCADE,null=True)
    client = models.ForeignKey(Client1, on_delete=models.CASCADE)
    lieu_A = models.CharField(max_length=60)
    lieu_B = models.CharField(max_length=60)
    dateA = models.DateTimeField(default=datetime.now, blank=True)
    dateB = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f"Reservation {self.pk}: {self.client} - {self.lieu_A} to {self.lieu_B}"






