from django.db import models

# Create your models here.

class DispensariomedicoEspecialidadesmedicos(models.Model):
    idespecialidades = models.AutoField(db_column='idEspecialidades', primary_key=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    estado = models.TextField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DispensarioMedico_especialidadesmedicos'

class DispensariomedicoMarcas(models.Model):
    idmarca = models.AutoField(db_column='idMarca', primary_key=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    estado = models.TextField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DispensarioMedico_marcas'


class DispensariomedicoMedicos(models.Model):
    idmedico = models.AutoField(db_column='idMedico', primary_key=True)  # Field name made lowercase.
    nombre = models.TextField(db_column='Nombre', blank=True, null=True)  # Field name made lowercase.
    cedula = models.TextField(db_column='Cedula', unique=True)  # Field name made lowercase.
    idespecialidades = models.ForeignKey(DispensariomedicoEspecialidadesmedicos, models.DO_NOTHING, db_column='idEspecialidades', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DispensarioMedico_medicos'


class DispensariomedicoPacientes(models.Model):
    idPaciente = models.AutoField(db_column='IdPaciente', primary_key=True)  # Field name made lowercase.
    nombre = models.TextField(db_column='Nombre', blank=True, null=True)  # Field name made lowercase.
    cedula = models.TextField(db_column='Cedula', blank=True, null=True)  # Field name made lowercase.
    nocarnet = models.TextField(db_column='NoCarnet', blank=True, null=True)  # Field name made lowercase.
    idTipoPaciente = models.ForeignKey('DispensariomedicoTipopacientes', models.DO_NOTHING, db_column='idTipoPaciente', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DispensarioMedico_pacientes'


class DispensariomedicoTipopacientes(models.Model):
    idTipoPaciente = models.AutoField(db_column='IdTipoPaciente', primary_key=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    estado = models.TextField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DispensarioMedico_tipopacientes'


class DispensariomedicoUbicacioness(models.Model):
    idubicaciones = models.AutoField(db_column='idUbicaciones', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    estante = models.TextField(db_column='Estante', blank=True, null=True)  # Field name made lowercase.
    tramo = models.TextField(db_column='Tramo', blank=True, null=True)  # Field name made lowercase.
    celda = models.TextField(db_column='Celda', blank=True, null=True)  # Field name made lowercase.
    estado = models.TextField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DispensarioMedico_ubicacioness'


class DispensariomedicoVisitas(models.Model):
    idvisitas = models.AutoField(db_column='idVisitas', primary_key=True)  # Field name made lowercase.
    horavisita = models.TimeField(db_column='HoraVisita', blank=True, null=True)  # Field name made lowercase.
    medicamentossuministrado = models.TextField(db_column='MedicamentosSuministrado', blank=True, null=True)  # Field name made lowercase.
    recomendaciones = models.TextField(db_column='Recomendaciones', blank=True, null=True)  # Field name made lowercase.
    estado = models.TextField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    idpaciente = models.ForeignKey(DispensariomedicoPacientes, models.DO_NOTHING, db_column='idPaciente', blank=True, null=True)  # Field name made lowercase.
    idmedico = models.ForeignKey(DispensariomedicoMedicos, models.DO_NOTHING, db_column='idMedico', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DispensarioMedico_visitas'


class Especialidadesmedicos(models.Model):
    idespecialidades = models.AutoField(db_column='idEspecialidades', primary_key=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    estado = models.TextField(db_column='Estado', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'EspecialidadesMedicos'


class Marcas(models.Model):
    idmarca = models.AutoField(db_column='idMarca', primary_key=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    estado = models.TextField(db_column='Estado', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    def __str__(self):
        texto = "IdMarca:{0},Descripcion: {1} "
        return texto.format(self.idmarca, self.descripcion)

    class Meta:
        managed = True
        db_table = 'Marcas'



class Medicos(models.Model):
    idmedico = models.AutoField(db_column='idMedico', primary_key=True)  # Field name made lowercase.
    nombre = models.TextField(db_column='Nombre', blank=True, null=True)  # Field name made lowercase.
    cedula = models.TextField(db_column='Cedula', unique=True)  # Field name made lowercase.
    idespecialidades = models.ForeignKey(Especialidadesmedicos, models.DO_NOTHING, db_column='idEspecialidades', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Medicos'


class Pacientes(models.Model):
    idPaciente = models.AutoField(db_column='IdPaciente', primary_key=True)  # Field name made lowercase.
    nombre = models.TextField(db_column='Nombre', blank=True, null=True)  # Field name made lowercase.
    cedula = models.TextField(db_column='Cedula', blank=True, null=True)  # Field name made lowercase.
    nocarnet = models.TextField(db_column='NoCarnet', blank=True, null=True)  # Field name made lowercase.
    idTipoPaciente = models.ForeignKey('Tipopacientes', models.DO_NOTHING, db_column='idTipoPaciente', to_field='idTipoPaciente', blank=True, null=True)  # Field name made lowercase.
    estado = models.TextField(db_column='Estado', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Pacientes'


class Tipofarmacos(models.Model):
    idtipofarmaco = models.AutoField(db_column='idTipoFarmaco', primary_key=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    estado = models.TextField(db_column='Estado', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'TipoFarmacos'


class Tipopacientes(models.Model):
    idTipoPaciente = models.AutoField(db_column='IdTipoPaciente', primary_key=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    estado = models.TextField(db_column='Estado', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'TipoPacientes'


class Ubicacioness(models.Model):
    idubicaciones = models.AutoField(db_column='idUbicaciones', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    estante = models.TextField(db_column='Estante', blank=True, null=True)  # Field name made lowercase.
    tramo = models.TextField(db_column='Tramo', blank=True, null=True)  # Field name made lowercase.
    celda = models.TextField(db_column='Celda', blank=True, null=True)  # Field name made lowercase.
    estado = models.TextField(db_column='Estado', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Ubicacioness'


class Visitas(models.Model):
    idvisitas = models.AutoField(db_column='idVisitas', primary_key=True)  # Field name made lowercase.
    idmedico = models.ForeignKey(Medicos, models.DO_NOTHING, db_column='idMedico', blank=True, null=True)  # Field name made lowercase.
    idPaciente = models.ForeignKey(Pacientes, models.DO_NOTHING, db_column='idPaciente', to_field='idPaciente', blank=True, null=True)  # Field name made lowercase.
    fechavisita = models.DateField(db_column='FechaVisita', blank=True, null=True)  # Field name made lowercase.
    horavisita = models.TimeField(db_column='HoraVisita', blank=True, null=True)  # Field name made lowercase.
    medicamentossuministrado = models.TextField(db_column='MedicamentosSuministrado', blank=True, null=True)  # Field name made lowercase.
    recomendaciones = models.TextField(db_column='Recomendaciones', blank=True, null=True)  # Field name made lowercase.
    estado = models.TextField(db_column='Estado', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Visitas'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
