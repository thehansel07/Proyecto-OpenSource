# Generated by Django 5.0.6 on 2024-05-24 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codename', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
                ('first_name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DispensariomedicoEspecialidadesmedicos',
            fields=[
                ('idespecialidades', models.AutoField(db_column='idEspecialidades', primary_key=True, serialize=False)),
                ('descripcion', models.TextField(blank=True, db_column='Descripcion', null=True)),
                ('estado', models.TextField(blank=True, db_column='Estado', null=True)),
            ],
            options={
                'db_table': 'DispensarioMedico_especialidadesmedicos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DispensariomedicoMarcas',
            fields=[
                ('idmarca', models.AutoField(db_column='idMarca', primary_key=True, serialize=False)),
                ('descripcion', models.TextField(blank=True, db_column='Descripcion', null=True)),
                ('estado', models.TextField(blank=True, db_column='Estado', null=True)),
            ],
            options={
                'db_table': 'DispensarioMedico_marcas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DispensariomedicoMedicos',
            fields=[
                ('idmedico', models.AutoField(db_column='idMedico', primary_key=True, serialize=False)),
                ('nombre', models.TextField(blank=True, db_column='Nombre', null=True)),
                ('cedula', models.TextField(db_column='Cedula', unique=True)),
            ],
            options={
                'db_table': 'DispensarioMedico_medicos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DispensariomedicoPacientes',
            fields=[
                ('idPaciente', models.AutoField(db_column='IdPaciente', primary_key=True, serialize=False)),
                ('nombre', models.TextField(blank=True, db_column='Nombre', null=True)),
                ('cedula', models.TextField(blank=True, db_column='Cedula', null=True)),
                ('nocarnet', models.TextField(blank=True, db_column='NoCarnet', null=True)),
            ],
            options={
                'db_table': 'DispensarioMedico_pacientes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DispensariomedicoTipopacientes',
            fields=[
                ('idTipoPaciente', models.AutoField(db_column='IdTipoPaciente', primary_key=True, serialize=False)),
                ('descripcion', models.TextField(blank=True, db_column='Descripcion', null=True)),
                ('estado', models.TextField(blank=True, db_column='Estado', null=True)),
            ],
            options={
                'db_table': 'DispensarioMedico_tipopacientes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DispensariomedicoUbicacioness',
            fields=[
                ('idubicaciones', models.AutoField(db_column='idUbicaciones', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, db_column='Descripcion', max_length=50, null=True)),
                ('estante', models.TextField(blank=True, db_column='Estante', null=True)),
                ('tramo', models.TextField(blank=True, db_column='Tramo', null=True)),
                ('celda', models.TextField(blank=True, db_column='Celda', null=True)),
                ('estado', models.TextField(blank=True, db_column='Estado', null=True)),
            ],
            options={
                'db_table': 'DispensarioMedico_ubicacioness',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DispensariomedicoVisitas',
            fields=[
                ('idvisitas', models.AutoField(db_column='idVisitas', primary_key=True, serialize=False)),
                ('horavisita', models.TimeField(blank=True, db_column='HoraVisita', null=True)),
                ('medicamentossuministrado', models.TextField(blank=True, db_column='MedicamentosSuministrado', null=True)),
                ('recomendaciones', models.TextField(blank=True, db_column='Recomendaciones', null=True)),
                ('estado', models.TextField(blank=True, db_column='Estado', null=True)),
            ],
            options={
                'db_table': 'DispensarioMedico_visitas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
                ('action_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Especialidadesmedicos',
            fields=[
                ('idespecialidades', models.AutoField(db_column='idEspecialidades', primary_key=True, serialize=False)),
                ('descripcion', models.TextField(blank=True, db_column='Descripcion', null=True)),
                ('estado', models.TextField(blank=True, db_column='Estado', null=True)),
            ],
            options={
                'db_table': 'EspecialidadesMedicos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Marcas',
            fields=[
                ('idmarca', models.AutoField(db_column='idMarca', primary_key=True, serialize=False)),
                ('descripcion', models.TextField(blank=True, db_column='Descripcion', null=True)),
                ('estado', models.TextField(blank=True, db_column='Estado', null=True)),
            ],
            options={
                'db_table': 'Marcas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Medicos',
            fields=[
                ('idmedico', models.AutoField(db_column='idMedico', primary_key=True, serialize=False)),
                ('nombre', models.TextField(blank=True, db_column='Nombre', null=True)),
                ('cedula', models.TextField(db_column='Cedula', unique=True)),
            ],
            options={
                'db_table': 'Medicos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('idPaciente', models.AutoField(db_column='IdPaciente', primary_key=True, serialize=False)),
                ('nombre', models.TextField(blank=True, db_column='Nombre', null=True)),
                ('cedula', models.TextField(blank=True, db_column='Cedula', null=True)),
                ('nocarnet', models.TextField(blank=True, db_column='NoCarnet', null=True)),
                ('estado', models.TextField(blank=True, db_column='Estado', null=True)),
            ],
            options={
                'db_table': 'Pacientes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipofarmacos',
            fields=[
                ('idtipofarmaco', models.AutoField(db_column='idTipoFarmaco', primary_key=True, serialize=False)),
                ('descripcion', models.TextField(blank=True, db_column='Descripcion', null=True)),
                ('estado', models.TextField(blank=True, db_column='Estado', null=True)),
            ],
            options={
                'db_table': 'TipoFarmacos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipopacientes',
            fields=[
                ('idTipoPaciente', models.AutoField(db_column='IdTipoPaciente', primary_key=True, serialize=False)),
                ('descripcion', models.TextField(blank=True, db_column='Descripcion', null=True)),
                ('estado', models.TextField(blank=True, db_column='Estado', null=True)),
            ],
            options={
                'db_table': 'TipoPacientes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ubicacioness',
            fields=[
                ('idubicaciones', models.AutoField(db_column='idUbicaciones', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, db_column='Descripcion', max_length=50, null=True)),
                ('estante', models.TextField(blank=True, db_column='Estante', null=True)),
                ('tramo', models.TextField(blank=True, db_column='Tramo', null=True)),
                ('celda', models.TextField(blank=True, db_column='Celda', null=True)),
                ('estado', models.TextField(blank=True, db_column='Estado', null=True)),
            ],
            options={
                'db_table': 'Ubicacioness',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Visitas',
            fields=[
                ('idvisitas', models.AutoField(db_column='idVisitas', primary_key=True, serialize=False)),
                ('fechavisita', models.DateField(blank=True, db_column='FechaVisita', null=True)),
                ('horavisita', models.TimeField(blank=True, db_column='HoraVisita', null=True)),
                ('medicamentossuministrado', models.TextField(blank=True, db_column='MedicamentosSuministrado', null=True)),
                ('recomendaciones', models.TextField(blank=True, db_column='Recomendaciones', null=True)),
                ('estado', models.TextField(blank=True, db_column='Estado', null=True)),
            ],
            options={
                'db_table': 'Visitas',
                'managed': False,
            },
        ),
    ]
