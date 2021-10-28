from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    #     # username from User model will be the email that is entered on the form. Essentially hiding the default username field and replacing it with email.
    #     # user_type_id = models.ForeignKey(UserType)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=10, blank=False)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    user_image = models.ImageField(null=True, upload_to='uploads')
    email_notification_active = models.BooleanField(default=False, blank=False)

    #     is_online = models.BooleanField(default=False, blank=False)
    #     updated_date = models.DateTimeField(auto_now_add=True)
    #
    # def updated(self):
    #     self.updated_date = timezone.now()
    #     self.save()

    def get_absolute_url(self):
        return reverse('profile-detail', args=[str(self.user.id)])

    def __str__(self):
        return \
            str(self.user)

    class Meta:
        ordering = ['last_name']


class UserExperience(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)


class ExperienceAccolades(models.Model):
    experience = models.ForeignKey(UserExperience, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)


class Education(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    school = models.CharField(max_length=50)
    degree_type = models.CharField(max_length=2)
    major = models.CharField(max_length=50)
    minor = models.CharField(max_length=50)


class EducationAccolades(models.Model):
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)


class Company(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)


class JobPost(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return \
            str(self.title)


class Applied(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    job = models.OneToOneField(JobPost, on_delete=models.CASCADE)

    def __str__(self):
        return \
            str(self.user)





# class CompanyProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     company_name = models.CharField(max_length=100, blank=False)
#     address = models.CharField(max_length=100, blank=False)
#     city = models.CharField(max_length=100, blank=False)
#     state = models.CharField(max_length=2, blank=False)
#     zipcode = models.CharField(max_length=10, blank=False)
#     website_url = models.CharField(max_length=100, blank=False)
#     description = models.TextField(max_length=2000)


# class CompanyImages(models.Model):
#     company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
#     path = models.ImageField(blank=False)
