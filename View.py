def login_view(request):
    return render(request, 'core/login.html')

def signup(request):
    return render(request, 'core/signup.html')
