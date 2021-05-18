from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div
from crispy_forms.bootstrap import FieldWithButtons, StrictButton


class MemberForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                FieldWithButtons('email', StrictButton('Join', css_class='btn-success', type='submit')),
            )
        )
        super(MemberForm, self).__init__(*args, **kwargs)


    class Meta:
        model = User
        fields = ('email',)
        
    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email)
        if user:
            raise forms.ValidationError('User with email address already exists.')
        return email
