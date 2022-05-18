import logging

from django.core.management.base import BaseCommand

from processor.models import Client, Domain

logging.getLogger().addHandler(logging.StreamHandler())


class Command(BaseCommand):
    COMMAND_NAME = 'create_public_tenant'

    def add_arguments(self, parser):
        parser.add_argument(
            "-d",
            "--domain",
            dest="domain",
            default='localhost',
        )

        super().add_arguments(parser)

    def handle(self, *args, **kwargs):
        try:
            tenant = Client.objects.get(schema_name='public')
            if tenant:
                logging.info('Public schema client already exists.')
        except Client.DoesNotExist:
            tenant = Client(schema_name='public', name='localhost', description='localhost registration')
            logging.info(f"tenant created with public schema")
            tenant.save()

        try:
            domain_name = kwargs.get('domain')
            domain = Domain.objects.get(domain=kwargs.get('domain'))
            if domain:
                logging.info(f"{domain_name} domain already exists. Please use different one")
        except Domain.DoesNotExist:
            domain = Domain()
            domain.domain = kwargs.get('domain')
            domain.tenant = tenant
            domain.is_primary = True
            domain.save()
            logging.info(f"{domain_name} domain created")
