from django.shortcuts import render
from django.http import  HttpResponseNotFound
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.




def main(request):
    context = {
        "name": "Александр",
        "email": "gonimani@mail.ru"

    }
    
    
    return render(request, "index.html", context)



def about(request):
    author = {
        'name' : 'Иван',
        'middle_name' : 'Петрович',
        'last_name' : 'Иванов',
        'phone' : '123456',
        'email' : 'vasa@mail.ru',
    }
    context = {
        'author': author
    }
    return render(request, "about.html", context)    


def get_item(request, item_id: int):
    try:
        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        return render(request, (f'Item with id={item_id} not found'))
    else:
        context = {
            "item": item
        }
        return render(request, "item_page.html", context)
  



def get_items(request):
    context = {
        "items": Item.objects.all()
        }  
    return render(request, "items_list.html", context) 


