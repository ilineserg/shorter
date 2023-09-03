# URL Shorter

Приложение умеет делать короткие ссылки из длинных

## Требования

Перед запуском вашего приложения убедитесь, что у вас установлены следующие компоненты:

- [Docker](https://docs.docker.com/engine/install/)
- Виртуальное окружение для Python. Например, [Pyenv](https://github.com/pyenv/pyenv#installation).

## Установка

1. Создайте виртуальное окружение для приложения с версией Python 3.11

2. Клонируйте репозиторий на свой локальный компьютер:

   ```bash
   git clone https://github.com/ilineserg/shorter.git
   
3. Перейдите в корневую папку с проектом 

    ```bash
   cd shorter
   
4. Установите poetry

    ```bash
   pip install poetry

5. Установите зависимости

    ```bash
   poetry install


## Запуск

1. Запустите сборку докера с PostgreSQL

    ```bash
   docker-compose up --build -d

2. Примените миграции к базе данных

    ```bash
   alembic upgrade head
   
4. Запустите приложение

    ```bash
   uvicorn shorter.api:app --host <ip-address> --port <port>
  

## Использование

Доступные методы можно посмотреть в Swagger документации

http://ip-address:port/docs