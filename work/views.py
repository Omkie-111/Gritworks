from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def doc_upload(request):
    if request.method == "POST" and request.FILES["document"]:
        document = request.FILES["document"]
        fs = FileSystemStorage()
        doc_file = fs.save(document.name, document)
        doc_file_url = fs.url(doc_file)
        return render(request, 'upload.html', {'document_url' : doc_file_url})
    return render(request, 'upload.html')

