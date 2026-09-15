from django.db import migrations

FIELD_MAP = {
    'Цвет': 'color',
    'Год': 'year',
    'Диаметр колеса': 'wheel_size',
    'Материал рамы': 'frame_material',
    'Размер': 'size',
    'Страна': 'country',
    'Производитель': 'manufacturer',
    'Покрышки': 'tires',
    'Рама': 'frame',
    'Подседельный штырь': 'seatpost',
    'Седло': 'saddle',
    'Вилка': 'fork',
    'Вынос': 'stem',
    'Колеса': 'wheels',
    'Руль': 'handlebar',
    'Тип тормозов': 'brake_type',
    'Тормозная система': 'brake_system',
    'Манетки': 'shifters',
    'Система шатунов': 'crankset',
    'Задний переключатель': 'rear_derailleur',
    'Цепь': 'chain',
    'Количество скоростей': 'speeds',
    'Гарантия': 'warranty',
}


def fill_fields(apps, schema_editor):
    Product = apps.get_model('shop', 'Product')
    for product in Product.objects.all():
        for line in product.characteristics.splitlines():
            if ':' in line:
                name, value = line.split(':', 1)
                name = name.strip()
                field = FIELD_MAP.get(name)
                if field:
                    setattr(product, field, value.strip())
        product.save()


def clear_fields(apps, schema_editor):
    Product = apps.get_model('shop', 'Product')
    for product in Product.objects.all():
        for field in FIELD_MAP.values():
            setattr(product, field, '')
        product.save()


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_product_brake_system_product_brake_type_and_more'),
    ]

    operations = [
        migrations.RunPython(fill_fields, clear_fields),
    ]