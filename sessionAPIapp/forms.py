from django import forms 

class ItemForm(forms.Form):
    item = forms.CharField(max_length=30)
    quantity = forms.IntegerField(widget = forms.Select(choices=[(x,x) for x in range(1,11)]))
