from django import forms

TIPOS_CHOICES = (
    ('ver', 'Verduras'),
    ('fru', 'Frutas'),)
alimentos = (('', '----'),)
numero = 32
cadena = "hola mundo"
class tipoForm(forms.Form):
	tipo_alimento = forms.ChoiceField(
			choices=TIPOS_CHOICES,
			widget=forms.Select(
				attrs={'class':'tipo'}
			)	
				)
	alimento = forms.ChoiceField(
				choices=alimentos,
				widget=forms.Select(
				attrs={'class':'alimentos'}
				)
					)

