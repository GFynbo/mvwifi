from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(label='Your email *', widget=forms.TextInput(attrs={'placeholder':'john@doe.com'}), required=True)
    full_name = forms.CharField(label='Your full name *', widget=forms.TextInput(attrs={'placeholder':'John Doe'}), required=True)
    install_addr = forms.CharField(label='Install address', widget=forms.TextInput(attrs={'placeholder':'123 Apple St, Edgartown, MA 02539'}), required=False)
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
                                help_text = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."), required=False)
    street_addr = forms.CharField(label='Street address', widget=forms.TextInput(attrs={'placeholder':'123 Orange St'}), required=False)
    city = forms.CharField(label='City', widget=forms.TextInput(attrs={'placeholder':'Edgartown'}), required=False)
    state = forms.CharField(label='State', widget=forms.TextInput(attrs={'placeholder':'MA'}),max_length=2, required=False)
    zip = forms.DecimalField(label='Zip code (postal)', widget=forms.TextInput(attrs={'placeholder':'02539'}), max_digits=5, required=False)
    contact_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
                                help_text = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."), required=False)

    message = forms.CharField(label='Your message *', widget=forms.Textarea(attrs={'placeholder':'Hello...'}), required=True)
