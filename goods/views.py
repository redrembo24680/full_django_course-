from django.shortcuts import render


def catalog(request):
    context = {
        "title": "Home - Каталог",
        "goods": [
            {
                "image": "deps/images/goods/set of tea table and three chairs.jpg",
                "name": "Чайний столик і три стільці",
                "description": "Комплект із трьох стільців і дизайнерський столик для вітальні.",
                "price": 150.00,
            },
            {
                "image": "deps/images/goods/set of tea table and two chairs.jpg",
                "name": "Чайний столик і два стільці",
                "description": "Набір із столу та двох стільців у мінімалістичному стилі.",
                "price": 93.00,
            },
            {
                "image": "deps/images/goods/double bed.jpg",
                "name": "Двоспальне ліжко",
                "description": "Двоспальне ліжко з узголів’ям, дуже ортопедичне.",
                "price": 670.00,
            },
            {
                "image": "deps/images/goods/kitchen table.jpg",
                "name": "Кухонний стіл з раковиною",
                "description": "Кухонний обідній стіл із вбудованою раковиною та стільцями.",
                "price": 365.00,
            },
            {
                "image": "deps/images/goods/kitchen table 2.jpg",
                "name": "Кухонний стіл з вбудованою плитою",
                "description": "Кухонний стіл із вбудованою плитою та раковиною. Багато полиць і стильний дизайн.",
                "price": 430.00,
            },
            {
                "image": "deps/images/goods/corner sofa.jpg",
                "name": "Кутовий диван для вітальні",
                "description": "Кутовий диван, що розкладається у двоспальне ліжко. Ідеально для прийому гостей!",
                "price": 610.00,
            },
            {
                "image": "deps/images/goods/bedside table.jpg",
                "name": "Приліжковий столик",
                "description": "Приліжковий столик із двома висувними шухлядами (квітка не входить у комплект).",
                "price": 55.00,
            },
            {
                "image": "deps/images/goods/sofa.jpg",
                "name": "Звичайний диван",
                "description": "Звичайний диван, він же софа. Нічого особливого.",
                "price": 190.00,
            },
            {
                "image": "deps/images/goods/office chair.jpg",
                "name": "Офісний стілець",
                "description": "Зручний офісний стілець для роботи.",
                "price": 30.00,
            },
            {
                "image": "deps/images/goods/plants.jpg",
                "name": "Рослина",
                "description": "Рослина для декору, що створює атмосферу свіжості та спокою.",
                "price": 10.00,
            },
            {
                "image": "deps/images/goods/flower.jpg",
                "name": "Стилізована квітка",
                "description": "Дизайнерська квітка (можливо, штучна) для прикрашення інтер’єру.",
                "price": 15.00,
            },
            {
                "image": "deps/images/goods/strange table.jpg",
                "name": "Незвичний приліжковий столик",
                "description": "Досить дивний на вигляд столик, але чудово підходить для спальні.",
                "price": 25.00,
            },
        ],
    }

    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
