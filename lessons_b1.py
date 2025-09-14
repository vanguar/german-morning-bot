# -*- coding: utf-8 -*-

LEVEL = "B1"

# Полная версия: 30 уроков уровня B1. 
# Формат совпадает с lessons.json (A1/A2):
#   title: str
#   words: list[[de, "ru (транскрипция)"]]
#   phrases: list[[de, ru]]
#   review: list[[de, ru]]
#   gram: {"rule": str, "table"?: list[list[str]], "examples"?: list[[de, ru]]}
#   task: str

LESSONS = [
    {
        "title": "B1 Урок 1: Связки и вводные слова (логика текста)",
        "words": [
            ["allerdings", "однако, правда (ал'дэр-дингс)"],
            ["eigentlich", "вообще-то (айгэнт-лихь)"],
            ["sowohl ... als auch", "как ..., так и ... (зово́ль ... альс ау́х)"],
            ["außerdem", "кроме того (а́усэр-дэм)"],
            ["dennoch", "тем не менее (де́н-нох)"],
            ["trotzdem", "несмотря на это (троц-де́м)"],
            ["zudem", "к тому же (цу-де́м)"],
            ["folglich", "следовательно (фо́льглихь)"],
        ],
        "phrases": [
            ["Ehrlich gesagt, ...", "Честно говоря, ..."],
            ["Soweit ich weiß, ...", "Насколько мне известно, ..."],
            ["Meines Erachtens ...", "По моему мнению ... (форм.)"],
            ["Zum einen ..., zum anderen ...", "С одной стороны ..., с другой стороны ..."],
            ["Im Übrigen ...", "Кроме того/впрочем ..."],
        ],
        "review": [
            ["deshalb", "поэтому"],
            ["jedoch", "однако"],
            ["inzwischen", "между тем"],
            ["somit", "таким образом"],
        ],
        "gram": {
            "rule": "Konjunktionaladverbien вызывают инверсию; вводные слова могут занимать позицию 1 и смещать сказуемое на позицию 2.",
            "table": [
                ["Vorfeld", "Linke Klammer (Verb)", "Mittelfeld", "Rechte Klammer"],
                ["Außerdem", "habe ich", "heute wenig Zeit", "—"],
                ["Dennoch", "gehe ich", "spazieren", "—"],
            ],
            "examples": [
                ["Eigentlich wollte ich kommen, aber ich war krank.", "Вообще-то я хотел прийти, но болел."],
                ["Außerdem habe ich keine Zeit.", "Кроме того, у меня нет времени."],
                ["Dennoch mache ich weiter.", "Тем не менее я продолжаю."],
            ],
        },
        "task": "Составьте 5 предложений с вводными словами и логическими связками (минимум 4 разных).",
    },
    {
        "title": "B1 Урок 2: Структура абзаца и связность",
        "words": [
            ["der Absatz", "абзац (а́п-зац)"],
            ["die Gliederung", "план/структура (гли́:дэ-рунг)"],
            ["der Übergang", "переход (ю́:бэр-ганг)"],
            ["einleiten", "вводить (а́йн-лайтэн)"],
            ["überleiten", "делать переход (ю́:бэр-лайтэн)"],
            ["abschließend", "в заключение (а́пшли:зэнт)"],
            ["zusammenfassen", "подытоживать (цу-за́мэн-фасэн)"],
            ["hervorheben", "подчёркивать (хэр-фо́р-хэбэн)"],
        ],
        "phrases": [
            ["Zum einen ..., zum anderen ...", "С одной стороны ..., с другой стороны ..."],
            ["Abschließend lässt sich sagen, dass ...", "В заключение можно сказать, что ..."],
            ["Zunächst wird ... dargestellt.", "Сначала будет представлено ..."],
            ["Im Folgenden ...", "Далее ..."],
            ["Zusammenfassend ...", "Подводя итог, ..."],
        ],
        "review": [
            ["zuerst/anschließend", "сначала/затем"],
            ["außerdem/ferner", "кроме того"],
            ["hingegen", "напротив"],
            ["dagegen", "зато, против этого"],
        ],
        "gram": {
            "rule": "Композиция абзаца: тема–разработка–пример–вывод. Инверсия после Konjunktionaladverb.",
            "examples": [
                ["Zunächst wird die Lage erklärt, anschließend folgt ein Beispiel.", "Сначала объясняется ситуация, затем следует пример."],
                ["Zusammenfassend lässt sich sagen, dass ...", "Подводя итог, можно сказать, что ..."],
            ],
        },
        "task": "Напишите абзац (6–8 предложений) с вводом, двумя переходами и выводом.",
    },
    {
        "title": "B1 Урок 3: Относительные предложения с предлогами",
        "words": [
            ["worauf", "на что (во-ра́уф)"],
            ["womit", "чем (во-ми́т)"],
            ["worüber", "о чём (во-рю́:бэ)"],
            ["an wen", "к кому (ан вэн)"],
            ["mit dem/der/den", "с которым/которой/которыми (мит)"],
            ["über den/die/das", "о котором/которой/котором (ю́бэр)"],
        ],
        "phrases": [
            ["Das ist die Frage, auf die ich keine Antwort habe.", "Это вопрос, на который у меня нет ответа."],
            ["Die Frau, mit der ich gesprochen habe, ist meine Lehrerin.", "Женщина, с которой я говорил, — моя учительница."],
            ["Das Thema, über das wir diskutieren, ist aktuell.", "Тема, о которой мы спорим, актуальна."],
        ],
        "review": [
            ["Relativpronomen", "относительное местоимение"],
            ["der/die/das", "который/ая/ое"],
            ["wo/was", "где/что (в относительных)"],
            ["Präposition", "предлог"],
        ],
        "gram": {
            "rule": "В Relativsatz предлог ставится перед относительным местоимением; возможны wo-/wor- формы для вещей/понятий.",
            "table": [
                ["Präp.", "Relativ", "Beispiel"],
                ["mit", "der/dem/den; womit", "Das Projekt, mit dem wir beginnen, ..."],
                ["über", "den/die/das; worüber", "Das Thema, worüber wir sprechen, ..."],
            ],
            "examples": [
                ["Der Mann, an den ich denke, heißt Paul.", "Мужчина, о котором я думаю, — Пауль."],
                ["Die Stadt, in der ich lebe, ist groß.", "Город, в котором я живу, большой."],
            ],
        },
        "task": "Сделайте 4 сложных предложения с относительными придаточными + предлог.",
    },
    {
        "title": "B1 Урок 4: Präteritum в рассказах",
        "words": [
            ["ging", "шёл (гинг)"],
            ["sah", "видел (за:)"],
            ["kam", "пришёл (кам)"],
            ["sagte", "сказал (за́ктэ)"],
            ["war/hatte", "был/имел (ваːр/ха́ттэ)"],
            ["stand", "стоял (штанд)"],
        ],
        "phrases": [
            ["Früher ging ich jeden Tag joggen.", "Раньше я каждый день бегал."],
            ["Dann sah ich plötzlich einen Hund.", "Потом я вдруг увидел собаку."],
            ["Es war kalt und ich hatte keine Jacke.", "Было холодно, и у меня не было куртки."],
        ],
        "review": [
            ["Perfekt/Präteritum", "перфект/претеритум"],
            ["Zeitangaben", "обозначения времени"],
            ["Erzählstil", "повествовательный стиль"],
            ["Tempuswechsel", "смена времён"],
        ],
        "gram": {
            "rule": "Präteritum часто используется в повествовании; sein/haben и частотные сильные глаголы.",
            "examples": [
                ["Er kam spät und sagte nichts.", "Он пришёл поздно и ничего не сказал."],
                ["Ich stand auf und ging hinaus.", "Я встал и вышел."],
            ],
        },
        "task": "Опишите эпизод из прошлого (6–8 предложений) в Präteritum.",
    },
    {
        "title": "B1 Урок 5: Частицы речи (doch, mal, eben, ja)",
        "words": [
            ["doch", "же (дох)"],
            ["mal", "-ка (маль)"],
            ["eben", "именно/просто (э́:бэн)"],
            ["ja", "же (я)"],
            ["schon", "уж (шон)"],
            ["wohl", "пожалуй (воль)"],
        ],
        "phrases": [
            ["Komm doch mal her!", "Подойди же-ка сюда!"],
            ["Das ist ja klar.", "Это же ясно."],
            ["Das wird schon klappen.", "Всё уж получится."],
            ["Er kommt wohl später.", "Он, пожалуй, придёт позже."],
        ],
        "review": [
            ["Modalpartikel", "модальная частица"],
            ["Höflichkeit", "вежливость"],
            ["Abschwächung", "смягчение"],
            ["Betonung", "выделение"],
        ],
        "gram": {
            "rule": "Модальные частицы меняют тон высказывания, не изменяя смысла; позиция — в Mittelfeld.",
            "examples": [
                ["Mach das Fenster doch zu!", "Да закрой же окно!"],
                ["Das war eben nicht möglich.", "Это как раз/именно было невозможно."],
            ],
        },
        "task": "Переформулируйте 6 нейтральных предложений, добавив частицы для разных оттенков.",
    },
    {
        "title": "B1 Урок 6: Косвенные вопросы",
        "words": [
            ["ob", "ли (об)"],
            ["weshalb", "почему, по какой причине (вэсха́льп)"],
            ["wieso", "почему (ви-зо́)"],
            ["worin", "в чём (во-ри́н)"],
            ["wodurch", "чем, посредством чего (во-ду́рьх)"],
            ["woran", "на чём/о чём (во-ра́н)"],
        ],
        "phrases": [
            ["Ich weiß nicht, ob er kommt.", "Я не знаю, придёт ли он."],
            ["Können Sie mir sagen, wie spät es ist?", "Скажите, пожалуйста, который час?"],
            ["Er fragte, weshalb ich gegangen sei.", "Он спросил, почему я ушёл."],
        ],
        "review": [
            ["Fragesatz", "вопросительное предложение"],
            ["Konjunktion", "союз"],
            ["Verbendstellung", "глагол в конце"],
            ["Indirekte Frage", "косвенный вопрос"],
        ],
        "gram": {
            "rule": "В косвенном вопросе порядок как в придаточном: сказуемое в конце; падеж/предлог сохраняются.",
            "examples": [
                ["Er fragt, wann der Zug abfährt.", "Он спрашивает, когда отправляется поезд."],
                ["Sag mir bitte, wo du wohnst.", "Скажи, пожалуйста, где ты живёшь."],
            ],
        },
        "task": "Преобразуйте 6 прямых вопросов в косвенные (с разными вопросительными словами).",
    },
    {
        "title": "B1 Урок 7: Склонение прилагательных — повторение",
        "words": [
            ["stark/schwach", "сильное/слабое склонение (штарк/швах)"],
            ["gemischt", "смешанное (гэ-мишт)"],
            ["ohne Artikel", "без артикля (о́нэ арти́кль)"],
            ["nach dem Artikel", "после артикля (нах дэм арти́кль)"],
            ["Endung", "окончание (э́н-дунг)"],
            ["Kasus", "падеж (ка́зус)"],
        ],
        "phrases": [
            ["ein interessantes Buch", "интересная книга"],
            ["die neuen Schuhe", "новые ботинки"],
            ["mit kaltem Wasser", "холодной водой"],
            ["ohne großes Risiko", "без большого риска"],
        ],
        "review": [
            ["Nominativ/Akkusativ", "именительный/винительный"],
            ["Dativ/Genitiv", "дательный/родительный"],
            ["bestimmt/unbestimmt", "определённый/неопределённый"],
            ["Pluralregeln", "правила множественного"],
        ],
        "gram": {
            "rule": "Повтор ключевых окончаний прилагательных по артиклю и падежу.",
            "table": [
                ["Kasus", "Best. Art.", "Unbest. Art.", "Ohne Art."],
                ["Nom. m.", "der gute Mann", "ein guter Mann", "guter Mann"],
                ["Akk. f.", "die neue Tasche", "eine neue Tasche", "neue Tasche"],
            ],
        },
        "task": "Поставьте верные окончания прилагательных в 8 примерах.",
    },
    {
        "title": "B1 Урок 8: Генитив и предлоги",
        "words": [
            ["trotz", "несмотря на (троц)"],
            ["während", "во время (вэ́:рэнт)"],
            ["wegen", "из-за (ве́:гэн)"],
            ["innerhalb/außerhalb", "внутри/вне (и́ннэр-хальп/а́усэр-хальп)"],
            ["anlässlich", "по случаю (а́н-лэс-лихь)"],
            ["seitens", "со стороны (за́йтэнс)"],
        ],
        "phrases": [
            ["Trotz des Regens gehen wir spazieren.", "Несмотря на дождь, мы идём гулять."],
            ["Während der Pause trinke ich Kaffee.", "Во время перерыва пью кофе."],
            ["Wegen der Arbeit bleibe ich zu Hause.", "Из-за работы остаюсь дома."],
        ],
        "review": [
            ["Genitiv-S", "суффикс родительного"],
            ["formell/umgangssprachlich", "формально/разг."],
            ["Präposition + Genitiv", "предлог + Genitiv"],
            ["Artikeldeklination", "склонение артикля"],
        ],
        "gram": {
            "rule": "Устойчивые предлоги с Genitiv; в разговорной речи возможен Dativ, но в письме избегать.",
            "examples": [
                ["Außerhalb der Stadt ist es ruhiger.", "За городом спокойнее."],
                ["Anlässlich des Jubiläums gab es ein Konzert.", "По случаю юбилея был концерт."],
            ],
        },
        "task": "Сделайте 6 предложений с Genitiv-предлогами (минимум 4 разных).",
    },
    {
        "title": "B1 Урок 9: Будущее и предположения (Futur I)",
        "words": [
            ["wird ... machen", "собирается сделать (вирд ... ма́хэн)"],
            ["vermutlich", "предположительно (фэр-му́т-лихь)"],
            ["wahrscheinlich", "вероятно (ва-шайн-лихь)"],
            ["bestimmt", "наверняка (бэ-штИмт)"],
            ["wohl", "пожалуй (воль)"],
            ["gleich", "скоро/вот-вот (глайхь)"],
        ],
        "phrases": [
            ["Er wird morgen kommen.", "Он придёт завтра."],
            ["Sie wird wohl krank sein.", "Наверное, она больна."],
            ["Es wird gleich regnen.", "Скоро пойдёт дождь."],
        ],
        "review": [
            ["Futur I/Präsens", "будущее/настоящее"],
            ["Vermutung", "предположение"],
            ["Abschätzung", "оценка вероятности"],
            ["Gradpartikel", "частица степени"],
        ],
        "gram": {
            "rule": "Futur I выражает будущее или предположение; модальные частицы задают степень уверенности.",
            "examples": [
                ["Er ist bestimmt schon zu Hause.", "Он наверняка уже дома."],
                ["Sie wird wohl unterwegs sein.", "Она, вероятно, в пути."],
            ],
        },
        "task": "Сформулируйте 6 предположений (о будущем и настоящем).",
    },
    {
        "title": "B1 Урок 10: Пассив (Vorgangspassiv) — повторение",
        "words": [
            ["werden + Part. II", "образование пассива (вэ́рдэн + партицип)"],
            ["von/durch", "кем/чем (фон/дýрьх)"],
            ["hergestellt", "произведён (хэр-гештэ́льт)"],
            ["geöffnet", "открыт (гэ-э́фнэт)"],
            ["gebaut", "построен (гэ-ба́ут)"],
            ["gelöst", "решён (гэ-лёст)"],
        ],
        "phrases": [
            ["Das Haus wird gebaut.", "Дом строится."],
            ["Die Tür wurde geöffnet.", "Дверь была открыта."],
            ["Das Problem wurde schnell gelöst.", "Проблема была быстро решена."],
        ],
        "review": [
            ["Vorgang/Zustand", "процесс/состояние"],
            ["Agent", "действующее лицо"],
            ["Tempus", "время"],
            ["Partizip II", "причастие II"],
        ],
        "gram": {
            "rule": "Vorgangspassiv: werden + Partizip II; агент вводится von/durch. Отличать от Zustandspassiv (sein + Part.II).",
            "examples": [
                ["Der Brief wird von ihr geschrieben.", "Письмо пишется ею."],
                ["Die Straße ist gesperrt (Zustand).", "Улица перекрыта (состояние)."],
            ],
        },
        "task": "Переделайте 6 активных предложений в пассив (2 времени).",
    },
    {
        "title": "B1 Урок 11: Каузация с lassen",
        "words": [
            ["lassen", "позволять/заставлять (ла́ссэн)"],
            ["sich lassen", "поддаваться/можно (зихь ла́ссэн)"],
            ["reparieren lassen", "починить (поручить) (рэ-па-ри́рэн ла́ссэн)"],
            ["schneiden lassen", "подстричься (шна́йдэн ла́ссэн)"],
            ["machen lassen", "сделать по поручению (ма́хэн ла́ссэн)"],
            ["nicht zu machen sein", "неподдаваемый (нихть цу́ ма́хэн зайнь)"],
        ],
        "phrases": [
            ["Ich lasse mein Fahrrad reparieren.", "Я чиню велосипед (в мастерской)."],
            ["Das Fenster lässt sich nicht öffnen.", "Окно не открывается."],
            ["Ich lasse mir die Haare schneiden.", "Я подстригаюсь."],
        ],
        "review": [
            ["Infinitivgruppe", "инфинитивная группа"],
            ["Passiversatz", "замена пассива"],
            ["Modalität", "модальность"],
            ["Reflexivität", "возвратность"],
        ],
        "gram": {
            "rule": "lassen + Infinitiv (каузация); sich lassen — пассивная возможность/неподдаваемость.",
            "examples": [
                ["Das Problem lässt sich lösen.", "Проблему можно решить."],
                ["Die Aufgabe lässt sich nicht in einer Stunde machen.", "Задание нельзя выполнить за час."],
            ],
        },
        "task": "Составьте 6 предложений с lassen (каузация/возможность).",
    },
    {
        "title": "B1 Урок 12: Konjunktiv II (вежливость и нереальность)",
        "words": [
            ["würde + Inf.", "форма вежливости/условности (вю́рдэ)"],
            ["hätte/wäre", "имел бы/был бы (хэ́ттэ/вэ́:рэ)"],
            ["könnte", "мог бы (кё́нтэ)"],
            ["möchte", "хотел бы (мё́хтэ)"],
            ["sollte", "следовало бы (зо́льтэ)"],
            ["dürfte", "можно ли (вежл.) (дю́рфтэ)"],
        ],
        "phrases": [
            ["Ich hätte gern einen Kaffee.", "Я бы хотел кофе."],
            ["Könnten Sie mir helfen?", "Не могли бы вы мне помочь?"],
            ["Ich würde das anders machen.", "Я бы сделал иначе."],
        ],
        "review": [
            ["Irrealis", "ирреальность"],
            ["Höflichkeit", "вежливость"],
            ["Bedingungssatz", "условное предложение"],
            ["würde-Form", "форма würde"],
        ],
        "gram": {
            "rule": "Konjunktiv II — вежливые просьбы и гипотетические ситуации; прошедшее: hätte/wäre + Part.II.",
            "examples": [
                ["Wenn ich Zeit hätte, würde ich reisen.", "Если бы у меня было время, я бы путешествовал."],
                ["Er könnte später kommen.", "Он мог бы прийти позже."],
            ],
        },
        "task": "Сделайте 6 вежливых просьб/гипотетических фраз (настоящее и прошедшее).",
    },
    {
        "title": "B1 Урок 13: Временные придаточные (nachdem, bevor, bis)",
        "words": [
            ["nachdem", "после того как (нах-де́м)"],
            ["bevor", "перед тем как (бэ-фо́р)"],
            ["bis", "пока/до тех пор (бис)"],
            ["sobald", "как только (зо-ба́льт)"],
            ["solange", "пока/пока что (зо-ла́нгэ)"],
            ["während", "в то время как (вэ́:рэнт)"],
        ],
        "phrases": [
            ["Nachdem ich gegessen hatte, ging ich spazieren.", "После того как поел, пошёл гулять."],
            ["Bevor du gehst, ruf mich an.", "Перед уходом позвони мне."],
            ["Warte, bis ich komme.", "Подожди, пока я приду."],
        ],
        "review": [
            ["Plusquamperfekt", "предпрошедшее"],
            ["Konjunktion", "союз"],
            ["Temporalsatz", "временное придаточное"],
            ["Verbendstellung", "глагол в конце"],
        ],
        "gram": {
            "rule": "Порядок глаголов в временных придаточных; Plusquamperfekt с nachdem.",
            "examples": [
                ["Sobald es warm wird, fahren wir ans Meer.", "Как только станет тепло, поедем на море."],
                ["Während ich koche, hört er Musik.", "Пока я готовлю, он слушает музыку."],
            ],
        },
        "task": "Составьте 6 предложений с разными временными союзами.",
    },
    {
        "title": "B1 Урок 14: Причина и следствие (da, denn, deshalb)",
        "words": [
            ["da", "так как (да)"],
            ["denn", "ибо, так как (дэнн)"],
            ["deshalb/darum", "поэтому (дэ́схальп/да́рум)"],
            ["weshalb", "почему (вэсха́льп)"],
            ["infolgedessen", "вследствие этого (ин-фо́льгэ-дэссэн)"],
            ["somit", "таким образом (зо́:мит)"],
        ],
        "phrases": [
            ["Da es regnet, bleiben wir zu Hause.", "Так как идёт дождь, остаёмся дома."],
            ["Es ist spät, deshalb fahren wir nicht.", "Поздно, поэтому не поедем."],
            ["Wir sind müde, denn wir haben viel gearbeitet.", "Мы устали, ведь много работали."],
        ],
        "review": [
            ["Hauptsatz/Verbzweit", "главное/глагол на 2 месте"],
            ["Position 0 (denn)", "без инверсии"],
            ["Konjunktionaladverb", "союз-наречие (инверсия)"],
            ["Kausalsatz", "причинное придаточное"],
        ],
        "gram": {
            "rule": "deshalb/darum/infolgedessen вызывают инверсию; denn — позиция 0; da вводит придаточное.",
            "examples": [
                ["Ich habe viel zu tun, denn morgen ist die Prüfung.", "Много дел, ведь завтра экзамен."],
                ["Er war müde, deshalb ging er früh ins Bett.", "Он устал, поэтому рано лёг спать."],
            ],
        },
        "task": "Соедините 6 пар предложений через da/denn/deshalb/infolgedessen.",
    },
    {
        "title": "B1 Урок 15: Цель (damit / um ... zu)",
        "words": [
            ["damit", "чтобы (да-ми́т)"],
            ["um ... zu", "чтобы (ум ... цу)"],
            ["Absicht", "намерение (а́п-зихт)"],
            ["Ziel", "цель (циль)"],
            ["zwecks (+Gen.)", "с целью (цвэкс)"],
            ["beabsichtigen", "намереваться (бэ-а́п-зихтигэн)"],
        ],
        "phrases": [
            ["Ich lerne Deutsch, um in Deutschland zu studieren.", "Учу немецкий, чтобы учиться в Германии."],
            ["Ich spreche laut, damit alle mich hören.", "Говорю громко, чтобы все меня слышали."],
        ],
        "review": [
            ["Gleiche/verschiedene Subjekte", "одинаковые/разные подлежащие"],
            ["zu-Infinitiv", "инфинитив с zu"],
            ["Konjunktion", "союз"],
            ["Kommasetzung", "запятые"],
        ],
        "gram": {
            "rule": "um ... zu при одном подлежащем; damit — при разном. Инфинитивная группа отделяется запятой при дополнениях.",
            "examples": [
                ["Er spart Geld, um ein Auto zu kaufen.", "Копит деньги, чтобы купить машину."],
                ["Ich öffne das Fenster, damit es kühler wird.", "Открою окно, чтобы стало прохладнее."],
            ],
        },
        "task": "Сделайте 6 предложений: 3 с um ... zu и 3 с damit.",
    },
    {
        "title": "B1 Урок 16: Условие (wenn, falls, sofern)",
        "words": [
            ["wenn", "если (вэн)"],
            ["falls", "если вдруг (фальс)"],
            ["sofern", "если только (зо-фэрн)"],
            ["vorausgesetzt, dass", "при условии, что (фо-ра́ус-гезэцт дас)"],
            ["Bedingung", "условие (бэ-ди́нгунг)"],
            ["ansonsten", "в противном случае (ан-зонстэн)"],
        ],
        "phrases": [
            ["Wenn es regnet, bleiben wir zu Hause.", "Если будет дождь, останемся дома."],
            ["Falls Sie Fragen haben, schreiben Sie uns.", "Если есть вопросы, напишите нам."],
            ["Sofern alles klappt, fahren wir morgen.", "Если всё получится, поедем завтра."],
        ],
        "review": [
            ["Konditionalsatz", "условное придаточное"],
            ["Konjunktion", "союз"],
            ["Haupt-/Nebensatz", "главное/придаточное"],
            ["Komma", "запятая"],
        ],
        "gram": {
            "rule": "Разные степени формальности/вероятности: falls — более официальный вариант; sofern — ограничивающее условие.",
            "examples": [
                ["Wenn ich Zeit habe, rufe ich dich an.", "Если будет время, позвоню."],
                ["Vorausgesetzt, dass es klappt, beginnen wir um 10 Uhr.", "При условии, что получится, начнём в 10."],
            ],
        },
        "task": "Преобразуйте 6 утверждений в условные предложения (3 уровня вероятности).",
    },
    {
        "title": "B1 Урок 17: Уступка (obwohl, trotzdem, dennoch)",
        "words": [
            ["obwohl", "хотя (об-воль)"],
            ["trotzdem", "несмотря на это (троц-дэм)"],
            ["dennoch", "тем не менее (де́н-нох)"],
            ["gleichwohl", "тем не менее (книжн.) (глайхь-во́ль)"],
            ["zugleich", "в то же время (цу-глайхь)"],
            ["wenngleich", "хотя и (вэн-глайхь)"],
        ],
        "phrases": [
            ["Obwohl es kalt ist, gehe ich schwimmen.", "Хотя холодно, иду плавать."],
            ["Es regnet, trotzdem gehen wir spazieren.", "Идёт дождь, но мы гуляем."],
            ["Er war krank, dennoch arbeitete er weiter.", "Он был болен, однако продолжал работать."],
        ],
        "review": [
            ["Konzessivsatz", "уступительное придаточное"],
            ["Inversion", "инверсия"],
            ["Gegensatz", "противопоставление"],
            ["Grad", "степень"],
        ],
        "gram": {
            "rule": "Уступительные союзы; trotzdem/dennoch/gleichwohl — Konjunktionaladverb с инверсией.",
            "examples": [
                ["Obwohl ich müde bin, lerne ich weiter.", "Хотя я устал, продолжаю учиться."],
                ["Es war spät, dennoch blieben wir.", "Было поздно, тем не менее мы остались."],
            ],
        },
        "task": "Сделайте 6 пар предложений с obwohl и trotzdem/dennoch/gleichwohl.",
    },
    {
        "title": "B1 Урок 18: Partizip II как прилагательное",
        "words": [
            ["geöffnet", "открытый (гэ-э́фнэт)"],
            ["geschlossen", "закрытый (гэ-шло́сэн)"],
            ["gestohlen", "украденный (гэ-што́:лэн)"],
            ["verloren", "потерянный (фэр-ло́:рэн)"],
            ["beschädigt", "повреждённый (бэ-ше́:дигт)"],
            ["angegeben", "указанный (а́н-гэ-гé:бэн)"],
        ],
        "phrases": [
            ["die geöffnete Tür", "открытая дверь"],
            ["das verlorene Ticket", "потерянный билет"],
            ["die beschädigten Waren", "повреждённые товары"],
        ],
        "review": [
            ["Attribut", "определение"],
            ["Deklination", "склонение"],
            ["Aspekt (abgeschlossen)", "вид (завершённость)"],
            ["Passivnähe", "близость к пассиву"],
        ],
        "gram": {
            "rule": "Partizip II как прилагательное: склоняется по правилам прилагательных; часто выражает завершённость действия.",
            "examples": [
                ["die geschnittenen Blumen", "срезанные цветы"],
                ["die geschriebene Arbeit", "написанная работа"],
            ],
        },
        "task": "Опишите 6 предметов вокруг вас с Partizip II.",
    },
    {
        "title": "B1 Урок 19: Управление глаголов с предлогами",
        "words": [
            ["warten auf (+Akk.)", "ждать (ва́ртэн ауф)"],
            ["sich erinnern an (+Akk.)", "вспоминать о (зихь э-ри́нэрн ан)"],
            ["teilnehmen an (+Dat.)", "участвовать в (та́йль-неймен ан)"],
            ["abhängen von (+Dat.)", "зависеть от (а́п-хэнген фон)"],
            ["sich freuen auf/über", "радоваться (предвк./по факту) (фро́йэн)"],
            ["sich bewerben um", "подаваться на (бэ-вэ́рбэн ум)"],
        ],
        "phrases": [
            ["Ich warte auf den Bus.", "Я жду автобус."],
            ["Er erinnert sich an die Reise.", "Он вспоминает поездку."],
            ["Wir nehmen an dem Kurs teil.", "Мы участвуем в курсе."],
        ],
        "review": [
            ["Akk./Dat.", "винительный/дательный"],
            ["Rektion", "управление"],
            ["Reflexiv", "возвратность"],
            ["Präpositionalobjekt", "предложное дополнение"],
        ],
        "gram": {
            "rule": "Частотные глаголы с фиксированными предлогами и падежом; запоминать как единицы.",
            "examples": [
                ["Es hängt von dir ab.", "Это зависит от тебя."],
                ["Ich freue mich auf den Urlaub.", "Я с нетерпением жду отпуска."],
            ],
        },
        "task": "Сделайте 8 предложений с управлением (минимум 6 разных глаголов).",
    },
    {
        "title": "B1 Урок 20: Значения приставок über-/um-",
        "words": [
            ["umfahren (trennbar)", "объехать (ум-фа́:рэн)"],
            ["umfahren (untrennbar)", "сбить/наехать (ум-фа́:рэн)"],
            ["übersetzen (trennbar)", "переправить (ю́бэр-зэ́цэн)"],
            ["übersetzen (untrennbar)", "переводить (ю́бэр-зэ́цэн)"],
            ["umstellen", "переставить/перевести (ум-штэ́ллен)"],
            ["überlaufen", "переполниться/перебежать (ю́бэр-лауфэн)"],
        ],
        "phrases": [
            ["Er fährt das Hindernis um.", "Он объезжает препятствие."],
            ["Er übersetzt den Text.", "Он переводит текст."],
            ["Wir stellen auf Winterzeit um.", "Переходим на зимнее время."],
        ],
        "review": [
            ["trennbar/untrennbar", "отделяемые/неотделяемые"],
            ["Bedeutungswechsel", "смена значения"],
            ["Aussprache", "произношение"],
            ["Kontext", "контекст"],
        ],
        "gram": {
            "rule": "Значение глагола меняется от отделяемости приставки; ударение помогает различать.",
            "examples": [
                ["Sie setzt uns mit dem Boot über.", "Она переправляет нас лодкой."],
                ["Der Fahrer hat den Pfosten umgefahren.", "Водитель снёс столб."],
            ],
        },
        "task": "Подберите правильный глагол к 6 мини-ситуациям (контекст на выбор).",
    },
    {
        "title": "B1 Урок 21: Разговорные клише",
        "words": [
            ["keine Ahnung", "без понятия (ка́йнэ а́:нунг)"],
            ["Na ja", "ну да, так себе (на я́)"],
            ["Ach so!", "вот оно что (ах зо)"],
            ["Echt jetzt?", "серьёзно? (эхт йэцт)"],
            ["Klar doch!", "ну конечно! (клар дох)"],
            ["Passt schon.", "да нормально (паст шон)"],
        ],
        "phrases": [
            ["Na ja, es geht.", "Ну так себе."],
            ["Ach so, verstehe.", "А, понятно."],
            ["Klar doch, machen wir!", "Конечно, сделаем!"],
        ],
        "review": [
            ["Register", "регистр"],
            ["Höflichkeit", "вежливость"],
            ["Intonation", "интонация"],
            ["Pragmatik", "прагматика"],
        ],
        "gram": {"rule": "Речевые клише в нейтральной/разговорной речи; учитывать регистр и ситуацию."},
        "task": "Составьте диалог (8–10 реплик) с клише из списка.",
    },
    {
        "title": "B1 Урок 22: Формальное письмо — запрос и жалоба",
        "words": [
            ["die Anfrage", "запрос (а́н-фрагэ)"],
            ["die Beschwerde", "жалоба (бэ-швэ́рдэ)"],
            ["die Rückerstattung", "возврат средств (рю́к-эршта́тунг)"],
            ["zuständig", "ответственный (цу́-штэндихь)"],
            ["die Frist", "срок (фрист)"],
            ["die Kulanz", "добрая воля (ку-ла́нц)"],
        ],
        "phrases": [
            ["Hiermit möchte ich mich beschweren, ...", "Настоящим хочу пожаловаться, ..."],
            ["Ich bitte um eine Rückerstattung.", "Прошу о возврате средств."],
            ["Könnten Sie mir bitte nähere Informationen zusenden?", "Не могли бы вы выслать подробную информацию?"],
        ],
        "review": [
            ["Anrede/Schlussformel", "обращение/завершение"],
            ["Höflichkeitsformen", "вежливые формулы"],
            ["Sachlichkeit", "деловой стиль"],
            ["Betreff", "тема письма"],
        ],
        "gram": {
            "rule": "Структура формального письма: обращение — суть — требование/просьба — заключение.",
            "examples": [
                ["Ich bedanke mich im Voraus.", "Заранее благодарю."],
                ["Ich freue mich auf Ihre Rückmeldung.", "Буду рад вашему ответу."],
            ],
        },
        "task": "Напишите жалобу (7–9 предложений) по шаблону.",
    },
    {
        "title": "B1 Урок 23: Bewerbung — резюме и сопроводительное",
        "words": [
            ["der Lebenslauf", "резюме (ле́:бэнс-лауф)"],
            ["das Anschreiben", "сопроводительное (ан-шрай́бэн)"],
            ["die Stelle", "вакансия/должность (ште́лле)"],
            ["die Tätigkeit", "деятельность (тэ́:тих-кайт)"],
            ["die Qualifikation", "квалификация (ква-ли-фи-ка-цио́н)"],
            ["die Verantwortung", "ответственность (фэ-ра́нтвортунг)"],
        ],
        "phrases": [
            ["Ich bewerbe mich um die Stelle als ...", "Подаю заявку на должность ..."],
            ["Ich verfüge über Erfahrungen in ...", "Имею опыт в ..."],
            ["Anbei sende ich Ihnen meinen Lebenslauf.", "Прилагаю резюме."],
        ],
        "review": [
            ["um (+Akk.)", "предлог управления"],
            ["Soft Skills/Hard Skills", "мягкие/жёсткие навыки"],
            ["Motivation", "мотивация"],
            ["Einladung zum Gespräch", "приглашение на интервью"],
        ],
        "gram": {
            "rule": "Глаголы и предлоги Bewerbung (sich bewerben um, über Erfahrungen verfügen).",
            "examples": [
                ["Ich freue mich auf die Einladung zum Gespräch.", "Буду рад приглашению на собеседование."],
            ],
        },
        "task": "Составьте 7–8 предложений сопроводительного письма под реальную вакансию.",
    },
    {
        "title": "B1 Урок 24: Описание графиков и статистики",
        "words": [
            ["die Grafik zeigt", "график показывает (ди́ гра́:фик цайгт)"],
            ["der Anteil", "доля (а́н-тайль)"],
            ["im Vergleich zu", "по сравнению с (им фэр-гла́йх цу)"],
            ["zunehmen/abnehmen", "увеличиваться/уменьшаться (цу́-неймэн/а́п-нэймэн)"],
            ["schwanken", "колебаться (шва́нкен)"],
            ["sich stabilisieren", "стабилизироваться (зихь шта-би-ли-зи́рэн)"],
        ],
        "phrases": [
            ["Der Anteil steigt leicht.", "Доля слегка растёт."],
            ["Im Vergleich zum Vorjahr ...", "По сравнению с прошлым годом ..."],
            ["Die Werte schwanken.", "Значения колеблются."],
        ],
        "review": [
            ["neutraler Stil", "нейтральный стиль"],
            ["Konjunktionaladverb", "союз-наречие"],
            ["Zeitachse", "ось времени"],
            ["Trend", "тренд"],
        ],
        "gram": {"rule": "Точность формулировок и нейтральный тон описания данных."},
        "task": "Опишите сложную диаграмму (7–8 предложений) нейтральным стилем.",
    },
    {
        "title": "B1 Урок 25: Выражение мнения и аргументация",
        "words": [
            ["meiner Meinung nach", "по моему мнению (ма́йна майнунг нах)"],
            ["ich bin der Ansicht, dass", "я считаю, что (их бин дэ́р а́н-зи́хт дас)"],
            ["zum Beispiel", "например (цум ба́йшпиль)"],
            ["einerseits/andererseits", "с одной/с другой стороны (а́йнэрзайтс/а́ндэрэзайтс)"],
            ["der Standpunkt", "позиция (штанд-пунк)"],
            ["der Einwand", "возражение (а́йнванд)"],
        ],
        "phrases": [
            ["Ich bin der Meinung, dass ...", "Я считаю, что ..."],
            ["Einerseits ..., andererseits ...", "С одной стороны ..., с другой стороны ..."],
            ["Ein stichhaltiges Argument ist, dass ...", "Веский аргумент в том, что ..."],
        ],
        "review": [
            ["These/Antithese", "тезис/контртезис"],
            ["Beispiel", "пример"],
            ["Schluss", "вывод"],
            ["Kohärenz", "связность"],
        ],
        "gram": {"rule": "Структуры для аргументов и контраргументов; связность и логические маркеры."},
        "task": "Напишите мини-эссе (8–9 предложений) с 1 контраргументом и выводом.",
    },
    {
        "title": "B1 Урок 26: Здоровье и система страховки",
        "words": [
            ["die Krankenversicherung", "медстраховка (кра́нкен-фэр-зИ́хэрунг)"],
            ["die Versichertenkarte", "страховая карточка (фэр-зи́хэртэн-карте)"],
            ["die Überweisung", "направление (к врачу) (ю́:бэр-вайзунг)"],
            ["das Rezept", "рецепт (мед.) (рэ-цэ́пт)"],
            ["die Untersuchung", "осмотр/обследование (унтэр-цу́хунг)"],
            ["die Vorsorge", "профилактика (фо́р-зоргэ)"],
        ],
        "phrases": [
            ["Ich brauche eine Überweisung zum Spezialisten.", "Мне нужно направление к специалисту."],
            ["Haben Sie Ihre Versichertenkarte dabei?", "У вас с собой страховая карта?"],
            ["Sie sollten viel Wasser trinken.", "Вам следует пить много воды."],
        ],
        "review": [
            ["müssen/sollen", "обязанность/совет"],
            ["Termin", "запись"],
            ["Symptom/Diagnose", "симптом/диагноз"],
            ["Rezept einlösen", "получить лекарство"],
        ],
        "gram": {"rule": "Вежливые формулы у врача; модальные глаголы müssen/sollen."},
        "task": "Составьте диалог пациент–регистратура (8 реплик).",
    },
    {
        "title": "B1 Урок 27: Путешествия и рекламация",
        "words": [
            ["die Buchung", "бронирование (бу́:хунг)"],
            ["die Beschwerde", "претензия (бэ-швэ́рдэ)"],
            ["die Erstattung", "компенсация (эр-штáтунг)"],
            ["übernachten", "ночевать (ю́:бэр-на́хтэн)"],
            ["die Unterkunft", "жильё (в поездке) (у́нтэр-кунфт)"],
            ["die Abweichung", "отклонение (а́б-вайхунг)"],
        ],
        "phrases": [
            ["Meine Buchung wurde nicht gefunden.", "Моя бронь не найдена."],
            ["Ich verlange eine Erstattung.", "Требую компенсацию."],
            ["Das Zimmer entspricht nicht der Beschreibung.", "Номер не соответствует описанию."],
        ],
        "review": [
            ["fordern/bitten", "требовать/просить"],
            ["Mängel", "недостатки"],
            ["Frist setzen", "установить срок"],
            ["Beschwerdeweg", "порядок жалобы"],
        ],
        "gram": {"rule": "Шаблоны для жалоб и требований; формальные формулы."},
        "task": "Напишите рекламацию по отелю (7–8 предложений).",
    },
    {
        "title": "B1 Урок 28: Жильё и аренда",
        "words": [
            ["die Nebenkosten", "коммунальные платежи (нэ́:бэн-костэн)"],
            ["die Kaution", "залог (кау-цио́н)"],
            ["die Kündigungsfrist", "срок уведомления (кюн-дигунгс-фрист)"],
            ["der Mietvertrag", "договор аренды (ми́:т-фэр-тра́г)"],
            ["die Warmmiete/Kaltmiete", "аренда с/без коммуналки (ва́рм-/кальт-ми́тэ)"],
            ["möbliert", "меблированный (мё-бли́рт)"],
        ],
        "phrases": [
            ["Wie hoch sind die Nebenkosten?", "Какой размер коммунальных платежей?"],
            ["Die Kaution beträgt ...", "Залог составляет ..."],
            ["Ich kündige die Wohnung fristgerecht.", "Я расторгаю договор в срок."],
        ],
        "review": [
            ["Betrag", "сумма"],
            ["Frist", "срок"],
            ["Zustand der Wohnung", "состояние квартиры"],
            ["Übergabeprotokoll", "протокол передачи"],
        ],
        "gram": {"rule": "Вопросы и формулировки при заключении Mietvertrag; управление предлогов."},
        "task": "Составьте 8 уточняющих вопросов арендодателю.",
    },
    {
        "title": "B1 Урок 29: Медиа и критическое мышление",
        "words": [
            ["die Quelle", "источник (квэ́лле)"],
            ["die Falschmeldung", "ложная новость (фальш-мэ́лдунг)"],
            ["recherchieren", "проводить поиск (рэ-шер-ши́рэн)"],
            ["überprüfen", "проверять (ю́:бэр-прю́:фэн)"],
            ["zitieren", "цитировать (ци-ти́рэн)"],
            ["verfälschen", "искажать (фэр-фэ́льшен)"],
        ],
        "phrases": [
            ["Hast du die Quelle überprüft?", "Ты проверил источник?"],
            ["Laut Bericht ...", "Согласно отчёту ..."],
            ["Der Beitrag ist kritisch zu würdigen.", "Материал следует критически оценить."],
        ],
        "review": [
            ["Konjunktiv I", "косвенная речь"],
            ["Quelle/Autor", "источник/автор"],
            ["Nachweis", "подтверждение"],
            ["Bias", "предвзятость"],
        ],
        "gram": {
            "rule": "Косвенная речь для пересказа новостей; аккуратность цитирования.",
            "examples": [
                ["Der Sprecher sagt, die Lage sei stabil.", "Спикер говорит, что ситуация стабильна."],
                ["Die Zeitung berichtet, es gebe Probleme.", "Газета сообщает, что есть проблемы."],
            ],
        },
        "task": "Сделайте 4 пересказа новости в косвенной речи и один нейтральный комментарий.",
    },
    {
        "title": "B1 Урок 30: Итог — мини‑проект",
        "words": [
            ["die Zusammenfassung", "краткое изложение (цу-за́мэн-фасунг)"],
            ["die Reflexion", "рефлексия (рэ-флек-цио́н)"],
            ["der Schwerpunkt", "акцент, фокус (швэ́р-пункт)"],
            ["die Verbesserung", "улучшение (фэр-бэ́ссэрунг)"],
            ["die Zielsetzung", "постановка цели (циль-зэ́цунг)"],
            ["die Auswertung", "обработка/оценка (данных) (а́ус-вэртунг)"],
        ],
        "phrases": [
            ["Abschließend fasse ich zusammen, ...", "В завершение я подытожу, ..."],
            ["Mein Schwerpunkt lag auf ...", "Мой акцент был на ..."],
            ["Im Projekt habe ich ... angewendet.", "В проекте я применил(а) ..."],
        ],
        "review": [
            ["Projektstruktur", "структура проекта"],
            ["Selbsteinschätzung", "самооценка"],
            ["Ausblick", "перспектива"],
            ["Transfer", "перенос знаний"],
        ],
        "gram": {
            "rule": "Повтор ключевых конструкций уровня B1 (концессивные, условные, инфинитивные группы, пассив, косвенная речь).",
            "examples": [
                ["Obwohl es schwierig war, habe ich viel gelernt.", "Хотя было сложно, я многому научился."],
                ["Ich würde gern weiter Deutsch lernen.", "Я хотел бы продолжать учить немецкий."],
            ],
        },
        "task": "Напишите резюме курса (10–12 предложений) + мини‑эссе по выбранной теме (8 предложений).",
    },
]
