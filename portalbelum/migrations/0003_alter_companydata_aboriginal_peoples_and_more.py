# Generated by Django 4.0.5 on 2023-01-20 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalbelum', '0002_alter_companydata_gender_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydata',
            name='aboriginal_peoples',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='companydata',
            name='company_size',
            field=models.CharField(choices=[('small', 'small'), ('medium', 'medium'), ('large', 'large')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='companydata',
            name='person_with_disabilities',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='companydata',
            name='visible_minorities',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='companyname',
            name='name',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
