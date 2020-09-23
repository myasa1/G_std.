# Generated by Django 3.1.1 on 2020-09-23 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StdImage', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('StdID', models.DecimalField(decimal_places=2, max_digits=5)),
                ('DateOfBirth', models.DateField()),
                ('currentAge', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Gender', models.CharField(max_length=50)),
                ('contry', models.CharField(max_length=50)),
                ('cityStreet', models.CharField(max_length=50)),
                ('PastalCode', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Eimal', models.CharField(max_length=50)),
                ('PhonNum', models.DecimalField(decimal_places=2, max_digits=5)),
                ('SecondaryRate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('MotherTongue', models.CharField(max_length=50)),
                ('PaymentMethod', models.CharField(max_length=50)),
                ('JoinDate', models.DateTimeField()),
                ('Massge', models.TextField(max_length=1000)),
            ],
        ),
    ]