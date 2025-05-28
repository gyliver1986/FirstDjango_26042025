# FestDjango_26042025

## Инструкция по развертыанию проекта
1. Создать виртуальное окружение

python3 -m venv django_venv

2. Активировать виртуальное окружение

sourse django_venv/bin/activate

3. Установите нужные библиотеки в виртуальное окружение

pip install -r reguirements.txt

4. Запуск сервера

python manage.py runserver

# Дополнительно
1. Полезное расширение для шаблонов: `django`
ext install batistio.vscode-django
2. Добавить в `setting.json`
  "emmet.excludeLanguages": {
        "django-html" : "html"
    },
    "files.associations": {
        "*.html": "django-html"
    }
      