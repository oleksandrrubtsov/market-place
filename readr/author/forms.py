from django.forms import ModelForm
from .models import Author

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['first_name','last_name','date_of_birth',]