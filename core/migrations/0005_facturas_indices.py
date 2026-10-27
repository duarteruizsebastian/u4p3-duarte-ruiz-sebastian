# Migración del paso 05: facturas, renglones y dos índices de consultas.
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('core', '0004_renombrar_categoria'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=120)),
                ('fecha', models.DateField(default=django.utils.timezone.localdate)),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facturas', to=settings.AUTH_USER_MODEL)),
            ],
            options={'ordering': ['-fecha', '-id']},
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='core.factura')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='detalles', to='core.servicio')),
            ],
        ),
        migrations.AddIndex(
            model_name='servicio',
            index=models.Index(fields=['propietario', 'precio'], name='servicio_prop_precio_idx'),
        ),
        migrations.AddIndex(
            model_name='factura',
            index=models.Index(fields=['usuario', 'fecha'], name='factura_usuario_fecha_idx'),
        ),
    ]
