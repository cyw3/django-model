from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def form_elements(request):
    return render(request,'form-elements.html')

def validation_elements(request):
    return render(request,'validation-elements.html')

def form_wizard(request):
    return render(request,'form-wizard.html')
def ui_elements(request):
    return render(request,'ui-elements.html')
def typography(request):
    return render(request,'typography.html')
def tiles(request):
    return render(request,'tiles.html')
def buttons(request):
    return render(request,'buttons.html')
def grid(request):
    return render(request,'grid.html')
def tables(request):
    return render(request,'tables.html')

def login(request):
    return render(request,'login.html')

def page404(request):
    return render(request,'page404.html')

def tinymce(request):
    return render(request,'tinymce.html')

def markdown(request):
    return render(request, 'markdown.html')

def chart(request):
    return render(request, 'charts.html')