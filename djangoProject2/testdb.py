from django.http import HttpResponse
from TestModel.models import Test

def add(response):
    test = Test(name="Nick")
    test.save()

    return HttpResponse('<p>Add success!</p>')

def del_(response):
    test = Test.objects.get(id=1)
    test.delete()
    return HttpResponse('<p>Del success!</p>')

def query(response):
    list = Test.objects.all()
    response = ' '
    for var in list:
        response += var.name + " "
    response1 = response
    print(response1)
    return HttpResponse('<p>' + response1 + '</p>')

def update(response):
    test = Test.objects.get(id=2)
    test.name = 'Mick'
    test.save()
    return HttpResponse('<p>Update success!</p>')
