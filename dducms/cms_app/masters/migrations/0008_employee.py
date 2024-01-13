# Generated by Django 4.2.7 on 2023-12-15 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0007_alter_prodcuctcategory_catid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ename', models.CharField(max_length=200)),
                ('gender', models.IntegerField()),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=100)),
                ('datejoing', models.DateField()),
                ('Eimage', models.ImageField(upload_to='employees')),
                ('salary', models.IntegerField()),
                ('salaryday', models.CharField(max_length=100)),
                ('desid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masters.designation')),
                ('qualid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masters.qualification')),
            ],
        ),
    ]
