
import uuid
from django.db import models

# Create your models here.

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.TextField(max_length=100, null=True)
    exp_grad_date = models.DateField()

    def __str__(self):
        return "<Student id={} name={}>".format(
            self.id, self.name
        )

class University(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=100)

    def __str__(self):
        return "<University id={} name={}>".format(
            self.id, self.name
        )


class GradProgram(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    university = models.ForeignKey(University, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return "<GradProgram id={} name={} degree={}>".format(
            self.id, self.name, self.degree
        )

class Application(models.Model):
    app_no = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, null=False, on_delete=models.CASCADE)
    grad_prog_id = models.ForeignKey(GradProgram, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return "<Application app_no={} student={} grad_prog_id={}>".format(
            self.app_no, self.student, self.grad_prog_id
        )

class Subject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return "<Subject id={} name={}>".format(
            self.id, self.name
        )

class Major(models.Model):
    student = models.OneToOneField(Student, primary_key=True, on_delete=models.CASCADE)
    subject = models.OneToOneField(Subject, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return "<Major student={} subject={}>".format(
            self.student, self.subject
        )

class Minor(models.Model):
    student = models.OneToOneField(Student, primary_key=True, on_delete=models.CASCADE)
    subject = models.OneToOneField(Subject, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return "<Minor student={} subject={}>".format(
            self.student, self.subject
        )

class Requirements(models.Model):
    grad_prog = models.ForeignKey(GradProgram, null=False, on_delete=models.CASCADE)
    requirement = models.TextField(max_length=100)

    def __str__(self):
        return "<Requirements grad_prog={} requirement={}>".format(
            self.grad_prog, self.requirement
        )