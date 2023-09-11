from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'title' : 'Buku',
        'author': 'Syifa',
        'genre' : 'Fiksi',
        'price' : 100000,
        'amount' : 10,
        'synopsis' : 'Buku ini menceritakan tentang seorang anak yang bernama Syifa yang sangat cantik dan baik hati'

    }

    return render(request, 'main.html', context)