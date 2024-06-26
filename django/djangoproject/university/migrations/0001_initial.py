# Generated by Django 4.2.11 on 2024-04-11 19:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GradProgram',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.TextField(max_length=100, null=True)),
                ('exp_grad_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Requirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requirement', models.TextField(max_length=100)),
                ('grad_prog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.gradprogram')),
            ],
        ),
        migrations.AddField(
            model_name='gradprogram',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.university'),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('app_no', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('grad_prog_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.gradprogram')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.student')),
            ],
        ),
        migrations.CreateModel(
            name='Minor',
            fields=[
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='university.student')),
                ('subject', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='university.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='university.student')),
                ('subject', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='university.subject')),
            ],
        ),
    ]
