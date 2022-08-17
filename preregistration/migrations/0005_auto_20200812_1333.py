# Generated by Django 3.1 on 2020-08-12 10:33

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('preregistration', '0004_auto_20200811_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='disposable_parents',
            name='related',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='preregistration.disposable'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 12, 10, 33, 5, 861800, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='disposable_transportation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('pickup_date', models.DateField()),
                ('related', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='preregistration.disposable')),
            ],
        ),
    ]
