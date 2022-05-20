from django.conf import settings
from django.db import migrations
from oauth2_provider.models import AbstractApplication


def create_oauth_app(apps, schema_editor):
    OAuth2App = apps.get_model('oauth2_provider', 'Application')
    OAuth2App.objects.create(
        name=settings.OAUTH2_APP_NAME,
        client_type=AbstractApplication.CLIENT_PUBLIC,
        authorization_grant_type=AbstractApplication.GRANT_PASSWORD
    )


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0023_activity_ordering'),
        ('oauth2_provider', '0006_alter_application_client_secret'),
    ]

    operations = [
        migrations.RunPython(create_oauth_app, migrations.RunPython.noop)
    ]
