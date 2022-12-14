# Generated by Django 4.1.3 on 2022-12-07 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
        ('about', '0002_profileeducation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileCertification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_update', models.DateTimeField(auto_now=True, null=True)),
                ('institution', models.CharField(blank=True, max_length=256, null=True)),
                ('course', models.CharField(blank=True, max_length=256, null=True)),
                ('year', models.DateField(blank=True, null=True)),
                ('resume', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certification', to='perfil.profile')),
            ],
            options={
                'verbose_name': 'Certification',
                'verbose_name_plural': 'Certifications',
            },
        ),
    ]
