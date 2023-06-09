# Generated by Django 4.1.7 on 2023-03-26 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dentist_Assistant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('S', 'Single'), ('M', 'Married')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='progress',
            field=models.CharField(blank=True, choices=[('B', 'Beginning'), ('I', 'In Progress'), ('C', 'Completed')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='work',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
