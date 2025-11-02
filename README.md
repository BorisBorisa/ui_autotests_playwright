# UI Automation Playwright Tests

Этот проект реализует автоматизированные тесты
для [QA Practice E-Commerce Site](https://practice.qabrains.com/ecommerce).

## Описание

Цель этого проекта — автоматизация UI тестирования сайта электронной коммерции используемого для практики QA.
Тесты проверяют ключевые функции приложения, чтобы обеспечить его стабильность и корректность работы.
Структура проекта построена по лучшим практикам и легко поддерживается.

## Технологии

- **Python** - основной язык программирования
- **Playwright** - автоматизация UI-тестирования веб-приложений
- **Pytest** - фреймворк для написания и запуска тестов
- **Allure** - генерация детализированных отчётов о тестах
- **Pydantic** - управление настройками и загрузка тестовых данных

### Allure отчет

Результаты выполнения тестов доступны по
ссылке: [Allure report](https://borisborisa.github.io/ui_autotests_playwright/).

_Отчет содержит Playwright трассировку и видео выполнения тестов._

## Начало работы

### Клонирование репозитория

```
git clone https://github.com/BorisBorisa/ui_autotests_playwright.git
cd ui_autotests_playwright
```

### Создание виртуального окружения

#### Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Установка зависимостей

```bash
pip install -r requirements.txt
```

### Запуск тестов с генерацией отчета Allure

```bash
pytest -m "regression" --alluredir=./allure-results
```

Эта команда запустит все тесты проекта и выведет результаты в терминале.

### Просмотр отчета Allure

```bash
allure serve allure-results
```

Эта команда откроет отчет Allure в браузере по умолчанию.
