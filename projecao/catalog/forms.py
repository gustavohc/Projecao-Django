from django import forms
from django.core import validators
from catalog.models import House

class AddHouseForm(forms.ModelForm):
     class Meta:
          db_table = 'House'
          managed = True
          verbose_name = 'House'
          model = House
          fields = '__all__'

     # name = forms.CharField()
     # email = forms.EmailField()
     # verify_email = forms.EmailField(label='Enter your email again')
     # text = forms.CharField(widget=forms.Textarea)

     # validate email in forms
     # def clean(self):
     #      all_clean_data = super().clean()
     #      email = all_clean_data['email']
     #      vmail = all_clean_data['verify_email']

     #      if email != vmail:
     #           raise forms.ValidationError("Make sure emails match!")
     # botcacher = forms.CharField(required=False, 
     #                               widget=forms.HiddenInput,
     #                               validators=[validators.MaxLengthValidator(0)])

     # def clean_botcacher(self):
     #      botcacher = self.cleaned_data['botcacher']
     #      if len(botcacher) > 0:
     #           raise forms.ValidationError("GOTCHA BOT!")
     #      return botcacher