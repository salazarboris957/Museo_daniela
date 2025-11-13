from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='Personalizado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('descripcion', models.TextField()),
                ('referencia', models.ImageField(blank=True, upload_to='referencias/')),
                ('presupuesto', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('estado', models.CharField(choices=[('solicitado', '📥 Solicitado'), ('cotizado', '💰 Cotizado'), ('en_proceso', '🎨 En Proceso'), ('completado', '✅ Completado'), ('entregado', '🎉 Entregado')], default='solicitado', max_length=20)),
                ('fecha_solicitud', models.DateTimeField(auto_now_add=True)),
                ('historia_publica', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProcesoPersonalizado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='proceso_personalizados/')),
                ('descripcion', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('personalizado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personalizados.personalizado')),
            ],
        ),
    ]
