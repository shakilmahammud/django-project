from django import forms
from first_app.models import Ablum,Ami,Tumi,Musician

class Userform(forms.Form):
    user_mail  = forms.EmailField()
    user_email = forms.EmailField()
    user_name = forms.CharField()
    dob= forms.DateField()
    
    def clean(self):
        cleaned_data = super().clean()
        user_mail = cleaned_data["user_mail"]
        user_email = cleaned_data["user_email"]

        if user_mail != user_email:
            # Only do something if both fields are valid so far.
            raise forms.ValidationError(
                    "Filed not match"
                )