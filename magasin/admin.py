from django.contrib import admin
from .models import Produit,Emballage,Fournisseur,ProduitNC,Commander
# Register your models here.
admin.site.register(Produit),
admin.site.register(Emballage),
admin.site.register(Fournisseur),
admin.site.register(ProduitNC),
admin.site.register(Commander)

#root root12345