from django.db import models

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name + " " + str(self.id)


class Manager(models.Model):
    name = models.CharField(max_length=255)
    group = models.OneToOneField(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + str(self.id)


class Employee(models.Model):
    name = models.CharField(max_length=255)
    group = models.ForeignKey(Group, null=True, blank=True, on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, max_length=255, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + str(self.id)



