from django import forms
from app1.models import students

class studentforms(forms.ModelForm):
    class Meta:
        model = students #students is a veriable from models.py table name
        fields = '__all__'