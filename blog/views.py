from django.shortcuts import render

posts = [
    {
        'author': 'Админ',
        'title': 'Добро пожаловать в наш клуб!',
        'content': 'Обсуждаем программирование и IT-темы.',
        'date_posted': '6 декабря, 2024'
    },
    {
        'author': 'Модератор',
        'title': 'Новая встреча участников',
        'content': 'Узнайте, как присоединиться к нашей следующей встрече.',
        'date_posted': '4 декабря, 2024'
    }
]



def home(request):
    context = {
        'posts': posts
    }
    return render(request, './home.html', context)


def about(request):
    return render(request, './about.html', {'title': 'О клубе Python Bytes'})