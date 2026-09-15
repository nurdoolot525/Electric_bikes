from django.db import migrations


def add_detail_data(apps, schema_editor):
    Product = apps.get_model('shop', 'Product')

    data = {
        'Bianchi AQUILA L DURA ACE DI2 TEAM JUMBO 2021': {
            'article': 'BIAQ-0001',
            'description': 'Шоссейный велосипед топ-класса с электронной группой Shimano Dura-Ace Di2. Лёгкая рама, сверхплавное переключение передач, карбоновые колёса.',
            'sizes': '50, 53, 55, 58 см',
            'colors': 'Чёрный, Белый, Красный',
            'characteristics': 'Тип велосипеда: Шоссейный\nМатериал рамы: Карбон\nКолёса: 28 дюймов\nКоличество скоростей: 22\nВес: 7,4 кг\nТормоза: Дисковые гидравлические\nГод выпуска: 2021',
        },
        'Trek Verve 2 Disc Lithium Grey HYBD 2022': {
            'article': 'TRV-0002',
            'description': 'Городской гибридный велосипед для комфортных поездок по городу. Удобная посадка, дисковые тормоза и надёжные компоненты.',
            'sizes': 'XS, S, M, L, XL',
            'colors': 'Серый, Синий',
            'characteristics': 'Тип велосипеда: Гибридный\nМатериал рамы: Алюминий\nКолёса: 27.5 дюймов\nКоличество скоростей: 9\nВес: 13,8 кг\nТормоза: Дисковые механические\nГод выпуска: 2022',
        },
        'Trek Marlin 7 Matte Nautical Navy Matte Anth ATB 29 2022': {
            'article': 'TRM-0003',
            'description': 'Горный велосипед с колёсами 29 дюймов для кросс-кантри и активного отдыха. Подходит для новичков и опытных райдеров.',
            'sizes': 'S, M, L, XL',
            'colors': 'Тёмно-синий, Чёрный',
            'characteristics': 'Тип велосипеда: Горный\nМатериал рамы: Алюминий\nКолёса: 29 дюймов\nКоличество скоростей: 18\nВес: 13,1 кг\nТормоза: Дисковые гидравлические\nГод выпуска: 2022',
        },
        'Look 977 BLACK FLUO YELLOW GREEN XT 2x11S AMC 2018': {
            'article': 'LOK-0004',
            'description': 'Горный маунтинбайк с усиленной рамой и элементами кросс-кантри. Отличная управляемость на любой трассе.',
            'sizes': 'M, L',
            'colors': 'Чёрный, Жёлтый, Зелёный',
            'characteristics': 'Тип велосипеда: Горный\nМатериал рамы: Карбон\nКолёса: 29 дюймов\nКоличество скоростей: 22\nВес: 11,9 кг\nТормоза: Дисковые гидравлические\nГод выпуска: 2018',
        },
        'Orbea ALMA H30 2021': {
            'article': 'ORB-0005',
            'description': 'Горный карбоновый велосипед для гонок по пересечённой местности. Лёгкий, быстрый и надёжный.',
            'sizes': 'S, M, L, XL',
            'colors': 'Чёрный, Оранжевый',
            'characteristics': 'Тип велосипеда: Горный\nМатериал рамы: Карбон\nКолёса: 29 дюймов\nКоличество скоростей: 12\nВес: 11,5 кг\nТормоза: Дисковые гидравлические\nГод выпуска: 2021',
        },
        'Trek Fx 3 Disc Dnister Black HYBD 2022': {
            'article': 'TRF-0006',
            'description': 'Скоростной гибридный велосипед для города и шоссе. Проворный, лёгкий и комфортный в любых условиях.',
            'sizes': 'M, L, XL',
            'colors': 'Чёрный',
            'characteristics': 'Тип велосипеда: Гибридный\nМатериал рамы: Алюминий\nКолёса: 28 дюймов\nКоличество скоростей: 27\nВес: 12,7 кг\nТормоза: Дисковые гидравлические\nГод выпуска: 2022',
        },
        'Scott Scale 700 RS 2016': {
            'article': 'SCT-0007',
            'description': 'Лёгкий горный велосипед с карбоновой рамой. Отличный выбор для любителей гонок и тренировок.',
            'sizes': 'S, M, L',
            'colors': 'Чёрный, Красный',
            'characteristics': 'Тип велосипеда: Горный\nМатериал рамы: Карбон\nКолёса: 29 дюймов\nКоличество скоростей: 20\nВес: 12,3 кг\nТормоза: Дисковые гидравлические\nГод выпуска: 2016',
        },
        'Scott Scale 700 SL 2016': {
            'article': 'SCT-0008',
            'description': 'Облегчённая версия горного велосипеда для профессионалов. Максимальная жёсткость и минимальный вес.',
            'sizes': 'S, M, L, XL',
            'colors': 'Чёрный, Белый',
            'characteristics': 'Тип велосипеда: Горный\nМатериал рамы: Карбон\nКолёса: 29 дюймов\nКоличество скоростей: 22\nВес: 11,2 кг\nТормоза: Дисковые гидравлические\nГод выпуска: 2016',
        },
        'Trek Marlin 4 Aloha ATB 27.5 2022': {
            'article': 'TRM-0009',
            'description': 'Бюджетный горный велосипед для начинающих. Надёжная рама, 21 скорость и комфортная посадка.',
            'sizes': 'S, M, L',
            'colors': 'Алоха, Чёрный',
            'characteristics': 'Тип велосипеда: Горный\nМатериал рамы: Алюминий\nКолёса: 27.5 дюймов\nКоличество скоростей: 21\nВес: 14,2 кг\nТормоза: Ободные V-brake\nГод выпуска: 2022',
        },
        'Orbea RUDE 10 2022': {
            'article': 'ORB-0010',
            'description': 'Горный велосипед с 29-дюймовыми колёсами для трейлов. Уверенное поведение на спусках и подъёмах.',
            'sizes': 'S, M, L, XL',
            'colors': 'Чёрный, Зелёный',
            'characteristics': 'Тип велосипеда: Горный\nМатериал рамы: Алюминий\nКолёса: 29 дюймов\nКоличество скоростей: 12\nВес: 13,5 кг\nТормоза: Дисковые гидравлические\nГод выпуска: 2022',
        },
    }

    for product in Product.objects.all():
        values = data.get(product.title)
        if not values:
            continue
        product.article = values['article']
        product.description = values['description']
        product.sizes = values['sizes']
        product.colors = values['colors']
        product.quantity = 5
        product.characteristics = values['characteristics']
        product.save()


def remove_detail_data(apps, schema_editor):
    Product = apps.get_model('shop', 'Product')
    Product.objects.all().update(
        article='',
        description='',
        sizes='',
        colors='',
        quantity=1,
        characteristics='',
    )


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_product_article_product_characteristics_and_more'),
    ]

    operations = [
        migrations.RunPython(add_detail_data, remove_detail_data),
    ]