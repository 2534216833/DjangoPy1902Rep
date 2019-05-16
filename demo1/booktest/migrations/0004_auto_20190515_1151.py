# Generated by Django 2.2.1 on 2019-05-15 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0003_auto_20190515_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroinfo',
            name='gender',
            field=models.CharField(choices=[('man', '男'), ('woman', '女')], max_length=10),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='skill',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='绝招'),
        ),
    ]
