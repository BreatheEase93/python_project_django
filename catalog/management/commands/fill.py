import os
from django.core.management import BaseCommand, call_command
from catalog.models import Category, Product
from config.settings import BASE_DIR

class Command(BaseCommand):
    help = 'Очищает базу данных и загружает данные из фикстуры'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        fixture_path = os.path.join(BASE_DIR, 'library_fixture.json')

        try:
            call_command('loaddata', fixture_path)
            self.stdout.write(self.style.SUCCESS(f'Данные из {fixture_path} успешно загружены!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при загрузке фикстуры: {e}'))
