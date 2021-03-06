# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-28 17:03
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apostello', '0013_keyword_linked_groups'),
    ]

    operations = [
        migrations.CreateModel(
            name='QueuedSms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_to_send', models.DateTimeField()),
                ('sent', models.BooleanField(default=False)),
                ('failed', models.BooleanField(default=False)),
                ('content', models.CharField(max_length=1600, validators=[django.core.validators.RegexValidator('^[\\s\\w@?£!1$"¥#è?¤é%ù&ì\\ò(Ç)*:Ø+;ÄäøÆ,<LÖlöæ\\-=ÑñÅß.>ÜüåÉ/§à¡¿\']+$', message='You can only use GSM characters.')], verbose_name='Message')),
                ('sent_by', models.CharField(help_text='User that sent message. Stored for auditing purposes.', max_length=200, verbose_name='Sender')),
                ('recipient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apostello.Recipient')),
                ('recipient_group', models.ForeignKey(blank=True, help_text='Group (if any) that message was sent to', null=True, on_delete=django.db.models.deletion.CASCADE, to='apostello.RecipientGroup')),
            ],
        ),
    ]
