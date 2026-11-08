from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Cria ou atualiza o utilizador admin automaticamente'

    def handle(self, *args, **options):
        user, criado = User.objects.get_or_create(username='admin')
        user.set_password('admin123')
        user.is_superuser = True
        user.is_staff = True
        user.save()
        if criado:
            self.stdout.write(self.style.SUCCESS('Utilizador "admin" criado com sucesso!'))
        else:
            self.stdout.write(self.style.SUCCESS('Utilizador "admin" atualizado com sucesso!'))