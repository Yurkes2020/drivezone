# DriveZone API

Повна платформа для керування продажем авто з ролями користувачів, преміум-аккаунтами та інтеграцією з ПриватБанком для курсів валют.

---

## Вимоги

- Docker та Docker Compose
- Git
- Python 3.13 (для локального використання без Docker, опціонально)
- Postman (для тестування API)

---

## Інструкція запуску

### 1. Клонування репозиторію


git clone <URL_твого_репозиторію>
cd <назва_папки_проєкту>

### 2. Створення .env файлу

У корені проєкту створіть .env з наступним вмістом:

USER=postgres.bixvyixpcwpzekvugxcx 

PASSWORD=Yurkes41339@

HOST=aws-1-eu-north-1.pooler.supabase.com

PORT=5432

DBNAME=postgres

DJANGO_SECRET_KEY=Yurkes41339@
DEBUG=True

3. Запуск через Docker

Створіть і запустіть контейнери:

docker-compose up --build

4. Міграції та створення суперкористувача

Відкрийте новий термінал і виконайте:

docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py createsuperuser