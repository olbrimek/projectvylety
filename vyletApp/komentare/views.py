from django.shortcuts import render

def komentare_index(request):
    return render(request, 'komentare/index.html')

