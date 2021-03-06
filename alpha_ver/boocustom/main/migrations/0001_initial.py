# Generated by Django 4.0.4 on 2022-06-03 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=10, null=True, verbose_name='닉네임')),
                ('country', models.CharField(choices=[('인도', '인도'), ('인도네시아', '인도네시아'), ('일본', '일본'), ('스페인', '스페인'), ('브라질', '브라질'), ('중국', '중국')], max_length=10, null=True, verbose_name='나라')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('greetings', models.CharField(max_length=40, null=True, verbose_name='인삿말')),
            ],
            options={
                'verbose_name': 'Boo Post',
                'verbose_name_plural': 'Boo Post',
                'db_table': 'Boo Post',
            },
        ),
    ]
