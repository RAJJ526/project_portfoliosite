# Generated by Django 5.1.3 on 2024-11-08 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('client_name', models.CharField(max_length=100)),
                ('areas_of_working', models.CharField(max_length=100)),
                ('work_date', models.CharField(max_length=100)),
                ('claim_id', models.CharField(max_length=100)),
                ('insurance', models.CharField(max_length=100)),
                ('patient', models.CharField(max_length=100)),
                ('service_data', models.CharField(max_length=100)),
                ('billed_amount', models.CharField(max_length=100)),
                ('balance', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('reason', models.CharField(max_length=100)),
                ('action', models.CharField(max_length=100)),
                ('payment_information', models.CharField(max_length=100)),
                ('patient_responsibility', models.CharField(max_length=100)),
                ('cheque_no', models.CharField(max_length=100)),
                ('cheque_date', models.CharField(max_length=100)),
                ('paid_status', models.CharField(max_length=100)),
                ('paid_by', models.CharField(max_length=100)),
                ('denial_code', models.CharField(max_length=100)),
                ('add_corrected', models.CharField(max_length=100)),
                ('dx_corrected', models.CharField(max_length=100)),
                ('cpt', models.CharField(max_length=100)),
                ('solutions', models.CharField(max_length=100)),
            ],
        ),
    ]
