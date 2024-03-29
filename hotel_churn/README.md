# Прогнозирование оттока клиентов в сети отелей «Как в гостях»
**Описание проекта**<br>
`Заказчик этого исследования` — сеть отелей «Как в гостях».<br>
Чтобы привлечь клиентов, эта сеть отелей добавила на свой сайт возможность забронировать номер без предоплаты.<br>
Однако если клиент отменял бронирование, то компания терпела убытки.<br>
Чтобы решить эту проблему, нужно разработать систему, которая предсказывает отказ от брони.<br>
Если модель покажет, что бронь будет отменена, то клиенту предлагается внести депозит. Размер депозита — 80% от стоимости номера за одни сутки и затрат на разовую уборку.<br>

**Общий вывод:**
По результатам работы была построена модель по определению отказа от брони. Тип модели - `RandomForestClassifier`.<br>
Модель позволяет отелю увеличить прибыль даже с учетом расходов на создание модели.<br>

- Прибыль без модели: 32128090.0
- Бюджет модели: 400000.0
- Выигрыш в прибыли от модели 13505968.0

**Чаще всего отказывались от брони клиенты со следующими признаками:**
- время года summer (месяца: июнь, июль, август).
- тип заказчиков Transient-Party.
- количестве ночей - 1.
- тип номера Е.
- опции HB.
- канал дистрибуции Direct.
- тип заказчика Transient-Party.
- страны GBR, FRA.

Статус проекта:завершен.
