# Generated by Django 5.0.6 on 2024-05-13 23:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_printshop_alter_books_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='print_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publishers', to='users.printshop'),
        ),
    ]