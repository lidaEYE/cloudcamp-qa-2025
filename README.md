## Тестовое задание QA Cloud Camp 

**Выполнила:**
Глазикова Лидия  
+79261474717  
l.glazikova@gmail.com  

**Структура проекта**
```
├── py-task.py                  - программа на Python 
├── tests\example.spec.js       - автотест на Playwright           
└── README.md                   - README файл
```
**Оглавление:**  
[Задание 1. Python](#задание-1)  
[Задание 2. Автотест на Playwright](#задание-2)  
[Библиотеки и инструменты](#библиотеки-и-инструменты)  

### Задание 1
Программа на Python читает список чисел, а затем выводит только четные, максимальное и минимальное числа, а также сортирует числа в порядке возрастания.

#### Инструкция по запуску
1. Склонируйте к себе репозиторий, в котором хранится проект тестового задания, через выполнение команды в терминале  
    ```  
    git clone https://github.com/lidaEYE/cloudcamp-qa-2025.git 
    ```  
    Или скачайте zip-архив по [ссылке](https://github.com/lidaEYE/cloudcamp-qa-2025/archive/refs/heads/main.zip) и распакуйте его

2. Убедитесь, что на вашем компьютере установлен Python. В командной строке/терминале выполните команду
    ```  
    python -v  
    ```  
    Если он не установлен, то установите с официального сайта Python, выбрав подходящую версию для вашей операционной системы, и пройдите шаг сначала. В процессе установки обязательно поставьте галочку в чекбоксе "Add python.exe to PATH"  
  
3. Через командную строку/терминал перейдите в корневую директорию проекта, выполнив команду
    ```  
    cd /здесь укажите путь до директории с проектом  
    ```

4. Запустите программу командой
    ```  
    python py-task.py  
    ```


### Задание 2
Автотест на Playwright. Скрипт открывает веб-страницу https://example.com, проверяет, что заголовок содержит слово "Example". Затем находит элемент с текстом "More information" и кликает по нему. После клика происходит проверка, что произошёл переход на страницу с URL https://www.iana.org/help/example-domains.

#### Инструкция по запуску
1. Склонируйте к себе репозиторий, в котором хранится проект тестового задания, через выполнение команды в терминале    
    ```  
    git clone https://github.com/lidaEYE/cloudcamp-qa-2025.git 
    ```  
    Или скачайте zip-архив по [ссылке](https://github.com/lidaEYE/cloudcamp-qa-2025/archive/refs/heads/main.zip) и распакуйте его  

2. Убедитесь, что на вашем компьютере установлен Node.js. В командной строке/терминале выполните команду  
    ```  
   node -v
   npm -v 
    ```    
   Если Node.js не установлен — загрузите и установите его с официального сайта: https://nodejs.org/

1. Через командную строку/терминал перейдите в корневую директорию проекта, выполнив команду  
   ```  
   cd /здесь укажите путь до директории с проектом  
   ```
2. Установите необходимые зависимости из файла `package.json`, выполнив команду    
   ```  
   npm install 
   ```  
3. Запустите тесты, выполнив команду    
   ```  
   npx playwright test
   ```  

### Библиотеки и инструменты
- Python - 3.11.9
- playwright/test - 1.52.0
- types/node - 22.15.18
- npm - 10.9.2