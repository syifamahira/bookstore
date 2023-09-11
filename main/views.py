from django.shortcuts import render

# Create your views here.
def show_main(request):
    books = [
        {
            'title': 'Book of Journeys of Princess Syifa',
            'author': 'Syifa',
            'genre': 'Adventure',
            'price': 100000,
            'amount': 10,
            'synopsis': 'This is a story about a princess named Syifa who likes to travel around the world.',
        },
        {
            'title': 'Kayza and Azmy: a Love Story',
            'author': 'Syifa',
            'genre': 'Romance',
            'price': 20000,
            'amount': 20,
            'synopsis': 'A book about a love story between Kayza and Azmy. They are a couple who have been together for 5 years.',
        },
        {
            'title': 'Anisha Fashion Frenzy',
            'author': 'Syifa',
            'genre': 'Fashion',
            'price': 30000,
            'amount': 30,
            'synopsis': 'A book about fashion by Anisha. This book is suitable for those of you who like fashion.',
        },
        {
            'title': 'Healthy Productivity: by Shafira',
            'author': 'Syifa',
            'genre': 'Productivity',
            'price': 40000,
            'amount': 40,
            'synopsis': 'A book about productivity by Shafira. This book is suitable for those of you who want to be productive.',
        },
        {
            'title': 'Farah Squishy Castle',
            'author': 'Syifa',
            'genre': 'Children',
            'price': 50000,
            'amount': 50,
            'synopsis': 'This book tells the story of Farah and her castle that made of squishies',
        }
    ]

    context = {
        'books': books,
    }
    
    return render(request, 'main.html', context)
