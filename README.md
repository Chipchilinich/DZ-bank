# `Виджет банковских операций`

Программа создана для фильтрации и сортировки банковских счетов по дате и оплате.

## Установка:

 Клонируйте репозиторий
```
git clone https://клонировать https://github.com/Aliniss/Домашнее задание.git
```
 Запустить

## Зависимости проекта:
- The program uses the version Python 3.12.4
- black==24.4.2
- certifi==2024.7.4
- charset-normalizer==3.3.2
- click==8.1.7
- colorama==0.4.6
- coverage==7.6.0
- flake8==7.1.0
- idna==3.7
- iniconfig==2.0.0
- isort==5.13.2
- mccabe==0.7.0
- mypy==1.10.1
- mypy-extensions==1.0.0
- packaging==24.1
- pathspec==0.12.1
- platformdirs==4.2.2
- pluggy==1.5.0
- pycodestyle==2.12.0
- pyflakes==3.2.0
- pytest==8.2.2
- pytest-cov==5.0.0
- python-dotenv==1.0.1
- requests==2.32.3
- typing_extensions==4.12.2
- urllib3==2.2.2


## Функции, которые мы будем использовать в этой версии кода:
### 10.2 Содержит: 
- функции маскирования номера карты и счета, функцию преобразования даты.
### 11.1 Содержит: 
- функцию которая принимает список словарей с банковскими операциями и возвращает ID операции, в которых указана
заданная валюта, описание каждой операции.
- функцию - генератор номеров банковских карт.
### 11.2 Содержит: 
- декоратор для логирования вызова функции и записи ее результата в файл или на консоль.
### 12.1 Содержит: 
- функцию, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
- функцию, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях.
### 13.1 Содержит: 
- функцию, которая cчитывает данные о финансовых операциях из CSV файла и преобразует их в список словарей.
- функцию, которая cчитывает данные о финансовых операциях из excel файла и преобразует их в список словарей. 

## Тестирование:

.1 Запуск тестов

```
pytest
```

22 Запуск тестов с покрытием

```
pytest --cov
```
