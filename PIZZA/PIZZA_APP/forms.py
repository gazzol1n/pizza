from django import forms

class ExcelUploadForm(forms.Form):
    file = forms.FileField()
    model_choice = forms.ChoiceField(choices=[
        ('category', 'Category'),
        ('dish', 'Dish'),
    ])
