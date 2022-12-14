# Generated by Django 4.1 on 2022-09-13 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Main', '0003_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='feedback',
        ),
        migrations.AddField(
            model_name='feedback',
            name='feedback',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.product'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
