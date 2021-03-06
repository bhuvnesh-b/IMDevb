# Generated by Django 3.2.1 on 2021-05-21 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_post_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='brief',
            new_name='Brief',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='Image',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='link',
            new_name='Link',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='Name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='Content',
            field=models.TextField(default='About the project'),
        ),
    ]
