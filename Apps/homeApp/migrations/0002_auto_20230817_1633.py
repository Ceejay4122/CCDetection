
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datafileupload',
            name='trained_model_data',
            field=models.BinaryField(null=True),
        ),
        migrations.AlterField(
            model_name='datafileupload',
            name='description',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
