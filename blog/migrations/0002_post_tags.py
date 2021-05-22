# Generated by Django 3.2.1 on 2021-05-17 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='TAGS',
            field=models.CharField(choices=[('music', 'RELATED TO MUSIC'), ('game', 'RELATED TO GAMES'), ('s_media', 'RELATED TO SOCIAL MEDIA'), ('medical', 'RELATED TO MEDICAL'), ('e_commerce', 'RELATED TO E-COMMERCE'), ('na', 'N/A')], default='na', max_length=32),
        ),
    ]