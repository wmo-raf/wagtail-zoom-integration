# Generated by Django 4.2.1 on 2023-05-24 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZoomSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_key', models.CharField(blank=True, help_text='API Key obtained from Zoom', max_length=256, null=True, verbose_name='Zoom API Key')),
                ('api_secret', models.CharField(blank=True, help_text='API Secret obtained from Zoom', max_length=256, null=True, verbose_name='Zoom API Secret')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]