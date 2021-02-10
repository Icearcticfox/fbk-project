~~~~
1. Напишите на Python скрипт, который будет из POST запроса писать значение в базу данных (использовать Postgres).

2. Скрипт и БД должны быть упакованы в Docker.

3. Настройте nginx, который будет запрещать GET-запросы к скрипту.

4. Все должно запускаться из docker-compose.yml.

5. Все сервисы должны общаться между собой через внутреннюю сеть Docker. Nginx должен быть доступен на порту 8080.

6. Код, Dockerfile и docker-compose.yml выложите в публичный доступ на GitHub.
~~~~
Для запуска:
~~~~
sudo docker-compose --env-file .env.sample up
~~~~
sudo docker-compose --env-file .env.sample up