from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Yeni bir kullanıcı kaydet"""
    if request.method != 'POST':
        # Boş kayıt formu görüntüle.   
        form = UserCreationForm()
    else:
        # Tamamlanmış formu işle.
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            # Kullanıcıya oturum aç ve ana sayfaya yönlendir.
            login(request, new_user)
            return redirect('first_app:index')

    # Boş veya geçersiz bir form görüntüle.
    context = {'form': form}
    return render(request, 'registration/register.html', context)


