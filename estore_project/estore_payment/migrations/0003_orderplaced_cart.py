# Generated by Django 4.2.2 on 2023-09-01 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estore_payment', '0002_alter_orderplaced_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderplaced',
            name='cart',
            field=models.CharField(default='empty', max_length=100),
        ),
    ]
