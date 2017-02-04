from django import forms

from .models import Visitor

class VisitorForm(forms.ModelForm):

    class Meta:
        model = Visitor
        fields = ('first_name',
                  'last_name',
                  'call_sign',
                  'nfarl_member',
                  'contact_me',
                  'email',
                  'first_time',
                  'age',
                 )
