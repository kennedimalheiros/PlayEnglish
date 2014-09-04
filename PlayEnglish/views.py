from django.shortcuts import redirect


def home(request):
    if request.user.is_authenticated():
        return redirect('game_home')
    else:
        return redirect('url_login')


def home_barra(request):
    return redirect('game_home')
