from django.shortcuts import render

# Create your views here.
def test_load(request):
    return render(request,'test_load.html')

def test_load_server(request):
    return render(request,'test_load_server.html')