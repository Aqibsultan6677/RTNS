from django.apps import AppConfig


class CertificateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'certificate'
    verbose_name="Generate Certificates for Speakers"
