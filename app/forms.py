from django import forms
def check_for_m(value):
    if value[0].lower()=='m':
        raise forms.ValidationError('Started with m ')
    
def check_for_len(value):
    if len(value)>5:
        raise forms.ValidationError('Length is Exceded')

class StudentForms(forms.Form):
    Sname=forms.CharField(max_length=100,validators=[check_for_len])
    Sage=forms.IntegerField()
    Sid=forms.IntegerField()
    Semail=forms.EmailField(validators=[check_for_m])