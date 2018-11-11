from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import View, TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, ModelFormMixin, FormView, FormMixin, ContextMixin
from .models import User
from .forms import UserForm, LoginForm
from passlib.hash import pbkdf2_sha256 as e
from django.http import HttpResponseRedirect,HttpResponse

class HomeView(TemplateView):
    template_name = 'bookApp/home.html'


class SignupView(CreateView):
    form_class = UserForm
    template_name = 'bookApp/signup.html'
    success_url = reverse_lazy('Home')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.Password = e.encrypt(self.object.Password, rounds=12000, salt_size=32)
        self.object.save()
        return super().form_valid(form)


class LoginView(View, FormMixin):
    template_name = 'bookApp/login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        request = self.request
        form = self.get_form()
        password = request.POST['Password']
        fname = User.objects.filter(Email=request.POST['Email'])
        if fname:
            username = fname[0].First_name
            user_password = fname[0].Password
            if e.verify(password, user_password):
                return HttpResponseRedirect(reverse('user', kwargs={'id': username}))
            else:
                return render(request, self.template_name, {'form': form, 'incorrect_password': 'Incorrect Password'})
        else:
            return render(request, self.template_name, {'form': form, 'user_not_exist': 'User not exist'})


class UserView(View, ContextMixin):
    template_name = 'bookApp/user.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first_name'] = self.kwargs['id']
        return context


