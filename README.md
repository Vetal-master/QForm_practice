# ТЗ
Создать тестирующий модуль для модуля пористости QFORM.

# Рабочее окружение
1. Клиент SpaceClaim.
2. Интерпретатор IronPython SCDM (встроен в клиент SpaceClaim).
3. QForm Python API.
4. Библиотека pandas.

# Порядок работы.
1. Конвертировать параметры геометрии из xlsx в txt на Python для IronPython. Необходимо для генерации моделей.
т.к. ironpython не имеет библиотеки pandas. Модуль - geometry_IO.
2. Смержить содердимое подпроекта SpaceClaim через скрипт и запустить в интерпретатор IronPython.
Т.к. импортировать трудозатратно. Сложные констуркции не импортируются в IronPython SCDM. Модуль - run_merge и merged
3. Запустить подпроект QForm. Достает данные из Excel, прогоняет через QForm, записывает результаты 
в начальный Excel. Модуль - run_QForm_generator.

# Архитектура проекта 
Весь проект в директории **project**.

Имеет три подмодуля по работе с **Excel**, **QForm**, **SpaceClaim**.

## Excel
Содержит в себе функционал по работе с таблицами отдельно для геометрии и параметров QForm.

Данная реализация максимально гибкая для работы с таблицами.

Модуль - *global_excel_conf*. Содержит имена стобцов, листов и базовых сущностей. Также путь до dataset.

### geometry
Модуль - *geometry_IO*. Реализована функция по чтению параметров геометрии и конвертации данныех в txt.

В директории **configs**:

Модуль - *geometry_IO_conf*. Содержит сообщения для вывода результата работы и путь для конвертированного файла.

Модуль - *pandas_geometry_conf*. Содержит конкретирацию для работы со столбцами Excel.

### QForm
Модуль - *QForm_IO*. Реализованы функции по чтению параметров рассчета QForm и записи результатов рассчетов.

В директории **configs**:

Модуль - *QForm_IO_conf*. Содержит сообщения для вывода результата работы.

Модуль - *pandas_QForm_conf*. Содержит конкретирацию для работы со столбцами Excel.

## SpaceClaim
Данный модуль отвечает за создание моделей, а именно содержит функционал по созданию кубов, сфер и эллипсиодов.

Создание куба и эллипсоида максимально гибко. Создание сферы создано только для центра координат.

Модуль - *run_merge*. Скрипт который соединяет подпроект для вставки в интерпретатор IronPython SCDM.

Модуль - *merged* (**генерируемый модулем выше**). Все содержимое модуля нужно вставить в SC.

Директория **project** содержит весь функционал подмодуля.

Модуль - *porosity_generator*. Имеет функцию - классификатор для вырезки поры.

Модуль - *model_generator*. Содержит функцию - организатор для создания моделей. Тип подели - Куб с 2 плоскостям 
симметрии проходящие через главные оси и 1 пору в виде конкретной объемной фигуры, также в центре координат.

Модуль - *run_generator*. Функция запуска работы.

В директории **configs**:

Модуль - *geometry_generator_conf*. Содержит сообщения для вывода результата работы. И параметры базового куба.

Модуль - *import*. Содержит все необходимые библиотеки для работы. Как базовые - math, так и необходимые для
работы SC, а именно только эллипсоида.

В директории **geometry**:

Модули *SC_(имя объекта)*. Содержат функции для выдавливания и вырезания своих объектов.

Модуль *SC_utils*. Имеет функционал по визуацлизации, уделению и сохранению модели.

В директории **handlers**:

Модули *h_(имя объекта)*. Содержат функции для расчета характерных размеров своих объектов. 
И порядок обработки поры данного типа.

## QForm
Подмодуль, отвечающий за расчет требуемых параметров их ТЗ, например усилия на инструментах и средние напряжения.

Модуль - *run_generator*. Организатор подпроекта. Работает в 3 этапа:

1. Достает данные из Excel, используя соотвествующий подмодуль.
2. Запускает клиент QForm, расчитывает данные.
3. Кладет данные в соотвествующие поля в Excel.

Директория **project** содержит весь функционал подмодуля в зоне ответсвенности обработки данных.

Модуль - *experiment*. Содержит весь фунционал по обращению к клиенту QForm, а именно:

- Запуск клиента и скрипта.
- Создание привода.
- Расчет сценария.

3 части процесса одного расчета - 3 функции.

Модуль - *experiment_generator*. Функция - органищатор, доставляющая данные для расчета 1 комбинации данных.

В директории **configs**:

Модуль - *experiment_conf*. Содержит вывода результата работы генератора и путь до базового скрипта.

# Результат работы
Был разработан проект для тестирования модуля QForm, который работает на двух технлогиях - Python и IronPythonб
настроенный под работу с Excel, API SpaceClaim, API QForm, с гибкой настройкой всех сущностей
по зонам ответсенности и масштабируемой архитектурой.

Модуль - *global_conf*. Содержит общие для всех подмодулей данные - типы обрабатывемых фигур, 
также содержит абсолютные пути для QForm API и клиента QForm. Данный модуль является единственным редактируемым
для работы с сущностями вне проекта. Остальные *(имя)_conf* - конфиги для подмодулей в рамках проекта, то есть
относительные пути и локальные имена.
