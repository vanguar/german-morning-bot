# lessons_b2.py
# -*- coding: utf-8 -*-

LEVEL = "B2"

# 30 полноценных уроков уровня B2 (продвинутая грамматика и академический стиль).
# Структура совместима с вашим форматтером.

LESSONS = [
    {
        "title": "B2 Урок 1: Аргументация и регистр",
        "words": [
            ["somit", "таким образом"],
            ["hingegen", "напротив"],
            ["infolgedessen", "вследствие этого"],
            ["ferner", "кроме того (форм.)"]
        ],
        "phrases": [
            ["Es lässt sich feststellen, dass ...", "Можно констатировать, что ..."],
            ["Im Folgenden wird gezeigt, dass ...", "Далее будет показано, что ..."]
        ],
        "review": [],
        "gram": {
            "rule": "Связки высокого регистра для эссе и докладов.",
            "examples": [
                ["Hingegen spricht das Ergebnis für eine andere Deutung.", "Напротив, результат говорит в пользу иного толкования."],
                ["Infolgedessen ändern wir die Methode.", "Вследствие этого мы меняем метод."]
            ]
        },
        "task": "Напишите тезис и 2 аргумента с формальными связками."
    },
    {
        "title": "B2 Урок 2: Пассив и безличные конструкции",
        "words": [
            ["es wird ...", "безличный пассив"],
            ["man", "безличное подлежащее"],
            ["es heißt, dass ...", "говорят, что ..."],
            ["es ist zu erwarten", "ожидается"]
        ],
        "phrases": [
            ["Es wird angenommen, dass ...", "Предполагается, что ..."],
            ["Man geht davon aus, dass ...", "Исходят из того, что ..."]
        ],
        "review": [],
        "gram": {
            "rule": "Безличный пассив и альтернативы с man.",
            "examples": [
                ["Es wird viel geforscht.", "Много исследуется."],
                ["Man sagt, dass die Zahlen steigen.", "Говорят, что цифры растут."]
            ]
        },
        "task": "Перепишите 4 активных предложения в безличной форме."
    },
    {
        "title": "B2 Урок 3: Номинализация",
        "words": [
            ["die Durchführung", "проведение"],
            ["die Erkenntnis", "вывод, осознание"],
            ["die Zustimmung/Ablehnung", "согласие/отказ"],
            ["die Auswirkung", "влияние, последствие"]
        ],
        "phrases": [
            ["Nach der Durchführung der Studie ...", "После проведения исследования ..."],
            ["Die Zustimmung der Teilnehmer war hoch.", "Согласие участников было высоким."]
        ],
        "review": [],
        "gram": {
            "rule": "Номинирование действий и состояний для академического стиля.",
            "examples": [
                ["Die Ablehnung führte zur Verzögerung.", "Отказ привёл к задержке."],
                ["Die Erkenntnis ist von großer Bedeutung.", "Вывод имеет большое значение."]
            ]
        },
        "task": "Преобразуйте 5 глагольных конструкций в существительные."
    },
    {
        "title": "B2 Урок 4: Partizip I/II как определение, причастные обороты",
        "words": [
            ["die beruhigende Musik", "успокаивающая музыка (Part. I)"],
            ["die gemessenen Werte", "измеренные значения (Part. II)"],
            ["die steigenden Kosten", "растущие расходы"],
            ["die gesunkene Zahl", "снизившееся число"]
        ],
        "phrases": [
            ["Die in der Studie erfassten Daten ...", "Данные, зафиксированные в исследовании, ..."],
            ["Der auf dem Tisch liegende Brief ...", "Письмо, лежащее на столе, ..."]
        ],
        "review": [],
        "gram": {
            "rule": "Атрибутивное употребление Partizip I/II; запятые при расширениях.",
            "examples": [
                ["Die schnell wachsende Stadt investiert stark.", "Быстро растущий город много инвестирует."],
                ["Die bereits erwähnten Punkte sind wichtig.", "Уже упомянутые пункты важны."]
            ]
        },
        "task": "Перепишите 4 относительных предложения через Partizip."
    },
    {
        "title": "B2 Урок 5: Косвенная речь (Konjunktiv I) — полный обзор",
        "words": [
            ["er/sie sei", "он/она (будто) есть"],
            ["er habe", "он имеет (Konj. I)"],
            ["er gehe", "он идёт (Konj. I)"],
            ["laut dem Bericht", "согласно докладу"]
        ],
        "phrases": [
            ["Der Sprecher erklärte, man sei bereit.", "Докладчик заявил, что готовы."],
            ["Die Zeitung berichtet, es gebe Mängel.", "Газета сообщает, что есть недостатки."]
        ],
        "review": [],
        "gram": {
            "rule": "Konjunktiv I для передачи чужой речи; формы sein/haben/модальные.",
            "examples": [
                ["Er sagte, sie seien angekommen.", "Он сказал, что они прибыли."],
                ["Man meldet, es gebe Verzögerungen.", "Сообщают, что есть задержки."]
            ]
        },
        "task": "Передайте 5 высказываний в косвенной речи (Konjunktiv I)."
    },
    {
        "title": "B2 Урок 6: Konjunktiv II — ирреал и условные перифразы",
        "words": [
            ["wäre/hätte", "был бы/имел бы"],
            ["würde + Inf.", "бы сделал"],
            ["hätte ... machen können", "мог бы сделать"],
            ["wäre ... geworden", "стал бы (результат)"]
        ],
        "phrases": [
            ["Hätte ich mehr Zeit, würde ich reisen.", "Если бы у меня было больше времени, я бы путешествовал."],
            ["Er hätte helfen können.", "Он мог бы помочь."]
        ],
        "review": [],
        "gram": {
            "rule": "Полные перифразы для прошедшего/настоящего ирреала.",
            "examples": [
                ["Wenn er gekommen wäre, hätten wir angefangen.", "Если бы он пришёл, мы бы начали."],
                ["Ich würde das anders machen.", "Я бы сделал иначе."]
            ]
        },
        "task": "Сформулируйте 4 условных периода с разным временем."
    },
    {
        "title": "B2 Урок 7: Инфинитивные конструкции: zu/ohne zu/anstatt zu",
        "words": [
            ["ohne ... zu", "не делая чего-то"],
            ["anstatt ... zu", "вместо того чтобы"],
            ["darauf achten, zu ...", "следить за тем, чтобы ..."],
            ["dazu neigen, zu ...", "склоняться к тому, чтобы ..."]
        ],
        "phrases": [
            ["Er ging, ohne sich zu verabschieden.", "Он ушёл, не попрощавшись."],
            ["Anstatt zu warten, rief sie an.", "Вместо ожидания она позвонила."]
        ],
        "review": [],
        "gram": {
            "rule": "Расширенные инфинитивные группы с запятой при дополнениях.",
            "examples": [
                ["Er versuchte, den Fehler zu korrigieren.", "Он попытался исправить ошибку."],
                ["Sie bat darum, früher gehen zu dürfen.", "Она попросила разрешения уйти раньше."]
            ]
        },
        "task": "Сделайте 5 предложений с разными инфинитивными группами."
    },
    {
        "title": "B2 Урок 8: Ersatzformen Passiv (lassen, bekommen/erhalten)",
        "words": [
            ["sich lassen", "можно (поддаётся)"],
            ["bekommen + Part. II", "получить (кому-то что-то сделали)"],
            ["erhalten", "получить (форм.)"],
            ["gehen + zu + Inf.", "поддаётся (книжн.)"]
        ],
        "phrases": [
            ["Das Problem lässt sich lösen.", "Проблему можно решить."],
            ["Er bekam das Auto repariert.", "Ему починили машину."]
        ],
        "review": [],
        "gram": {
            "rule": "Пассивные эквиваленты без werden/sein; стилистические различия.",
            "examples": [
                ["Die Tür geht nicht zu öffnen.", "Дверь не поддаётся открытию."],
                ["Er erhielt die Unterlagen zugesandt.", "Он получил высланные документы."]
            ]
        },
        "task": "Преобразуйте 4 предложения из активного в Ersatzpassiv."
    },
    {
        "title": "B2 Урок 9: Частицы/модальные оттенки (schon, wohl, immerhin, erst)",
        "words": [
            ["wohl", "пожалуй, вероятно"],
            ["schon", "же/уже (усиление)"],
            ["immerhin", "всё-таки"],
            ["erst", "лишь, только"]
        ],
        "phrases": [
            ["Das wird wohl stimmen.", "Это, пожалуй, верно."],
            ["Er hat immerhin versucht.", "Он всё-таки попытался."]
        ],
        "review": [],
        "gram": {
            "rule": "Смысловые оттенки и позиция частиц в заявлении/возражении.",
            "examples": [
                ["Das ist schon möglich.", "Это вполне возможно."],
                ["Ich komme erst morgen.", "Я приду только завтра."]
            ]
        },
        "task": "Перефразируйте 4 нейтральных предложения, меняя оттенки."
    },
    {
        "title": "B2 Урок 10: Словообразование (präfix/suffix)",
        "words": [
            ["-ung/-keit/-heit", "суффиксы существительных"],
            ["ver-/ent-/zer-", "приставки со значением изменения"],
            ["über-/unter-", "слишком/недостаточно"],
            ["die Umstrukturierung", "реорганизация"]
        ],
        "phrases": [
            ["die Verbesserung/Veränderung", "улучшение/изменение"],
            ["die Überforderung/Unterbewertung", "перегрузка/недооценка"]
        ],
        "review": [],
        "gram": {
            "rule": "Продуктивные модели словообразования и смысл приставок/суффиксов.",
            "examples": [
                ["die Entwicklung – entwickeln", "развитие — развивать"],
                ["die Veröffentlichung – veröffentlichen", "публикация — публиковать"]
            ]
        },
        "task": "Образуйте 8 существительных от данных глаголов/прилагательных."
    },
    {
        "title": "B2 Урок 11: Сложные относительные предложения (was/wo/worauf)",
        "words": [
            ["alles, was ...", "всё, что ..."],
            ["der Ort, wo ...", "место, где ..."],
            ["der Grund, worauf ...", "причина, на которую ..."],
            ["der Zeitpunkt, zu dem ...", "момент, когда ..."]
        ],
        "phrases": [
            ["Alles, was gesagt wurde, ist wichtig.", "Всё, что было сказано, важно."],
            ["Der Ort, wo wir uns treffen, ist zentral.", "Место, где встречаемся, центральное."]
        ],
        "review": [],
        "gram": {
            "rule": "Неформальные/устойчивые формы was/wo, формальные Präp.+Relativ.",
            "examples": [
                ["Der Grund, aus dem wir handeln, ist klar.", "Причина, по которой мы действуем, ясна."],
                ["Das ist das, worauf es ankommt.", "Это то, что имеет значение."]
            ]
        },
        "task": "Сделайте 4 сложных относительных предложения разных типов."
    },
    {
        "title": "B2 Урок 12: Satzklammer и информационная структура",
        "words": [
            ["die Satzklammer", "рамочная конструкция (часть глагола в конце)"],
            ["Vorfeld/ Mittelfeld/ Nachfeld", "поля предложения"],
            ["Thema–Rhema", "данное–новое"],
            ["Fokus", "фокус"]
        ],
        "phrases": [
            ["Im Vorfeld steht oft das Thema.", "В начале часто стоит тема."],
            ["Die wichtigen Informationen werden fokussiert.", "Важные сведения фокусируются."]
        ],
        "review": [],
        "gram": {
            "rule": "Порядок компонентов и вынос информации для акцента.",
            "examples": [
                ["Morgen werde ich den Bericht schreiben.", "Завтра я напишу отчёт."],
                ["Den Bericht werde ich morgen schreiben.", "Отчёт я напишу завтра (фокус)."]
            ]
        },
        "task": "Перестройте 4 предложения, меняя фокус и порядок."
    },
    {
        "title": "B2 Урок 13: Причинно-следственные и уступительные союзы (zumal, obgleich, sodass)",
        "words": [
                ["zumal", "тем более что"],
                ["obgleich/obschon", "хотя"],
                ["sodass", "так что (следствие)"],
                ["insofern", "в той мере (постольку)"]
        ],
        "phrases": [
            ["Er blieb zu Hause, zumal er krank war.", "Он остался дома, тем более что был болен."],
            ["Es regnete stark, sodass wir warteten.", "Сильно шёл дождь, так что мы ждали."]
        ],
        "review": [],
        "gram": {
            "rule": "Расширение набора формальных союзов и их управление порядком слов.",
            "examples": [
                ["Obgleich es spät war, arbeiteten wir weiter.", "Хотя было поздно, мы продолжали работать."],
                ["Insofern ist der Plan sinnvoll.", "В этой мере план имеет смысл."]
            ]
        },
        "task": "Сделайте 4 предложения с разными союзами из урока."
    },
    {
        "title": "B2 Урок 14: Инверсии в условных периодах (высокий стиль)",
        "words": [
            ["Hätte ich ... , so ...", "если бы я ..., то ..."],
            ["Wäre er ... , würde ...", "если бы он ..., то ..."],
            ["Sollte ... , ...", "если вдруг, ..."],
            ["so/sei es, dass ...", "так что/будь то ..."]
        ],
        "phrases": [
            ["Hätte ich Zeit, so käme ich mit.", "Имей я время, я бы пошёл с вами."],
            ["Sollte es regnen, fällt das Fest aus.", "Если вдруг пойдёт дождь, праздник отменяется."]
        ],
        "review": [],
        "gram": {
            "rule": "Инверсия без wenn: книжный стиль условных конструкций.",
            "examples": [
                ["Wäre er da, könnten wir anfangen.", "Если бы он был здесь, мы могли бы начать."],
                ["Hättest du gefragt, hättest du gewusst.", "Спросил бы — знал бы."]
            ]
        },
        "task": "Перепишите 4 периода, используя инверсию вместо wenn."
    },
    {
        "title": "B2 Урок 15: Стиль и регистры (формальный/нейтральный)",
        "words": [
            ["umgehend", "незамедлительно (форм.)"],
            ["geeignet", "подходящий (форм.)"],
            ["statt/anstatt", "вместо"],
            ["bezüglich", "касательно (форм.)"]
        ],
        "phrases": [
            ["Wir bitten um umgehende Rückmeldung.", "Просим незамедлительный ответ."],
            ["Bezüglich Ihres Schreibens vom ...", "Касательно вашего письма от ..."]
        ],
        "review": [],
        "gram": {
            "rule": "Выбор синонимов по регистру, избегание разговорных элементов в письме.",
            "examples": [
                ["geeignet für ..., nicht geeignet für ...", "подходит для ..., не подходит для ..."],
                ["statt zu warten, ...", "вместо того чтобы ждать, ..."]
            ]
        },
        "task": "Замените разговорные выражения на формальные (6 случаев)."
    },
    {
        "title": "B2 Урок 16: Академическое письмо — ввод и план",
        "words": [
            ["die Einleitung", "введение"],
            ["die Fragestellung", "исследовательский вопрос"],
            ["die Methode", "метод"],
            ["die Schlussfolgerung", "вывод"]
        ],
        "phrases": [
            ["In der Einleitung wird ... erläutert.", "Во введении поясняется ..."],
            ["Die Fragestellung lautet:", "Исследовательский вопрос звучит так:"]
        ],
        "review": [],
        "gram": {
            "rule": "Клише для структуры академического текста.",
            "examples": [
                ["Zunächst wird der Stand der Forschung skizziert.", "Сначала намечается состояние исследований."],
                ["Abschließend werden die Ergebnisse diskutiert.", "В заключение обсуждаются результаты."]
            ]
        },
        "task": "Напишите ввод (5–6 предложений) к мини-эссе."
    },
    {
        "title": "B2 Урок 17: Связность текста — референция и дейксис",
        "words": [
            ["diese/solche/jene", "эти/такие/те"],
            ["darauf/daran/damit", "на это/на том/этим"],
            ["der/die/dasjenige", "тот самый"],
            ["diesbezüglich", "в связи с этим"]
        ],
        "phrases": [
            ["Diesbezüglich ist Folgendes wichtig.", "В связи с этим важно следующее."],
            ["Darauf wird später zurückgekommen.", "К этому вернутся позже."]
        ],
        "review": [],
        "gram": {
            "rule": "Местоименные связи между предложениями.",
            "examples": [
                ["Diese Argumente sind überzeugend. Jene sind schwach.", "Эти аргументы убедительны. Те — слабые."],
                ["Darauf wird im nächsten Kapitel eingegangen.", "К этому обратятся в следующей главе."]
            ]
        },
        "task": "Свяжите 5 пар предложений деиктическими элементами."
    },
    {
        "title": "B2 Урок 18: Описание диаграмм (расширенный уровень)",
        "words": [
            ["beträchtlich/geringfügig", "значительно/незначительно"],
            ["sich stabilisieren", "стабилизироваться"],
            ["der Höchst-/Tiefstwert", "максимум/минимум"],
            ["schwanken", "колебаться"]
        ],
        "phrases": [
            ["Die Werte schwanken leicht.", "Значения слегка колеблются."],
            ["Der Höchstwert wurde im Mai erreicht.", "Максимум достигнут в мае."]
        ],
        "review": [],
        "gram": {
            "rule": "Точность формулировок и нейтральный тон описания данных.",
            "examples": [
                ["Anfangs stiegen die Zahlen beträchtlich.", "Сначала цифры значительно выросли."],
                ["Später stabilisierten sie sich.", "Позже они стабилизировались."]
            ]
        },
        "task": "Опишите сложную диаграмму (7–8 предложений) нейтральным стилем."
    },
    {
        "title": "B2 Урок 19: Дискуссия — тезис, контртезис, пример",
        "words": [
            ["der Standpunkt", "позиция"],
            ["die Entgegnung", "возражение"],
            ["die Untermauerung", "подкрепление (доказательствами)"],
            ["stichhaltig", "весомый"]
        ],
        "phrases": [
            ["Ein stichhaltiges Argument ist, dass ...", "Веский аргумент в том, что ..."],
            ["Dem lässt sich entgegnen, dass ...", "Этому можно возразить, что ..."]
        ],
        "review": [],
        "gram": {
            "rule": "Композиция абзаца дискуссии: тезис – обоснование – пример – вывод.",
            "examples": [
                ["Zum Beleg kann folgendes Beispiel dienen:", "В качестве доказательства может служить пример:"],
                ["Abschließend ist festzuhalten, dass ...", "В заключение следует отметить, что ..."]
            ]
        },
        "task": "Напишите абзац дискуссии (8 предложений) по теме дня."
    },
    {
        "title": "B2 Урок 20: Косвенная вежливость и прагматика",
        "words": [
            ["Würden Sie wohl ...", "Не могли бы вы ..."],
            ["Wären Sie so freundlich, ...", "Будьте добры, ..."],
            ["Es wäre hilfreich, wenn ...", "Было бы полезно, если ..."],
            ["Dürfte ich ...", "Могу ли я (вежливо) ..."]
        ],
        "phrases": [
            ["Wären Sie so freundlich, mir die Datei zu senden?", "Будьте добры отправить мне файл."],
            ["Dürfte ich kurz stören?", "Могу ли я на минутку отвлечь?"]
        ],
        "review": [],
        "gram": {
            "rule": "Стратегии смягчения и косвенной просьбы.",
            "examples": [
                ["Es wäre hilfreich, wenn Sie das bestätigen.", "Было бы полезно, если вы это подтвердите."],
                ["Würden Sie mir bitte sagen, ...", "Не могли бы вы сказать мне, ..."]
            ]
        },
        "task": "Перепишите 6 прямых просьб в косвенные вежливые."
    },
    {
        "title": "B2 Урок 21: Идиомы и образные выражения (уровень B2)",
        "words": [
            ["ins Schwarze treffen", "попасть в точку"],
            ["um den heißen Brei reden", "ходить вокруг да около"],
            ["etwas unter die Lupe nehmen", "взять под лупу (тщательно изучить)"],
            ["mit zweierlei Maß messen", "мерить двойным стандартом"]
        ],
        "phrases": [
            ["Damit triffst du ins Schwarze.", "Этим ты попал в точку."],
            ["Nehmen wir das genauer unter die Lupe.", "Давайте изучим это детальнее."]
        ],
        "review": [],
        "gram": {
            "rule": "Устойчивые обороты в письменной и устной аргументации.",
            "examples": [
                ["Er redet um den heißen Brei.", "Он ходит вокруг да около."],
                ["Man misst hier mit zweierlei Maß.", "Здесь мерят двойным стандартом."]
            ]
        },
        "task": "Составьте 5 предложений с идиомами по контексту."
    },
    {
        "title": "B2 Урок 22: Формальные предлоги: angesichts, hinsichtlich, mittels",
        "words": [
            ["angesichts (+Gen.)", "ввиду"],
            ["hinsichtlich (+Gen.)", "относительно"],
            ["mittels (+Gen.)", "посредством"],
            ["im Hinblick auf (+Akk.)", "с учётом, в отношении"]
        ],
        "phrases": [
            ["Angesichts der Lage ...", "Ввиду ситуации ..."],
            ["Hinsichtlich der Kosten ...", "Относительно расходов ..."]
        ],
        "review": [],
        "gram": {
            "rule": "Употребление предлогов высокого стиля с Genitiv/Akkusativ.",
            "examples": [
                ["Mittels eines Experiments wurde dies gezeigt.", "Посредством эксперимента это было показано."],
                ["Im Hinblick auf die Zukunft ...", "С учётом будущего ..."]
            ]
        },
        "task": "Сделайте 4 формальных предложения с этими предлогами."
    },
    {
        "title": "B2 Урок 23: Синонимия и нюансы: sagen/äußern/erläutern/darlegen",
        "words": [
            ["äußern", "высказывать"],
            ["erläutern", "пояснять подробно"],
            ["darlegen", "излагать"],
            ["verdeutlichen", "прояснять"]
        ],
        "phrases": [
            ["Er legte seine Position dar.", "Он изложил свою позицию."],
            ["Die Autorin erläutert den Begriff.", "Автор подробно поясняет понятие."]
        ],
        "review": [],
        "gram": {
            "rule": "Выбор глагола по жанру и степени формальности.",
            "examples": [
                ["Sie äußerte Kritik an dem Vorschlag.", "Она высказала критику предложению."],
                ["Die Grafik verdeutlicht den Trend.", "График проясняет тренд."]
            ]
        },
        "task": "Подберите по 1 контексту к каждому синониму (микро-предложения)."
    },
    {
        "title": "B2 Урок 24: Типичные ошибки русскоязычных — порядок слов",
        "words": [
            ["Verbzweit", "глагол на втором месте"],
            ["Satzklammer", "рамочная конструкция"],
            ["Endstellung", "конечная позиция"],
            ["Position 0", "позиция 0 (союзы)"]
        ],
        "phrases": [
            ["Heute habe ich leider keine Zeit.", "Сегодня у меня, к сожалению, нет времени."],
            ["Ich denke, dass er morgen kommt.", "Я думаю, что он придёт завтра."]
        ],
        "review": [],
        "gram": {
            "rule": "Типичные нарушения Verbzweit/Endstellung и их исправление.",
            "examples": [
                ["Dann habe ich das Buch gelesen.", "Потом я прочитал книгу."],
                ["..., weil ich keine Zeit habe.", "... потому что у меня нет времени."]
            ]
        },
        "task": "Исправьте порядок слов в 6 предложениях."
    },
    {
        "title": "B2 Урок 25: Работа с источниками и цитатами",
        "words": [
            ["die Quellenangabe", "ссылка на источник"],
            ["zitieren", "цитировать"],
            ["plagiieren", "плагиатить"],
            ["wörtlich/sinngemäß", "дословно/приблизительно по смыслу"]
        ],
        "phrases": [
            ["Er wird wörtlich zitiert.", "Его цитируют дословно."],
            ["Die Quelle wird angegeben.", "Источник указан."]
        ],
        "review": [],
        "gram": {
            "rule": "Ввод цитат, Konjunktiv I для передачи, оформление.",
            "examples": [
                ["Der Autor wird wie folgt zitiert: ...", "Автора цитируют следующим образом: ..."],
                ["Sinngemäß sagt der Text, dass ...", "По смыслу текст говорит, что ..."]
            ]
        },
        "task": "Перепишите 3 цитаты в косвенной речи и оформите ссылку."
    },
    {
        "title": "B2 Урок 26: Деловая корреспонденция — предложение/договор",
        "words": [
            ["das Angebot", "коммерческое предложение"],
            ["die Konditionen", "условия (сделки)"],
            ["die Frist", "срок"],
            ["die Klausel", "пункт договора"]
        ],
        "phrases": [
            ["Wir unterbreiten Ihnen folgendes Angebot.", "Предлагаем вам следующее предложение."],
            ["Die Frist läuft am ... ab.", "Срок истекает ..."]
        ],
        "review": [],
        "gram": {
            "rule": "Стандартные формулы и конструкции в деловой переписке.",
            "examples": [
                ["Die Klauseln werden wie folgt geändert.", "Пункты изменяются следующим образом."],
                ["Bitte bestätigen Sie den Eingang.", "Просим подтвердить получение."]
            ]
        },
        "task": "Составьте письмо-предложение (7–8 предложений)."
    },
    {
        "title": "B2 Урок 27: Bewerbung B2+ — мотивация и компетенции",
        "words": [
                ["die Motivation", "мотивация"],
                ["die Kompetenz", "компетенция"],
                ["die Verantwortung", "ответственность"],
                ["die Weiterentwicklung", "дальнейшее развитие"]
        ],
        "phrases": [
            ["Ich strebe eine Position an, die ...", "Я стремлюсь к позиции, которая ..."],
            ["Ich übernehme gern Verantwortung.", "Я охотно беру на себя ответственность."]
        ],
        "review": [],
        "gram": {
            "rule": "Сильные глаголы и формулы самопрезентации.",
            "examples": [
                ["Ich bringe Erfahrung in ... mit.", "Я обладаю опытом в ..."],
                ["Ich sehe meine Stärken in ...", "Мои сильные стороны в ..."]
            ]
        },
        "task": "Напишите абзац мотивации (6–7 предложений)."
    },
    {
        "title": "B2 Урок 28: Презентация — вступление и завершение",
        "words": [
            ["die Zielsetzung", "цель"],
            ["die Gliederung", "структура"],
            ["zum Schluss", "в заключение"],
            ["zusammenfassend", "подводя итог"]
        ],
        "phrases": [
            ["Zunächst stelle ich die Zielsetzung vor.", "Сначала представлю цель."],
            ["Zusammenfassend lässt sich sagen, dass ...", "Подводя итог, можно сказать, что ..."]
        ],
        "review": [],
        "gram": {
            "rule": "Открывающие/закрывающие клише, логика переходов.",
            "examples": [
                ["Im Anschluss komme ich zum zweiten Punkt.", "Затем перейду ко второму пункту."],
                ["Zum Schluss bedanke ich mich für Ihre Aufmerksamkeit.", "В конце благодарю за внимание."]
            ]
        },
        "task": "Напишите скрипт вступления и финала (по 3 предложения)."
    },
    {
        "title": "B2 Урок 29: Медиа-реплика — комментарий/критика",
        "words": [
            ["der Kommentar", "комментарий"],
            ["die Stellungnahme", "позиция/заключение"],
            ["kritisch würdigen", "критически оценивать"],
            ["die Verzerrung", "искажение"]
        ],
        "phrases": [
            ["In meinem Kommentar werde ich ...", "В своём комментарии я ..."],
            ["Der Beitrag ist kritisch zu würdigen.", "Материал следует критически оценить."]
        ],
        "review": [],
        "gram": {
            "rule": "Композиция комментария и оценочная лексика.",
            "examples": [
                ["Die Darstellung weist Verzerrungen auf.", "В изложении есть искажения."],
                ["Die Autorin legt überzeugend dar, dass ...", "Автор убедительно излагает, что ..."]
            ]
        },
        "task": "Напишите мини-комментарий (8 предложений) к новости."
    },
    {
        "title": "B2 Урок 30: Итоговый обзор — смешанные конструкции",
        "words": [
            ["die Synthese", "синтез"],
            ["die Vertiefung", "углубление"],
            ["die Überleitung", "переход"],
            ["die Schlussfolgerung", "вывод"]
        ],
        "phrases": [
            ["In der Synthese werden die Ergebnisse gebündelt.", "В синтезе результаты объединяются."],
            ["Daraus ergibt sich folgende Schlussfolgerung:", "Отсюда вытекает следующий вывод:"]
        ],
        "review": [],
        "gram": {
            "rule": "Комплексное применение конструкций уровня B2 в связном тексте.",
            "examples": [
                ["Obgleich die Daten begrenzt sind, lässt sich Folgendes feststellen.", "Хотя данные ограничены, можно установить следующее."],
                ["Sollte sich dies bestätigen, wären die Auswirkungen beträchtlich.", "Если это подтвердится, последствия были бы значительны."]
            ]
        },
        "task": "Напишите итоговое эссе (10 предложений) с 6 разными конструкциями B2."
    }
]
