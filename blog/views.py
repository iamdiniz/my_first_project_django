from django.shortcuts import render


# Create your views here.
def blog(request):
    print('blog')

    context = {
        'text': 'Olá blog',
        'title': 'Essa é uma pagina de exemplo - ',
    }

    return render(
        request,
        'blog/index.html',
        context
    )


def exemplo(request):
    print('exemplo')

    context = {
        'text': 'Olá exemplo'
    }

    return render(
        request,
        'blog/exemplo.html',
        context
    )