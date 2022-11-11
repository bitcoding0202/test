from django import forms  
from app.models import Input  


class InputForm(forms.ModelForm):  
    class Meta:  
        model = Input  
        fields = "__all__"  
