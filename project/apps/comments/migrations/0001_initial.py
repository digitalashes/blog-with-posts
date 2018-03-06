# Generated by Django 2.0.3 on 2018-03-06 22:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('body', models.TextField(help_text='Comment Body.', max_length=1024, verbose_name='Comment')),
                ('ip_address', models.GenericIPAddressField(default='0.0.0.0', help_text='Comment Author IP Address.', verbose_name='Ip Address')),
                ('post', models.ForeignKey(help_text='Post.', on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='posts.Post', verbose_name='Post')),
                ('user', models.ForeignKey(help_text='Comment Author.', on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ('-created', 'user'),
            },
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['post', 'body', 'user', 'ip_address'], name='comments_co_post_id_535be7_idx'),
        ),
    ]