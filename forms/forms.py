from django.forms.fields import CharField, ChoiceField
from .models import Customer, Document
from django.forms import Form, ModelForm, ModelMultipleChoiceField, widgets
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# avaliable fields are
# comp_name, street1, street2, city, state, post_code, country, phone_number
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        exclude = ("entry_date", "last_modified", "email_hash")

class LoginForm(ModelForm):
    """Simple login form"""
    class Meta:
        model = User
        fields = ("username", "password")


class GenerateDocumentForm(Form):
    document = ModelMultipleChoiceField(queryset=Document.objects.all())
    customer = ModelMultipleChoiceField(queryset=Customer.objects.all())

    def clean_document(self):
        data = self.cleaned_data["document"]
        if len(data) > 1:
            raise ValidationError("Can only procress one document at a time.")
        return data


class DocumentForm(ModelForm):
    class Meta:
        model = Document
        exclude = ("last_modified",)


ACTIONS = (("Update", "1"), ("Delete", "2"))


class CustomerIdForm(Form):
    email_address = CharField(max_length=254)
    action = ChoiceField(choices=ACTIONS)

    def clean(self):
        cd = self.cleaned_data
        pk = cd.get("email_address")
        action = cd.get("action")
        if not Customer.objects.filter(email_address=pk):  # nothing found
            raise ValidationError("Email address matches no customer record")
        else:
            return cd
