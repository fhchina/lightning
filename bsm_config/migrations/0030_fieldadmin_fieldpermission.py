# Generated by Django 2.2.9 on 2020-10-28 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('bsm_config', '0029_auto_20200926_0010'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=150, verbose_name='字段名')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsm_config.Admin', verbose_name='关联Admin')),
            ],
            options={
                'verbose_name': 'Admin字段配置',
                'verbose_name_plural': 'Admin字段配置',
                'unique_together': {('admin', 'field')},
            },
        ),
        migrations.CreateModel(
            name='FieldPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read', models.BooleanField(default=True, verbose_name='读')),
                ('write', models.BooleanField(default=True, verbose_name='写')),
                ('field_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsm_config.FieldAdmin', verbose_name='关联字段')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group', verbose_name='角色')),
            ],
            options={
                'verbose_name': '字段权限配置',
                'verbose_name_plural': '字段权限配置',
                'unique_together': {('field_admin', 'group')},
            },
        ),
    ]
