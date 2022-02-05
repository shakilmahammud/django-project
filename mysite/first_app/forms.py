from dataclasses import field
from django import forms
from first_app import models

class Userform(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = '__all__'
#     user_mail  = forms.EmailField()
#     user_email = forms.EmailField()
#     user_name = forms.CharField()
#     dob= forms.DateField()
#     user_mail  = forms.EmailField()
#     user_email = forms.EmailField()
#     user_name = forms.CharField()
#     dob= forms.DateField()
    
#     def clean(self):
#         cleaned_data = super().clean()
#         user_mail = cleaned_data["user_mail"]
#         user_email = cleaned_data["user_email"]

#         if user_mail != user_email:
#             # Only do something if both fields are valid so far.
#             raise forms.ValidationError(
#                     "Filed not match")