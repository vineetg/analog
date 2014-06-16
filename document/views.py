from django.shortcuts import render

from document.models import Document

def index(request):
    latest_documents = Document.objects.all().order_by('-date_updated')[:5]
    context = {'latest_documents': latest_documents}
    return render(request, 'document/index.html', context)

def create(request):
    return render(request, 'document/index.html')
