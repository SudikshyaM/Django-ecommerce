# Generated by Django 5.1.1 on 2024-09-11 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_cerificate_chaireview_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.FileField(null=True, upload_to='static/uploads'),
        ),
    ]
