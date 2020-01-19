from django import forms
from django.forms import ChoiceField
from django.core.exceptions import ValidationError

# class ChoiceNoValidation(ChoiceField):
#     def validate(self, value):
#         pass
#
#
# class ContactForm(forms.ModelForm):
#     choice = ChoiceNoValidation(label=u'Test')
#
#     def __init__(self):
#         XXXXXX
#         raise ValidationError(u'Fallo ')
#

#    class Meta:
#        model = Footer

class ContactForm(forms.Form):
    name = forms.CharField(max_length=20, required=True,
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'full-width',
                                   'id': 'id_name',
                                   'type': 'text',
                                   'name': 'name',
                                   'placeholder': 'Your Name'
                               }
                           ))
    email = forms.EmailField(required=True,
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'full-width',
                                   'id': 'id_email',
                                   'type': 'text',
                                   'name': 'email',
                                   'placeholder': 'Your Email'
                               }
                           ))

    website = forms.URLField(required=True,
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'full-width',
                                   'id': 'id_website',
                                   'type': 'text',
                                   'name': 'website',
                                   'placeholder': 'Your Website'
                               }
                           ))

    comment = forms.CharField(required=True,
                           widget=forms.Textarea(
                               attrs={
                                   'class': 'full-width',
                                   'id': 'id_comment',
                                   'name': 'comment',
                                   'placeholder': 'Your Comment'
                               }
                           ))

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(max_length=20, required=True,
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'full-width',
                                       'id': 'id_name',
                                       'type': 'text',
                                       'name': 'name',
                                       'placeholder': 'Your Name'
                                   }
                               ))
        self.fields['email'] = forms.EmailField(required=True,
                                 widget=forms.TextInput(
                                     attrs={
                                         'class': 'full-width',
                                         'id': 'id_email',
                                         'type': 'text',
                                         'name': 'email',
                                         'placeholder': 'Your Email'
                                     }
                                 ))

        self.fields['website'] = forms.URLField(required=True,
                                 widget=forms.TextInput(
                                     attrs={
                                         'class': 'full-width',
                                         'id': 'id_website',
                                         'type': 'text',
                                         'name': 'website',
                                         'placeholder': 'Your Website'
                                     }
                                 ))

        self.fields['comment'] = forms.CharField(required=True,
                                  widget=forms.Textarea(
                                      attrs={
                                          'class': 'full-width',
                                          'id': 'id_comment',
                                          'name': 'comment',
                                          'placeholder': 'Your Comment'
                                      }
                                  ))
