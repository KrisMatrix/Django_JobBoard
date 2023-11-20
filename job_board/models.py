from django.db import models

# Create your models here.
# model => python class
# model represents a table in the db

class JobPosting(models.Model):
    # by default we have an id file that starts at 1 and auto-increments
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.IntegerField()
    is_active = models.IntegerField(default=False)

    def __str__(self):
        # for changing django admin to be more readable.
        return f"{self.title} | {self.company} | Active: {self.is_active}"

  # makemigrations
  # -> creates instructions telling django how the db have changed.

  # migrate
  # -> Applies the above changes

#CRUD
# create
# read
# update
# delete

# model manager -> objects
# JobPosting.objects.all()
# JobPosting.objects.get(id=1)
# JobPosting.objects.filter(company='abc tech')