from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import CreateView
from django.views.generic import View

from .. import models, forms


# Create new Customer
class CustomerCreate(CreateView):
    model = models.Customer
    form_class = forms.CustomerForm



class CustomerId(View):
    '''
    Identify customer via email_address
    redirect to update or delete page with customer information
    '''
    template_name = "forms/customer_id_form.html"
    form_class = forms.CustomerIdForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            email_address = request.POST["email_address"]
            customer = models.Customer.objects.get(email_address=email_address)
            customer_pk = customer.email_hash
            action = request.POST["action"]
            print(action)
            if action == "Update":
                return redirect("forms:cust-update", pk=customer_pk)
            elif action == "Delete":
                return redirect("forms:cust-del", pk=customer_pk)

        return render(request, self.template_name, {'form': form}) 


class UpdateCustomer(View):
    """
    Form to update customer information - email_address field cannot be changed
    """
    template_name = "forms/customer_form.html"
    form_class = forms.CustomerForm

    def get(self, request, pk:str, *args, **kwargs) -> HttpResponseRedirect:
        form = self.form_class
        instance = get_object_or_404(models.Customer, pk=pk)
        email_address = instance.email_address
        return render(request, self.template_name, {'form': form,'email_address':email_address})
    
    def post(self, request, *args, **kwargs):
        email_address = request.POST.get("email_address")
        instance = get_object_or_404(models.Customer, email_address=email_address)
        form = self.form_class(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect("forms:index")
        return render(request, self.template_name, {'form': form,'email_address':email_address})


class DeleteCustomer(View):
    # need to confirm that instance is deleted
    def get(self, request, pk:str, *args, **kwargs) -> HttpResponseRedirect:
        if instance:= models.Customer.objects.get(pk=pk):
            instance.delete()
            return redirect('forms:index')
        # return some kind of error
    