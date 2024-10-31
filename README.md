### Разработчик проекта: Лоскутова Татьяна (Loskutova Tatiana)

# Ссылки на задеполенный API в сети:
Backend Api: api.dev.tanishahelper.ru/api/

admin@gmail.com
Loskutidze1988

### Технологический стек
- Python - основной язык программирования.
- Django REST framework - инструмент для создания веб-API на основе Django
- GIT - система контроля версий проекта
- Pytest - инструмент для тестирования проекта
- Swager - инструмент для документирования
- Docker - контейнеризация приложения
- CI/CD - непрерывная интеграция и развертывание

# Breaks Helper - Назначение проекта
> API Сервис для организации работы сотрудников. Сервис предоставляет возможность создание организации, групп внутри организации, рабочих смен и обедов сотрудников.


# Установка проекта в Docker
1. Создание образа и запуск
```
docker-compose up -d
```
2. Инициализация проекта
```
docker-compose exec web make initial
```
3. Добавление суперюзера
```
docker-compose exec web python manage.py createsuperuser
```
4. Проверить

## Основной функционал
### Пользователи
**Возможности:**
1. Идентификация и аутентификация (вход по никнейму, телефонму или почте)
2. Просмотр и изменение профиля
3. Смена пароля

### Корпоративные пользователи
Корпортаивного пользователя может создавать руководство организации

**Особенности:**

1. Управлять корпоративным аккаунтом может только руководитель организации.
2. Удалять из организации корпоративный аккаунт нельзя, только удаляется полностью профиль
3. Пользователь не может сменить организацию
4. Пользователь не может менять персональные данные, кроме номера телефона и пароля

---

### Организации и группы
**Возможности для создателя организации:**
1. Создать и изменять, просматривать и удалять организацию
2. Приглашать пользователей системы в организацию
3. Назначать сотрудникам организации должности
4. Создавать группы внутри организаций
5. Назначать участников группы из списка сотрудников организации


**Возможности для сотрудников организации:**
1. Подавать заявки и вступать в организации
2. Просматривать список организаций и групп
4. Только руководитель организации может создавать смены на день и задавать временные интервалы смен
3. Выходить из организации
---

### Обеденные перерывы и смены
1. Возможность бронировать обеденные перервы в зависимости от условий. Есть ли свободный слот, учитвая кол-во online сотрудников. Происходят разного рода валидации
2. Если будет фронт, то будет возможность для кнопок, чтобы менять статусы