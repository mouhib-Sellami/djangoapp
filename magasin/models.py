from django.db import models
from datetime import date
# Create your models here.


class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.TextField()
    email = models.EmailField()
    telephone = models.CharField(max_length=8)

    def __str__(self):
        return "{} {} {} {} ".format(self.nom, self.adresse, self.email, self.telephone)


COUL_CHOICES = [('bl', 'blanc'), ('rg', 'rouge'),
                ('ble', 'bleur'), ('vr', 'vert'), ('muli', 'multicolore')]


class Emballage(models.Model):
    matiere = models.CharField(max_length=100)
    color = models.CharField(
        max_length=10, choices=COUL_CHOICES, default='Transparent')

    def __str__(self):
        return "{} {} ".format(self.matiere, self.color)


TYPE_CHOICES = [('em', 'emballe'), ('fr', 'frais'), ('cs', 'conserve')]


class Produit(models.Model):
    libelle = models.CharField(max_length=100)
    description = models.TextField(default='Non definie')
    prix = models.DecimalField(max_digits=10, decimal_places=3)
    Type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    img = models.ImageField(blank=True)
    emballag = models.OneToOneField(
        Emballage, on_delete=models.CASCADE, null=True)
    fournisseur = models.ForeignKey(
        Fournisseur, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "{}, {}, {}, {}".format(self.libelle, self.description, self.prix, self.Type)


class ProduitNC(Produit):
    duree_garantie = models.CharField(max_length=100)

    def __str__(self):
        return super().__str__() + " {} ".format(self.duree_garantie)


class Commander(models.Model):
    duree_garantie = models.CharField(max_length=100)
    dateCde = models.DateField(null=True, default=date.today())
    totalCde = models.DecimalField(max_digits=10, decimal_places=3)
    produits = models.ManyToManyField(Produit)

    def __str__(self):
        return "{} {} {} {} ".format(self.duree_garantie, self.dateCde, self.totalCde, self.produits)
