from django.db import models

# Create your models here.


class Mentor(models.Model):
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'mentors'

    def __str__(self):
        # Shows all record links
        return self.f_name + self.l_name


class Mentee(models.Model):
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'mentees'

    def __str__(self):
        # Shows all record links
        return self.f_name + self.l_name


class Topic(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Shows all record links
        return self.name


class Mentor_Topic(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.PROTECT)
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    years_of_experience = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
