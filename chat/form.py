from django import forms

class ContactForm(forms.Form):
  subject = forms.CharField(widget=forms.TextInput(attrs={'size':'48', 'class':'form-control'}))
  email_to = forms.EmailField(widget=forms.TextInput(attrs={'size':'48', 'class':'form-control'}))
  message = forms.CharField(widget=forms.Textarea(attrs={'cols':50, 'rows': 5 , 'class':'form-control'}))
