from magasin.models import Produit
listProduit = [
    {
        'libelle' : 'Table',
        'description' : 'Table ronde diamétre 85 cm',
        'prix' : 65.000,
        'Type' : 'em'
    } ,
       {
        'libelle' : 'Couette',
        'description' : '220x220 double face',
        'prix' : 98.000,
        'Type' : 'em'
    },
          {
        'libelle' : 'Tomate',
        'description' : 'TBoite 800gr',
        'prix' : 3.500,
        'Type' : 'cs'
    },
             {
        'libelle' : 'Pomme',
        'description' : 'Pomme rouge sbiba',
        'prix' : 4.5000,
        'Type' : 'fr'
    }
]
try:
    Produit.objects.bulk_create([Produit(**{'libelle' : prod['libelle'],
                                        'description' : prod['description'],
                                        'prix' : prod['prix'],
                                        'Type' : prod['Type']})
                              for prod in listProduit])
    print(Produit.objects.filter(prix__gt=50.000))
    p = Produit.objects.get(id = 1)
    p.prix = 69.500
    p.save(update_fields=['prix'])
    p2 = Produit.objects.get(libelle = 'Pomme')
    p2.delete()
except Exception:
    print('error')
    print('hi')
