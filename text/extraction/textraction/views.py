# pdf_app/views.py
from django.shortcuts import render, redirect
from .forms import PDFFileForm

def upload_pdf(request):
    if request.method == 'POST':
        form = PDFFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_pdf')
    else:
        form = PDFFileForm()
    return render(request, 'textraction/upload_pdf.html', {'form': form})
