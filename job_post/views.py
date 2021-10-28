from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render
from django.views.generic import ListView, TemplateView

from .forms import CustomCreationForm, CustomUserCreationForm, ImageForm
from .models import *


def register(request):
    # We don't want logged-in users to access the registration page.
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('upwork:home')
    # Assign form data to user (else create a new form for new user)
    if request.method == 'POST':

        # Complete Registrations
        if request.POST['submit'] == 'Complete':
            form = CustomCreationForm(request.POST)

            # If valid, create a UserProfile with submitted information
            if form.is_valid():
                UserProfile.objects.create(
                        user_id=request.user.id,
                        first_name=form.cleaned_data['first_name'],
                        last_name=form.cleaned_data['last_name'],
                        email=request.user,
                        phone=form.cleaned_data['phone'],
                        city=form.cleaned_data['city'],
                        state=form.cleaned_data['state'],
                        zipcode=form.cleaned_data['zipcode'],
                        email_notification_active=form.cleaned_data['email_notification_active'],
                        date_of_birth="1993-06-14"
                )

                request.user.first_name = form.cleaned_data['first_name']
                request.user.last_name = form.cleaned_data['last_name']
                request.user.save()

            # redirect to the home page, change this to user profile?
            return redirect('upwork:home')

        form = CustomUserCreationForm(request.POST)

        # Assigns user as Recruiter
        if request.POST['submit'] == 'Recruiter':
            # Get logged in user object
            user = request.user

            # Assign user to Group 'Recruiters'
            group = Group.objects.get(name='recruiters')
            group.user_set.add(user)

            form = CustomCreationForm()

            context = {
                'form': form,
            }

            return render(request, 'registration/signup3.html', context=context)

        # Assigns user as Seeker
        if request.POST['submit'] == 'Seeker':
            # Get logged in user object
            user = request.user

            # Assign user to Group 'Seekers'
            group = Group.objects.get(name='seekers')
            group.user_set.add(user)

            form = CustomCreationForm()

            context = {
                'form': form,
            }

            return render(request, 'registration/signup3.html', context=context)

        # Register user (else redirect to /login)
        if form.is_valid():
            form.save()

            # TODO: This is probably really bad to do.
            # Authenticate and log user in
            user = authenticate(username=request.POST['username'], password=request.POST['password2'])
            login(request, user)

            # If the user can login, direct them to the next step of registration
            if user is not None:
                context = {
                    'form': form.cleaned_data,
                    'user': user
                }
                return render(request, 'registration/signup2.html', context=context)

        # We want this to redirect to the login screen if the user already exists
        else:
            return redirect('login')

    # create a new form
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form
    }

    return render(request, 'registration/signup.html', context)


def recruiter(request):
    print("made it to recruiter view")


class HomeView(TemplateView):
    template_name = 'job_post/home.html'


class SearchResultsView(ListView):
    # TODO: Replace this model with the Job_post model
    model = User
    template_name = 'job_post/search_results.html'

    # def get_queryset(self):
    #     return Customer.objects.filter(
    #             Q(name__icontains='B')
    #     )


def handle_uploaded_file(uploaded_file):
    with open('uploads', 'wb+') as destination:
        for chunk in uploaded_file.chunks():
            destination.write(chunk)


def user_profile(request):
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)

        if request.method == 'POST':
            form = ImageForm(request.POST, request.FILES)

            print(form)

            user = request.user

            if form.is_valid():
                form.save(commit=False)
                handle_uploaded_file(request.FILES['user_image'])
                request.user.profile.user_image = 'abc.jpg'

                return render(request, 'job_post/profile.html', context={
                    'form': ImageForm(),
                    'user': request.user,
                    'profile': profile
                })
            else:
                print(form.errors)

        else:
            form = ImageForm()

        return render(request, 'job_post/profile.html', context={
            'form': form,
            'user': request.user,
            'profile': profile
        })

    else:
        return redirect('login')


class ProfileView(TemplateView):
    model = UserProfile
    template_name = 'job_post/profile.html'

    # def get_user_profile(self):
    #     return get_object_or_404(User, username=self.kwargs.get('user'))
