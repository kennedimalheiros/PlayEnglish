from django.shortcuts import render, redirect


def home(request):
    if request.user.is_authenticated():
        return render(request, 'index.html', {})
    else:
        return redirect('url_login')


def home_barra(request):
    return redirect('game_home')
