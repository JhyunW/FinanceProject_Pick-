# Generated by Django 4.2.4 on 2023-11-20 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.IntegerField()),
                ('cur_unit', models.TextField()),
                ('ttb', models.TextField()),
                ('tts', models.TextField()),
                ('deal_bas_r', models.TextField()),
                ('bkpr', models.TextField()),
                ('yy_efee_r', models.TextField()),
                ('ten_dd_efee_r', models.TextField()),
                ('kftc_bkpr', models.TextField()),
                ('kftc_deal_bas_r', models.TextField()),
                ('cur_nm', models.TextField()),
                ('date_field', models.TextField()),
            ],
        ),
    ]