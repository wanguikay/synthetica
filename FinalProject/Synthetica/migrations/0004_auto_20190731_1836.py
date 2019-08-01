# Generated by Django 2.2.3 on 2019-07-31 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Synthetica', '0003_auto_20190730_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generate',
            name='data_type',
            field=models.CharField(choices=[('sex', 'Gender'), ('age', 'Age'), ('address', 'Address'), ('pstatus', 'Parents Cohabitation'), ('medu', 'Mothers Education'), ('mjob', 'Mothers Job'), ('fedu', 'Fathers Education'), ('fjob', 'Fathers Job'), ('guardian', 'Guardian'), ('famsize', 'Family Size'), ('famrel', 'Family Relationships'), ('reason', 'Reason'), ('traveltime', 'Travel Time'), ('studytime', 'Study Time'), ('failures', 'Failures'), ('schoolsup', 'School Support'), ('famsup', 'Family Support'), ('activities', 'Extra-Curricular'), ('paidclass', 'Paid Classes'), ('internet', 'Internet Access'), ('freetime', 'Free Time'), ('walc', 'Weekend Alcohol'), ('dalc', 'Workday Alcohol'), ('health', 'Health'), ('absences', 'Absences'), ('mean', 'Mean')], default='sex', max_length=10, verbose_name='Data Type'),
        ),
    ]