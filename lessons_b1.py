# lessons_b1.py
# -*- coding: utf-8 -*-

LEVEL = "B1"

# 30 полноценных уроков уровня B1.
# Структура совместима с вашим lessons.json и format_lesson():
#   title: str
#   words: list[[de, ru]]
#   phrases: list[[de, ru]]
#   review: list[[de, ru]]
#   gram: {"rule": str, "table"?: list[list[str]], "examples"?: list[[de, ru]]}
#   task: str

LESSONS = [
    {
        "title": "B1 Урок 1: Связки и вводные слова (логика текста)",
        "words": [
            ["allerdings", "однако, правда"],
            ["eigentlich", "вообще-то"],
            ["sowohl ... als auch", "как ..., так и ..."],
            ["außerdem", "кроме того"]
        ],
        "phrases": [
            ["Ehrlich gesagt, ...", "Честно говоря, ..."],
            ["Soweit ich weiß, ...", "Насколько мне известно, ..."]
        ],
        "review": [],
        "gram": {
            "rule": "Позиция вводных слов в главном предложении и их влияние на инверсию.",
            "examples": [
                ["Eigentlich wollte ich kommen, aber ich war krank.", "Вообще-то я хотел прийти, но болел."],
                ["Außerdem habe ich keine Zeit.", "Кроме того, у меня нет времени."]
            ]
        },
        "task": "Составьте 4 предложения с вводными словами и логическими связками."
    },
    {
        "title": "B1 Урок 2: Структура абзаца и связность",
        "words": [
            ["der Absatz", "абзац"],
            ["die Gliederung", "план/структура"],
            ["der Übergang", "переход (между частями)"],
            ["abschließend", "в заключение"]
        ],
        "phrases": [
            ["Zum einen ..., zum anderen ...", "С одной стороны ..., с другой стороны ..."],
            ["Abschließend lässt sich sagen, dass ...", "В заключение можно сказать, что ..."]
        ],
        "review": [],
        "gram": {
            "rule": "Порядок слов в сложных предложениях при многочастных связках.",
            "examples": [
                ["Zum einen ist es teuer, zum anderen ist es praktisch.", "С одной стороны это дорого, с другой — практично."],
                ["Abschließend lässt sich sagen, dass die Lösung gut ist.", "В заключение можно сказать, что решение хорошее."]
            ]
        },
        "task": "Напишите абзац (5–6 предложений) с двумя переходами и выводом."
    },
    {
        "title": "B1 Урок 3: Относительные предложения с предлогами",
        "words": [
            ["worauf", "на что"],
            ["womit", "чем (с помощью чего)"],
            ["worüber", "о чём"],
            ["an wen", "к кому"]
        ],
        "phrases": [
            ["Das ist die Frage, auf die ich keine Antwort habe.", "Это вопрос, на который у меня нет ответа."],
            ["Die Frau, mit der ich gesprochen habe, ist meine Lehrerin.", "Женщина, с которой я говорил, — моя учительница."]
        ],
        "review": [],
        "gram": {
            "rule": "Relativsätze с предлогами: предлог ставится перед относительным местоимением.",
            "table": [
                ["auf + den -> auf den (Relativ: auf den/die/das; worauf)"],
                ["mit + dem -> mit dem (Relativ: mit dem/der; womit)"]
            ],
            "examples": [
                ["Das Thema, über das wir diskutieren, ist aktuell.", "Тема, о которой мы спорим, актуальна."],
                ["Der Mann, an den ich denke, heißt Paul.", "Мужчина, о котором я думаю, зовут Пауль."]
            ]
        },
        "task": "Сделайте 3 сложных предложения с относительными придаточными + предлог."
    },
    {
        "title": "B1 Урок 4: Präteritum в рассказах",
        "words": [
            ["ging", "шел (Prät. von gehen)"],
            ["sah", "видел (Prät. von sehen)"],
            ["kam", "пришел (Prät. von kommen)"],
            ["sagte", "сказал (Prät. von sagen)"]
        ],
        "phrases": [
            ["Früher ging ich jeden Tag joggen.", "Раньше я каждый день бегал."],
            ["Dann sah ich plötzlich einen Hund.", "Потом я вдруг увидел собаку."]
        ],
        "review": [],
        "gram": {
            "rule": "Präteritum для часто употребимых глаголов в повествовании (gehen, kommen, sein, haben, sagen, sehen).",
            "examples": [
                ["Es war kalt und ich hatte keine Jacke.", "Было холодно, и у меня не было куртки."],
                ["Er kam spät und sagte nichts.", "Он пришел поздно и ничего не сказал."]
            ]
        },
        "task": "Опишите короткий эпизод из прошлого (4–5 предложений) в Präteritum."
    },
    {
        "title": "B1 Урок 5: Частицы речи (doch, mal, eben, ja)",
        "words": [
            ["doch", "же (усиление/возражение)"],
            ["mal", "-ка (смягчение)"],
            ["eben", "просто/именно"],
            ["ja", "же (общеизвестность)"]
        ],
        "phrases": [
            ["Komm doch mal her!", "Подойди же-ка сюда!"],
            ["Das ist ja klar.", "Это же ясно."]
        ],
        "review": [],
        "gram": {
            "rule": "Модальные частицы изменяют тон высказывания, не меняя смысла.",
            "examples": [
                ["Mach das Fenster doch zu!", "Да закрой же окно!"],
                ["Das war eben nicht möglich.", "Это просто/именно было невозможно."]
            ]
        },
        "task": "Переформулируйте 4 нейтральных предложения с частицами для разных оттенков."
    },
    {
        "title": "B1 Урок 6: Косвенные вопросы",
        "words": [
            ["ob", "ли (вопрос)"],
            ["weshalb", "почему, по какой причине"],
            ["wieso", "почему"],
            ["worin", "в чём"]
        ],
        "phrases": [
            ["Ich weiß nicht, ob er kommt.", "Я не знаю, придёт ли он."],
            ["Können Sie mir sagen, wie spät es ist?", "Скажите, пожалуйста, который час?"]
        ],
        "review": [],
        "gram": {
            "rule": "В косвенном вопросе глагол уходит в конец; порядок как в придаточном.",
            "examples": [
                ["Er fragt, wann der Zug abfährt.", "Он спрашивает, когда отправляется поезд."],
                ["Sag mir bitte, wo du wohnst.", "Скажи, пожалуйста, где ты живёшь."]
            ]
        },
        "task": "Преобразуйте 4 прямых вопроса в косвенные."
    },
    {
        "title": "B1 Урок 7: Склонение прилагательных — повторение",
        "words": [
            ["stark/schwach", "сильное/слабое склонение"],
            ["nach dem Artikel", "после артикля"],
            ["ohne Artikel", "без артикля"],
            ["gemischt", "смешанное"]
        ],
        "phrases": [
            ["ein interessantes Buch", "интересная книга (с неопред. артиклем)"],
            ["die neuen Schuhe", "новые ботинки (с определ. артиклем)"]
        ],
        "review": [],
        "gram": {
            "rule": "Повтор ключевых окончаний прилагательных в разных позициях.",
            "table": [
                ["der gute Mann / ein guter Mann / guter Mann"],
                ["die neue Tasche / eine neue Tasche / neue Tasche"]
            ],
            "examples": [
                ["Ich kaufe ein günstiges Ticket.", "Я покупаю дешёвый билет."],
                ["Er sucht eine spannende Serie.", "Он ищет захватывающий сериал."]
            ]
        },
        "task": "Поставьте верные окончания прилагательных в 6 примерах."
    },
    {
        "title": "B1 Урок 8: Генитив и предлоги",
        "words": [
            ["trotz", "несмотря на (Genitiv)"],
            ["während", "во время (Genitiv)"],
            ["wegen", "из-за (Genitiv)"],
            ["innerhalb/außerhalb", "внутри/вне (Genitiv)"]
        ],
        "phrases": [
            ["Trotz des Regens gehen wir spazieren.", "Несмотря на дождь, мы идём гулять."],
            ["Während der Pause trinke ich Kaffee.", "Во время перерыва пью кофе."]
        ],
        "review": [],
        "gram": {
            "rule": "Устойчивые предлоги с Genitiv; разговорный вариант с Dativ — в речи, но избегать в письме.",
            "examples": [
                ["Wegen der Arbeit bleibe ich zu Hause.", "Из-за работы я остаюсь дома."],
                ["Außerhalb der Stadt ist es ruhiger.", "За городом спокойнее."]
            ]
        },
        "task": "Сделайте 4 предложения с Genitiv-предлогами."
    },
    {
        "title": "B1 Урок 9: Будущее и предположения (Futur I)",
        "words": [
            ["wird ... machen", "собирается сделать"],
            ["vermutlich", "предположительно"],
            ["wahrscheinlich", "вероятно"],
            ["bestimmt", "точно, наверняка"]
        ],
        "phrases": [
            ["Er wird morgen kommen.", "Он придёт завтра."],
            ["Sie wird wohl krank sein.", "Наверное, она больна."]
        ],
        "review": [],
        "gram": {
            "rule": "Futur I и оттенки вероятности в настоящем.",
            "examples": [
                ["Es wird gleich regnen.", "Скоро пойдёт дождь."],
                ["Er ist bestimmt schon zu Hause.", "Он наверняка уже дома."]
            ]
        },
        "task": "Сформулируйте 5 предположений (о будущем и настоящем)."
    },
    {
        "title": "B1 Урок 10: Пассив (Vorgangspassiv) — повторение",
        "words": [
            ["werden + Part. II", "образование пассива"],
            ["Präsens/Präteritum", "настоящее/прошедшее"],
            ["von/durch", "кем/чем (агент)"],
            ["hergestellt", "произведён"]
        ],
        "phrases": [
            ["Das Haus wird gebaut.", "Дом строится."],
            ["Die Tür wurde geöffnet.", "Дверь была открыта."]
        ],
        "review": [],
        "gram": {
            "rule": "Пассив процесса: времена Präsens/Präteritum; агент через von/durch.",
            "examples": [
                ["Der Brief wird von ihr geschrieben.", "Письмо пишется ею."],
                ["Das Problem wurde schnell gelöst.", "Проблема была быстро решена."]
            ]
        },
        "task": "Переделайте 4 активных предложения в пассив."
    },
    {
        "title": "B1 Урок 11: Каузация с lassen",
        "words": [
            ["lassen", "позволять/заставлять"],
            ["sich lassen", "можно (поддаётся)"],
            ["reparieren lassen", "починить (поручить)"],
            ["schneiden lassen", "подстричься (у парикмахера)"]
        ],
        "phrases": [
            ["Ich lasse mein Fahrrad reparieren.", "Я чиню велосипед (в мастерской)."],
            ["Das Fenster lässt sich nicht öffnen.", "Окно не открывается (не поддаётся)."]
        ],
        "review": [],
        "gram": {
            "rule": "lassen + Infinitiv (каузация); sich lassen — пассивная возможность.",
            "examples": [
                ["Ich lasse mir die Haare schneiden.", "Я подстригаюсь."],
                ["Das Problem lässt sich lösen.", "Проблему можно решить."]
            ]
        },
        "task": "Составьте 4 предложения с lassen (каузация/возможность)."
    },
    {
        "title": "B1 Урок 12: Конъюнктив II (вежливость и нереальность)",
        "words": [
            ["würde + Inf.", "конструкция вежливости/условности"],
            ["hätte/wäre", "Konjunktiv II haben/sein"],
            ["könnte", "мог бы"],
            ["möchte", "хотел бы"]
        ],
        "phrases": [
            ["Ich hätte gern einen Kaffee.", "Я бы хотел кофе."],
            ["Könnten Sie mir helfen?", "Не могли бы вы мне помочь?"]
        ],
        "review": [],
        "gram": {
            "rule": "Konjunktiv II для вежливых просьб и гипотетических ситуаций.",
            "examples": [
                ["Wenn ich Zeit hätte, würde ich reisen.", "Если бы у меня было время, я бы путешествовал."],
                ["Er könnte später kommen.", "Он мог бы прийти позже."]
            ]
        },
        "task": "Сделайте 5 вежливых просьб/гипотетических фраз."
    },
    {
        "title": "B1 Урок 13: Временные придаточные (nachdem, bevor, bis)",
        "words": [
            ["nachdem", "после того как"],
            ["bevor", "перед тем как"],
            ["bis", "пока (до тех пор)"],
            ["sobald", "как только"]
        ],
        "phrases": [
            ["Nachdem ich gegessen hatte, ging ich spazieren.", "После того как я поел, я пошёл гулять."],
            ["Bevor du gehst, ruf mich an.", "Перед уходом позвони мне."]
        ],
        "review": [],
        "gram": {
            "rule": "Порядок глаголов в временных придаточных; Perfekt/Plusquamperfekt с nachdem.",
            "examples": [
                ["Sobald es warm wird, fahren wir ans Meer.", "Как только станет тепло, поедем на море."],
                ["Warte, bis ich komme.", "Подожди, пока я приду."]
            ]
        },
        "task": "Составьте 4 предложения с разными временными союзами."
    },
    {
        "title": "B1 Урок 14: Причина и следствие (da, denn, deshalb)",
        "words": [
            ["da", "так как (в начале)"],
            ["denn", "ибо, так как (позиция 0)"],
            ["deshalb/darum", "поэтому"],
            ["weshalb", "почему (причина)"]
        ],
        "phrases": [
            ["Da es regnet, bleiben wir zu Hause.", "Так как идёт дождь, остаёмся дома."],
            ["Es ist spät, deshalb fahren wir nicht.", "Поздно, поэтому не поедем."]
        ],
        "review": [],
        "gram": {
            "rule": "Konjunktionaladverbien (deshalb, darum) вызывают инверсию; denn — позиция 0.",
            "examples": [
                ["Ich habe viel zu tun, denn morgen ist die Prüfung.", "У меня много дел, ведь завтра экзамен."],
                ["Er war müde, deshalb ging er früh ins Bett.", "Он устал, поэтому рано лёг спать."]
            ]
        },
        "task": "Соедините пары предложений через da/denn/deshalb (4 примера)."
    },
    {
        "title": "B1 Урок 15: Цель (damit / um ... zu)",
        "words": [
            ["damit", "чтобы (разные подлежащие)"],
            ["um ... zu", "чтобы (одно подлежащее)"],
            ["Ziel", "цель"],
            ["Absicht", "намерение"]
        ],
        "phrases": [
            ["Ich lerne Deutsch, um in Deutschland zu studieren.", "Я учу немецкий, чтобы учиться в Германии."],
            ["Ich spreche laut, damit alle mich hören.", "Я говорю громко, чтобы все меня слышали."]
        ],
        "review": [],
        "gram": {
            "rule": "um ... zu при одинаковом подлежащем; damit — при разном.",
            "examples": [
                ["Er spart Geld, um ein Auto zu kaufen.", "Он копит деньги, чтобы купить машину."],
                ["Ich öffne das Fenster, damit es kühler wird.", "Открою окно, чтобы стало прохладнее."]
            ]
        },
        "task": "Сделайте 4 предложения: 2 с um ... zu, 2 с damit."
    },
    {
        "title": "B1 Урок 16: Условие (wenn, falls, sofern)",
        "words": [
            ["wenn", "если (общ.)"],
            ["falls", "если вдруг (более формально)"],
            ["sofern", "если только"],
            ["Bedingung", "условие"]
        ],
        "phrases": [
            ["Wenn es regnet, bleiben wir zu Hause.", "Если будет дождь, останемся дома."],
            ["Falls Sie Fragen haben, schreiben Sie uns.", "Если у вас есть вопросы, напишите нам."]
        ],
        "review": [],
        "gram": {
            "rule": "Придаточные условия с разной степенью формальности.",
            "examples": [
                ["Sofern alles klappt, fahren wir morgen.", "Если всё получится, поедем завтра."],
                ["Wenn ich Zeit habe, rufe ich dich an.", "Если будет время, позвоню."]
            ]
        },
        "task": "Преобразуйте 4 утверждения в условные предложения."
    },
    {
        "title": "B1 Урок 17: Уступка (obwohl, trotzdem, dennoch)",
        "words": [
            ["obwohl", "хотя"],
            ["trotzdem", "несмотря на это"],
            ["dennoch", "тем не менее"],
            ["zugleich", "в то же время"]
        ],
        "phrases": [
            ["Obwohl es kalt ist, gehe ich schwimmen.", "Хотя холодно, я иду плавать."],
            ["Es regnet, trotzdem gehen wir spazieren.", "Идёт дождь, тем не менее мы гуляем."]
        ],
        "review": [],
        "gram": {
            "rule": "Уступительные союзы; trotzdem/dennoch — инверсия.",
            "examples": [
                ["Er war krank, dennoch arbeitete er weiter.", "Он был болен, однако продолжал работать."],
                ["Obwohl ich müde bin, lerne ich weiter.", "Хотя я устал, продолжаю учиться."]
            ]
        },
        "task": "Сделайте 4 пары предложений с obwohl и trotzdem/dennoch."
    },
    {
        "title": "B1 Урок 18: Partizip II как прилагательное",
        "words": [
            ["geöffnet", "открытый"],
            ["geschlossen", "закрытый"],
            ["gestohlen", "украденный"],
            ["verloren", "потерянный"]
        ],
        "phrases": [
            ["die geöffnete Tür", "открытая дверь"],
            ["das verlorene Ticket", "потерянный билет"]
        ],
        "review": [],
        "gram": {
            "rule": "Partizip II + склонение прилагательных, значение завершённости.",
            "examples": [
                ["die geschnittenen Blumen", "срезанные цветы"],
                ["die geschriebene Arbeit", "написанная работа"]
            ]
        },
        "task": "Опишите предметы вокруг вас с Partizip II (4 примера)."
    },
    {
        "title": "B1 Урок 19: Управление глаголов с предлогами",
        "words": [
            ["warten auf (+Akk.)", "ждать (кого/что)"],
            ["sich erinnern an (+Akk.)", "вспоминать о"],
            ["teilnehmen an (+Dat.)", "участвовать в"],
            ["abhängen von (+Dat.)", "зависеть от"]
        ],
        "phrases": [
            ["Ich warte auf den Bus.", "Я жду автобус."],
            ["Er erinnert sich an die Reise.", "Он вспоминает поездку."]
        ],
        "review": [],
        "gram": {
                "rule": "Частотные глаголы с фиксированными предлогами.",
                "examples": [
                    ["Wir nehmen an dem Kurs teil.", "Мы участвуем в курсе."],
                    ["Es hängt von dir ab.", "Это зависит от тебя."]
                ]
        },
        "task": "Сделайте 6 предложений с управлением (разные предлоги)."
    },
    {
        "title": "B1 Урок 20: Значения приставок über-/um-",
        "words": [
            ["umfahren (trennbar)", "объехать"],
            ["umfahren (untrennbar)", "сбить (наехать)"],
            ["übersetzen (trennbar)", "переправить (через)"],
            ["übersetzen (untrennbar)", "переводить (текст)"]
        ],
        "phrases": [
            ["Er fährt das Hindernis um.", "Он объезжает препятствие."],
            ["Er übersetzt den Text.", "Он переводит текст."]
        ],
        "review": [],
        "gram": {
            "rule": "Значение меняется в зависимости от отделяемости приставки.",
            "examples": [
                ["Sie setzt uns mit dem Boot über.", "Она переправляет нас лодкой."],
                ["Der Fahrer hat den Pfosten umgefahren.", "Водитель снёс столб."]
            ]
        },
        "task": "Подберите правильный глагол к контексту (4 мини-ситуации)."
    },
    {
        "title": "B1 Урок 21: Разговорные связки и устойчивые выражения",
        "words": [
            ["keine Ahnung", "без понятия"],
            ["Na ja", "ну да, так себе"],
            ["Ach so!", "вот оно что!"],
            ["Echt jetzt?", "серьёзно?"]
        ],
        "phrases": [
            ["Na ja, es geht.", "Ну так себе."],
            ["Ach so, verstehe.", "А, понятно."]
        ],
        "review": [],
        "gram": {
            "rule": "Речевые клише в нейтральной и разговорной речи.",
            "examples": [
                ["Keine Ahnung, was er meint.", "Понятия не имею, что он имеет в виду."],
                ["Echt jetzt? Das ist unglaublich!", "Правда? Это невероятно!"]
            ]
        },
        "task": "Составьте диалог (6–8 реплик) с клише из списка."
    },
    {
        "title": "B1 Урок 22: Формальное письмо — запрос и жалоба",
        "words": [
            ["die Anfrage", "запрос"],
            ["die Beschwerde", "жалоба"],
            ["die Rückerstattung", "возврат средств"],
            ["zuständig", "ответственный (за)"]
        ],
        "phrases": [
            ["Hiermit möchte ich mich beschweren, ...", "Настоящим хочу пожаловаться, ..."],
            ["Ich bitte um eine Rückerstattung.", "Прошу о возврате средств."]
        ],
        "review": [],
        "gram": {
            "rule": "Формулы вежливости в официальной переписке.",
            "examples": [
                ["Könnten Sie mir bitte nähere Informationen zusenden?", "Не могли бы вы выслать подробную информацию?"],
                ["Ich bedanke mich im Voraus.", "Заранее благодарю."]
            ]
        },
        "task": "Напишите короткую жалобу (6–7 предложений) по шаблону."
    },
    {
        "title": "B1 Урок 23: Bewerbung — резюме и сопроводительное",
        "words": [
            ["der Lebenslauf", "резюме"],
            ["das Anschreiben", "сопроводительное письмо"],
            ["die Stelle", "вакансия/должность"],
            ["die Tätigkeit", "деятельность"]
        ],
        "phrases": [
            ["Ich bewerbe mich um die Stelle als ...", "Подаю заявку на должность ..."],
            ["Ich verfüge über Erfahrungen in ...", "Имею опыт в ..."]
        ],
        "review": [],
        "gram": {
            "rule": "Глаголы и предлоги Bewerbung (sich bewerben um, über Erfahrungen verfügen).",
            "examples": [
                ["Anbei sende ich Ihnen meinen Lebenslauf.", "Прилагаю резюме."],
                ["Ich freue mich auf die Einladung zum Gespräch.", "Буду рад приглашению на собеседование."]
            ]
        },
        "task": "Составьте 5−6 предложений сопроводительного письма."
    },
    {
        "title": "B1 Урок 24: Описание графиков и статистики",
        "words": [
            ["die Grafik zeigt", "график показывает"],
            ["der Anteil", "доля"],
            ["im Vergleich zu", "по сравнению с"],
            ["zunehmen/abnehmen", "увеличиваться/уменьшаться"]
        ],
        "phrases": [
            ["Der Anteil steigt leicht.", "Доля слегка растёт."],
            ["Im Vergleich zum Vorjahr ...", "По сравнению с прошлым годом ..."]
        ],
        "review": [],
        "gram": {
            "rule": "Порядок слов с Konjunktionaladverbien в описании данных.",
            "examples": [
                ["Zunächst wird die Entwicklung beschrieben.", "Сначала описывается динамика."],
                ["Anschließend werden die Gründe genannt.", "Затем называются причины."]
            ]
        },
        "task": "Опишите простую диаграмму (5 предложений)."
    },
    {
        "title": "B1 Урок 25: Выражение мнения и аргументация",
        "words": [
            ["meiner Meinung nach", "по моему мнению"],
            ["ich bin der Ansicht, dass", "я считаю, что"],
            ["zum Beispiel", "например"],
            ["einerseits/andererseits", "с одной стороны/с другой стороны"]
        ],
        "phrases": [
            ["Ich bin der Meinung, dass ...", "Я считаю, что ..."],
            ["Einerseits ..., andererseits ...", "С одной стороны ..., с другой стороны ..."]
        ],
        "review": [],
        "gram": {
            "rule": "Структуры для аргументов и контраргументов.",
            "examples": [
                ["Das hat viele Vorteile, zum Beispiel ...", "У этого много преимуществ, например ..."],
                ["Andererseits gibt es Risiken.", "С другой стороны есть риски."]
            ]
        },
        "task": "Напишите мини-эссе (6–7 предложений) с 1 контраргументом."
    },
    {
        "title": "B1 Урок 26: Здоровье и система страховки",
        "words": [
            ["die Krankenversicherung", "медстраховка"],
            ["die Versichertenkarte", "страховая карточка"],
            ["die Überweisung", "направление (к врачу)"],
            ["das Rezept", "рецепт (мед.)"]
        ],
        "phrases": [
            ["Ich brauche eine Überweisung zum Spezialisten.", "Мне нужно направление к специалисту."],
            ["Haben Sie Ihre Versichertenkarte dabei?", "У вас с собой страховая карта?"]
        ],
        "review": [],
        "gram": {
            "rule": "Вежливые формулы у врача; модальные глаголы с müssen/sollen.",
            "examples": [
                ["Sie sollten viel Wasser trinken.", "Вам следует пить много воды."],
                ["Ich muss das Rezept einlösen.", "Мне нужно получить лекарство по рецепту."]
            ]
        },
        "task": "Составьте диалог пациент–регистратура (6 реплик)."
    },
    {
        "title": "B1 Урок 27: Путешествия и рекламация",
        "words": [
            ["die Buchung", "бронь"],
            ["die Beschwerde", "претензия, жалоба"],
            ["die Erstattung", "компенсация"],
            ["übernachten", "ночевать"]
        ],
        "phrases": [
            ["Meine Buchung wurde nicht gefunden.", "Моя бронь не найдена."],
            ["Ich verlange eine Erstattung.", "Требую компенсацию."]
        ],
        "review": [],
        "gram": {
                "rule": "Речевые шаблоны для жалоб и требований.",
                "examples": [
                    ["Das Zimmer entspricht nicht der Beschreibung.", "Номер не соответствует описанию."],
                    ["Ich möchte den Manager sprechen.", "Я хочу поговорить с менеджером."]
                ]
        },
        "task": "Напишите короткую рекламацию по отелю (5 предложений)."
    },
    {
        "title": "B1 Урок 28: Жильё и аренда",
        "words": [
            ["die Nebenkosten", "коммунальные платежи"],
            ["die Kaution", "залог"],
            ["die Kündigungsfrist", "срок уведомления"],
            ["der Mietvertrag", "договор аренды"]
        ],
        "phrases": [
            ["Wie hoch sind die Nebenkosten?", "Какой размер коммунальных платежей?"],
            ["Die Kaution beträgt ...", "Залог составляет ..."]
        ],
        "review": [],
        "gram": {
            "rule": "Вопросы и формулировки при заключении Mietvertrag.",
            "examples": [
                ["Ich kündige die Wohnung fristgerecht.", "Я расторгаю договор в установленный срок."],
                ["Die Wohnung ist möbliert.", "Квартира меблирована."]
            ]
        },
        "task": "Составьте список из 6 уточняющих вопросов арендодателю."
    },
    {
        "title": "B1 Урок 29: Медиа и критическое мышление",
        "words": [
            ["die Quelle", "источник"],
            ["die Falschmeldung", "ложная новость"],
            ["recherchieren", "проводить поиск/проверку"],
            ["überprüfen", "проверять"]
        ],
        "phrases": [
            ["Hast du die Quelle überprüft?", "Ты проверил источник?"],
            ["Laut Bericht ...", "Согласно отчёту ..."]
        ],
        "review": [],
        "gram": {
            "rule": "Косвенная речь для пересказа новостей; Konjunktiv I в простом виде.",
            "examples": [
                ["Der Sprecher sagt, die Lage sei stabil.", "Спикер говорит, что ситуация стабильна."],
                ["Die Zeitung berichtet, es gebe Probleme.", "Газета сообщает, что есть проблемы."]
            ]
        },
        "task": "Сделайте 3 перефраза новости в косвенной речи."
    },
    {
        "title": "B1 Урок 30: Итог — мини-проект",
        "words": [
            ["die Zusammenfassung", "краткое изложение"],
            ["die Reflexion", "рефлексия, оценка"],
            ["der Schwerpunkt", "акцент, фокус"],
            ["die Verbesserung", "улучшение"]
        ],
        "phrases": [
            ["Abschließend fasse ich zusammen, ...", "В завершение я подытожу, ..."],
            ["Mein Schwerpunkt lag auf ...", "Мой акцент был на ..."]
        ],
        "review": [],
        "gram": {
            "rule": "Повтор ключевых конструкций уровня B1.",
            "examples": [
                ["Obwohl es schwierig war, habe ich viel gelernt.", "Хотя было сложно, я многому научился."],
                ["Ich würde gern weiter Deutsch lernen.", "Я хотел бы продолжать изучать немецкий."]
            ]
        },
        "task": "Напишите краткое резюме курса (8–10 предложений) с примерами конструкций."
    }
]
