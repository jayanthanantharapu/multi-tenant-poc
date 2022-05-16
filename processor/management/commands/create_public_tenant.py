import logging

from django.core.exceptions import ObjectDoesNotExist
from django_tenants.management.commands import BaseTenantCommand

from processor.models import Client, Domain


class Command(BaseTenantCommand):
    COMMAND_NAME = 'create_public_tenant'

    def add_arguments(self, parser):
        parser.add_argument(
            "-d",
            "--domain",
            dest="input-path",
            default='localhost',
        )

        super().add_arguments(parser)

    def handle(self, *args, **kwargs):
        super().handle(*args, **kwargs)

        try:
            if Client.objects.get(schema_nanme='public'):
                logging.info('Public schema client already exists.')
        except ObjectDoesNotExist:
            tenant = Client(schema_name='public', name='localhost', description='localhost registration')
            tenant.save()

        try:
            if Domain.objects.get(domain=kwargs.get('domain')):
                logging.info(f"{kwargs.get('domain')} domain already exists. Please use different one")
        except ObjectDoesNotExist:
            domain = Domain()
            domain.domain = kwargs.get('domain')
            domain.tenant = tenant
            domain.is_primary = True
            domain.save()
