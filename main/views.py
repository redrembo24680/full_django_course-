from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):

    categories = Categories.objects.all()

    context = {
        'title': 'Home - Головна',
        'content': "Магазин меблів Home",
        'categories': categories

    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - Про нас',
        'content': 'Про нас',
        'text_on_page': f"""
Ласкаво просимо до Home – місця, де комфорт, стиль і якість 
поєднуються в ідеальних меблевих рішеннях для вашого дому та офісу.\n

📌 Хто ми?
Ми – команда професіоналів, які знають, як створити затишок у кожному куточку вашого простору. 
Наш магазин пропонує широкий вибір меблів від надійних виробників, щоб ви могли знайти ідеальні рішення для будь-якої кімнати.\n

🎯 Наша місія
Допомагати клієнтам облаштовувати комфортні, функціональні та стильні інтер’єри, 
пропонуючи тільки якісні меблі за доступними цінами.\n

💛 Наші цінності
✔ Якість – Ми обираємо тільки перевірені матеріали та виробників.
✔ Стиль – Наш асортимент охоплює класичні, сучасні та ексклюзивні дизайнерські моделі.
✔ Комфорт – Меблі мають бути не лише красивими, а й зручними та довговічними.
✔ Клієнтоорієнтованість – Ми дбаємо про ваш комфорт на кожному етапі: від вибору меблів до доставки.\n

🚛 Чому обирають нас?
🔹 Великий асортимент для будь-якого інтер’єру
🔹 Гнучкі умови оплати та швидка доставка
🔹 Консультації від наших фахівців
🔹 Гарантія якості та сервісна підтримка\n

Ми віримо, що меблі – це більше, ніж просто предмети інтер’єру. 
Це частина вашого життя, яка створює атмосферу затишку та гармонії.\n

Завітайте до Home і переконайтеся, що обирати меблі може бути легко та приємно! 🏡✨
"""

    }

    return render(request, 'main/about.html', context)
