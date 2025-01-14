# Generated by Django 5.0.6 on 2024-07-20 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0009_delete_cartproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='image')),
                ('quantity', models.CharField(default=1, max_length=10)),
                ('subtotal', models.CharField(default=50, max_length=10)),
            ],
        ),
    ]
