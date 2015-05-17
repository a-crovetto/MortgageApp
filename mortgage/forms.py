from django import forms

class EmailForm(forms.Form):
    principal = forms.DecimalField()
    interest = forms.DecimalField()
