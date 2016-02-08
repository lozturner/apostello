# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-24 15:15
from __future__ import unicode_literals

import apostello.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultResponses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_no_keyword_auto_reply', models.TextField(default='Thank you, %name%, your message has been received.', help_text='This message will be sent when a SMS matched a keyword, but that keyword has no reply set', max_length=1000, validators=[apostello.validators.less_than_sms_char_limit])),
                ('default_no_keyword_not_live', models.TextField(default='Thank you, %name%, for your text. But "%keyword%" is not active..', help_text='Default message for when a keyword is not currently active.', max_length=1000, validators=[apostello.validators.less_than_sms_char_limit])),
                ('keyword_no_match', models.TextField(default='Thank you, %name%, your message has not matched any of our keywords. Please correct your message and try again.', help_text='Reply to use when an SMS does not match any keywords', max_length=1000, validators=[apostello.validators.less_than_sms_char_limit])),
                ('start_reply', models.TextField(default='Thanks for signing up!', help_text='Reply to use when someone matches "start"', max_length=1000, validators=[apostello.validators.less_than_sms_char_limit])),
                ('name_update_reply', models.TextField(default='Thanks %s!', help_text='Reply to use when someone matches "name".', max_length=1000, validators=[apostello.validators.less_than_sms_char_limit])),
                ('name_failure_reply', models.TextField(default="Something went wrong, sorry, please try again with the format 'name John Smith'.", help_text='Reply to use when someone matches "name"with bad formatting.', max_length=1000, validators=[apostello.validators.less_than_sms_char_limit])),
                ('auto_name_request', models.TextField(default="Hi there, I'm afraid we currently don't have your number inour address book. Could you please reply in the format\n'name John Smith'", help_text='Message to send when we first receive a message from someone not in the contacts list.', max_length=1000, validators=[apostello.validators.less_than_sms_char_limit])),
            ],
            options={
                'verbose_name': 'Default Responses',
            },
        ),
        migrations.CreateModel(
            name='ElvantoGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sync', models.BooleanField(default=False, verbose_name='Automatic Sync')),
                ('name', models.CharField(max_length=255, verbose_name='Group Name')),
                ('e_id', models.CharField(max_length=36, unique=True, verbose_name='Elvanto ID')),
                ('last_synced', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_archived', models.BooleanField(default=False, verbose_name='Archived')),
                ('keyword', models.SlugField(max_length=12, unique=True, validators=[apostello.validators.validate_lower, django.core.validators.RegexValidator('^[\\s\\w@?£!1$"¥#è?¤é%ù&ì\\ò(Ç)*:Ø+;ÄäøÆ,<LÖlöæ\\-=ÑñÅß.>ÜüåÉ/§à¡¿\']+$', message='You can only use GSM characters.'), apostello.validators.twilio_reserved, apostello.validators.no_overlap_keyword], verbose_name='Keyword')),
                ('description', models.CharField(max_length=200, verbose_name='Keyword Description')),
                ('custom_response', models.CharField(blank=True, help_text='This text will be sent back as a reply when any incoming message matches this keyword. If empty, the site wide response will be used.', max_length=100, validators=[django.core.validators.RegexValidator('^[\\s\\w@?£!1$"¥#è?¤é%ù&ì\\ò(Ç)*:Ø+;ÄäøÆ,<LÖlöæ\\-=ÑñÅß.>ÜüåÉ/§à¡¿\']+$', message='You can only use GSM characters.'), apostello.validators.less_than_sms_char_limit], verbose_name='Auto response')),
                ('deactivated_response', models.CharField(blank=True, help_text="Use this if you want a custom response after deactivation. e.g. 'You are too late for this event, sorry!'", max_length=100, validators=[django.core.validators.RegexValidator('^[\\s\\w@?£!1$"¥#è?¤é%ù&ì\\ò(Ç)*:Ø+;ÄäøÆ,<LÖlöæ\\-=ÑñÅß.>ÜüåÉ/§à¡¿\']+$', message='You can only use GSM characters.'), apostello.validators.less_than_sms_char_limit], verbose_name='Deactivated response')),
                ('too_early_response', models.CharField(blank=True, help_text="Use this if you want a custom response before. e.g. 'You are too early for this event, please try agian on Monday!'", max_length=1000, validators=[django.core.validators.RegexValidator('^[\\s\\w@?£!1$"¥#è?¤é%ù&ì\\ò(Ç)*:Ø+;ÄäøÆ,<LÖlöæ\\-=ÑñÅß.>ÜüåÉ/§à¡¿\']+$', message='You can only use GSM characters.'), apostello.validators.less_than_sms_char_limit], verbose_name='Not yet activated response')),
                ('activate_time', models.DateTimeField(default=django.utils.timezone.now, help_text='The keyword will not be active before this time and so no messages will be able to match it. Leave blank to activate now.', verbose_name='Activation Time')),
                ('deactivate_time', models.DateTimeField(blank=True, help_text='The keyword will not be active after this time and so no messages will be able to match it. Leave blank to never deactivate.', null=True, verbose_name='Deactivation Time')),
                ('last_email_sent_time', models.DateTimeField(blank=True, null=True, verbose_name='Time of last sent email')),
                ('owners', models.ManyToManyField(blank=True, help_text='If this field is empty, any user can see this keyword. If populated, then only the named users and staff will have access.', to=settings.AUTH_USER_MODEL, verbose_name='Limit viewing to only these people')),
                ('subscribed_to_digest', models.ManyToManyField(blank=True, help_text='Choose users that will receive daily updates of matched messages.', related_name='subscribers', to=settings.AUTH_USER_MODEL, verbose_name='Subscribed to daily emails.')),
            ],
            options={
                'ordering': ['keyword'],
            },
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_archived', models.BooleanField(default=False, verbose_name='Archived')),
                ('is_blocking', models.BooleanField(default=False, help_text="If our number has received on of Twilio's stop words, we are now blocked.", verbose_name='Blocking')),
                ('first_name', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator('^[\\s\\w@?£!1$"¥#è?¤é%ù&ì\\ò(Ç)*:Ø+;ÄäøÆ,<LÖlöæ\\-=ÑñÅß.>ÜüåÉ/§à¡¿\']+$', message='You can only use GSM characters.')], verbose_name='First Name')),
                ('last_name', models.CharField(max_length=40, validators=[django.core.validators.RegexValidator('^[\\s\\w@?£!1$"¥#è?¤é%ù&ì\\ò(Ç)*:Ø+;ÄäøÆ,<LÖlöæ\\-=ÑñÅß.>ÜüåÉ/§à¡¿\']+$', message='You can only use GSM characters.')], verbose_name='Last Name')),
                ('number', phonenumber_field.modelfields.PhoneNumberField(help_text='Cannot be our number, or we get an SMS loop.', max_length=128, unique=True, validators=[apostello.validators.not_twilio_num])),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='RecipientGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_archived', models.BooleanField(default=False, verbose_name='Archived')),
                ('name', models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[\\s\\w@?£!1$"¥#è?¤é%ù&ì\\ò(Ç)*:Ø+;ÄäøÆ,<LÖlöæ\\-=ÑñÅß.>ÜüåÉ/§à¡¿\']+$', message='You can only use GSM characters.')], verbose_name='Name of group')),
                ('description', models.CharField(max_length=200, verbose_name='Group description')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(default='apostello', max_length=255)),
                ('sms_char_limit', models.PositiveSmallIntegerField(default=160, help_text='SMS length limit.')),
                ('disable_all_replies', models.BooleanField(default=False, help_text='Tick this box to disable all automated replies')),
                ('office_email', models.EmailField(blank=True, help_text='Email to send information emails to', max_length=254)),
                ('from_email', models.EmailField(blank=True, help_text='Email to send emails from', max_length=254)),
                ('slack_url', models.URLField(blank=True, help_text='Post all incoming messages to this slack hook. Leave blank to disable.')),
                ('sync_elvanto', models.BooleanField(default=False, help_text='Toggle automatic syncing of Elvanto groups. Sync will be done overnight')),
            ],
            options={
                'verbose_name': 'Site Configuration',
            },
        ),
        migrations.CreateModel(
            name='SmsInbound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(help_text="Twilio's unique ID for this SMS", max_length=34, unique=True, verbose_name='SID')),
                ('is_archived', models.BooleanField(default=False, verbose_name='Is Archived')),
                ('dealt_with', models.BooleanField(default=False, help_text='Used, for example, to mark people as registered for an event.', verbose_name='Dealt With?')),
                ('content', models.CharField(blank=True, max_length=1600, verbose_name='Message body')),
                ('time_received', models.DateTimeField(blank=True, null=True)),
                ('sender_name', models.CharField(max_length=200, verbose_name='Sent by')),
                ('sender_num', models.CharField(max_length=200, verbose_name='Sent from')),
                ('matched_keyword', models.CharField(max_length=12)),
                ('matched_colour', models.CharField(max_length=7)),
                ('matched_link', models.CharField(max_length=200)),
                ('display_on_wall', models.BooleanField(default=False, help_text='If True, SMS will be shown on all live walls.', verbose_name='Display on Wall?')),
            ],
            options={
                'ordering': ['-time_received'],
            },
        ),
        migrations.CreateModel(
            name='SmsOutbound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(help_text="Twilio's unique ID for this SMS", max_length=34, unique=True, verbose_name='SID')),
                ('content', models.CharField(max_length=1600, validators=[django.core.validators.RegexValidator('^[\\s\\w@?£!1$"¥#è?¤é%ù&ì\\ò(Ç)*:Ø+;ÄäøÆ,<LÖlöæ\\-=ÑñÅß.>ÜüåÉ/§à¡¿\']+$', message='You can only use GSM characters.')], verbose_name='Message')),
                ('time_sent', models.DateTimeField(default=django.utils.timezone.now)),
                ('sent_by', models.CharField(help_text='User that sent message. Stored for auditing purposes.', max_length=200, verbose_name='Sender')),
                ('recipient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apostello.Recipient')),
                ('recipient_group', models.ForeignKey(blank=True, help_text='Group (if any) that message was sent to', null=True, on_delete=django.db.models.deletion.CASCADE, to='apostello.RecipientGroup')),
            ],
            options={
                'ordering': ['-time_sent'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False, help_text='This must be true to grant users access to the site.')),
                ('can_see_groups', models.BooleanField(default=True)),
                ('can_see_contact_names', models.BooleanField(default=True)),
                ('can_see_keywords', models.BooleanField(default=True)),
                ('can_see_outgoing', models.BooleanField(default=True)),
                ('can_see_incoming', models.BooleanField(default=True)),
                ('can_send_sms', models.BooleanField(default=False)),
                ('can_see_contact_nums', models.BooleanField(default=False)),
                ('can_import', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='recipient',
            name='groups',
            field=models.ManyToManyField(blank=True, to='apostello.RecipientGroup'),
        ),
    ]