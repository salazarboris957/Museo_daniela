from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='ArticuloBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('contenido', models.TextField()),
                ('imagen_portada', models.ImageField(upload_to='blog/')),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('etiquetas', models.CharField(max_length=200)),
            ],
        ),
    ]
