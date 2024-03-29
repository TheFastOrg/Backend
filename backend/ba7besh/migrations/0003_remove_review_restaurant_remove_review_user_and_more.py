# Generated by Django 4.1.5 on 2023-07-08 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ba7besh', '0002_remove_business_restaurant_remove_business_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='restaurant',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='reviewlike',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='reviewlike',
            name='review',
        ),
        migrations.RemoveField(
            model_name='reviewlike',
            name='user',
        ),
        migrations.DeleteModel(
            name='BusinessInfo',
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='ReviewLike',
        ),
    ]
