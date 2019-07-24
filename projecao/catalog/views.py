from django.shortcuts import render
from django.http import HttpResponse
# from catalog import forms
from catalog.forms import AddHouseForm

# Create your views here.
def index(request):
    my_dic = {'insert': "This is a insertion!"}
    return render(request, 'catalog/index.html', context=my_dic)

def add_house(request):
    form = AddHouseForm()

    if request == 'POST':
        form = AddHouseForm(request.POST)

    if form.is_valid():
        form.save(commit=True)
        return index(request)
    else:
        print("Form invalid")


#     form = forms.AddHouseForm()

#     if request == 'POST':
#         form = forms.AddHouseForm(request.POST)

#         if form.is_valid():
#             form.save(commit=True)
#             return index(request)
#         else:
#             print("Form invalid")
        
    return render(request, 'catalog/add_house_form.html', {'form':form})