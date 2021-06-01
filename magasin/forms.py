from django.forms import ModelForm
from .models import *

class ProduitForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProduitForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Produit
        fields = "__all__"
        
class CommandeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommandeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Commander
        fields = '__all__'

class ForniForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ForniForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Fournisseur
        fields = '__all__'