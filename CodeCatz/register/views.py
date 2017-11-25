from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from register.forms import UserProfileForm
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from register.forms import SignUpForm

def signup(request):
    ProfileInlineFormset = inlineformset_factory(User, UserProfile, fields=('phone', 'address'))
    if request.method == 'POST':
        form = SignUpForm(request.POST)   
        formset = ProfileInlineFormset(request.POST)
        if form.is_valid():
            created_user = form.save(commit=False)
            formset = ProfileInlineFormset(request.POST, instance=created_user)
            if formset.is_valid():
                created_user.save()
                #formset.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect(reverse('home'))
                
    else:
        formset = ProfileInlineFormset()
        form = SignUpForm()
    return render(request, 'register/signup.html', {
            "form": form,
            "formset": formset,
        })

@login_required
def view_user(request, pk):
    user = User.objects.get(pk=pk)
    if request.user.is_authenticated() and request.user.id == user.id:
        userProfile = UserProfile.objects.get(pk=pk)
        context = {'user': user, 'userProfile': userProfile}
        return render(request, 'register/view.html', context)
    else:
        raise PermissionDenied


@login_required
def edit_user(request, pk):
    user = User.objects.get(pk=pk)
    user_form = UserProfileForm(instance=user)

    ProfileInlineFormset = inlineformset_factory(User, UserProfile, fields=('phone', 'address'))
    formset = ProfileInlineFormset(instance=user)
    if request.user.is_authenticated() and request.user.id == user.id:
        if request.method == "POST":
            user_form = UserProfileForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)

                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return HttpResponseRedirect('home')

        return render(request, "register/account_update.html", {
            "noodle": pk,
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied

