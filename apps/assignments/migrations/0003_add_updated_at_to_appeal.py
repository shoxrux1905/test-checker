from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("assignments", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="appeal",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
