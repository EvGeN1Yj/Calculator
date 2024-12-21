# Используем базовый образ Ubuntu
FROM ubuntu:20.04

# Устанавливаем переменные среды для минимального взаимодействия с пользователем
ENV DEBIAN_FRONTEND=noninteractive

# Обновляем пакеты и устанавливаем Python и необходимые библиотеки
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-tk \
    xvfb-run \
    && apt-get clean

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY project/ /app/

# Печатаем структуру каталогов, чтобы проверить, что все файлы скопированы
RUN ls -R /app

# Открываем порт для приложения
EXPOSE 5000

# Команда для запуска приложения
#CMD ["python3", "/app/main.py"]
CMD xvfb-run --server-args="-screen 0 1024x768x24" python3 /app/main.py
