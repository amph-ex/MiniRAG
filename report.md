# Лабораторная работа 20 — Сборка MiniRAG на Python

**Студент:** Artemii Subota  
**Система и версия Python:** Windows, Python 3.12.10

## 1. Цель работы

Цель лабораторной работы — изучить основные этапы создания небольшой RAG-системы (Retrieval-Augmented Generation) на Python.

В ходе работы необходимо подготовить базу знаний, разделить текст на фрагменты, создать векторные представления с помощью модели Sentence Transformers, сохранить их, реализовать семантический поиск и подготовить контекст для передачи языковой модели.

## 2. Подготовка проекта и окружения

Работа выполнялась в Windows с использованием Python 3.12.10.

Для проекта было создано виртуальное окружение `.venv`. Установлены необходимые библиотеки, включая:

- sentence-transformers
- numpy
- scikit-learn
- google-genai

Проект разделён на отдельные модули: `rag`, `llm`, `examples`, `practice`, `source` и `database`.

## 3. Проверка работы Weather API

Для проверки HTTP-запросов был создан файл `examples/e20_01_weather_api.py`.

Программа отправляет запрос к погодному API и выводит полученные данные.

Фактический результат запуска:

```text
HTTP-статус: 200
Город: Yerevan
Температура: 10 °C
Ощущается как: 8 °C
Влажность: 64 %
Погода: Overcast
```

Запрос выполнен успешно. HTTP-статус 200 означает, что сервер обработал запрос без ошибки.

## 4. Подготовка базы знаний

Для экспериментов был подготовлен исходный текст с информацией о магазине:

```text
Заказы отправляются %#$ по предоплате.
Доставка %#$ занимает 3-5 дней.
В нашем магазине %#$ предусмотрен возврат.
Адрес нашего %#$ магазина - город Берлин.
```

Исходный текст был обработан и разделён на отдельные фрагменты (chunks).

В результате было получено 4 фрагмента для дальнейшей индексации.

## 5. Создание эмбеддингов

Для преобразования текстовых фрагментов в числовые векторы использовалась библиотека Sentence Transformers.

В проекте применялась модель:

`sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`

Модель поддерживает многоязычные тексты, в том числе русский язык.

С помощью метода `model.encode()` каждый текстовый фрагмент преобразовывался в вектор.

Размерность одного вектора:

```text
(384,)
```

Это означает, что каждый фрагмент представлен 384 числовыми значениями.

## 6. Индексация и сохранение данных

После создания эмбеддингов данные были сохранены для последующего поиска.

Фактический результат:

```text
Сохранено фрагментов: 4
```

Индекс сохранялся в файле:

`database/database.txt`

Это позволяет использовать подготовленные данные без необходимости каждый раз вручную создавать базу знаний заново.

## 7. Семантический поиск

Для поиска использовались эмбеддинг пользовательского вопроса и векторные представления фрагментов базы знаний.

Сходство между векторами рассчитывалось с помощью cosine similarity.

Для получения нескольких наиболее подходящих результатов использовался параметр `top_k`.

Пример результата поиска по вопросу о доставке:

```text
2
Доставка занимает 3-5 дней | 0.876
Заказы отправляются по предоплате | 0.462
[ДЕМО без генерации]
Доставка занимает 3-5 дней
```

Первый фрагмент получил более высокий показатель сходства и был выбран как наиболее подходящий ответ.

## 8. Формирование контекста и промпта

После поиска подходящих фрагментов система формирует контекст.

Контекст содержит найденную информацию из базы знаний, которая может быть передана языковой модели.

В отдельном модуле `llm/prompt_builder.py` реализована подготовка промпта.

Промпт объединяет:

- вопрос пользователя;
- найденный контекст;
- инструкции для языковой модели.

Это позволяет ограничить ответ информацией, полученной из базы знаний.

## 9. Переменные окружения и LAB_STUDENT

Для настройки проекта использовались переменные окружения:

- `GEMINI_API_KEY` — ключ для доступа к Gemini API;
- `LAB_STUDENT` — имя студента.

Для проверки переменной `LAB_STUDENT` в PowerShell была выполнена команда:

```powershell
$env:LAB_STUDENT="Anna"
```

После этого была запущена проверка:

```powershell
& .\.venv\Scripts\python.exe -m examples.e20_12_environment
```

Фактический результат:

```text
LAB_STUDENT: Anna
```

Проверка прошла успешно: программа получила значение переменной окружения.

## 10. DEMO-режим

Для проверки работы RAG-системы без обращения к внешней языковой модели был реализован режим `demo`.

В этом режиме программа выполняет поиск по базе знаний и возвращает найденный фрагмент без генерации ответа через Gemini.

Пример результата:

```text
[ДЕМО без генерации]
Заказы отправляются по предоплате
```

При отсутствии подходящих данных в базе программа может вернуть сообщение:

```text
В базе нет ответа.
```

DEMO-режим позволяет отдельно проверить работу поиска и подготовку ответа, не завися от доступности внешнего API.

## 11. Проверка Gemini API

В проекте была реализована возможность обращения к Gemini API через библиотеку `google-genai`.

Во время проверки возникли проблемы с доступностью моделей и выполнением запросов.

Были получены следующие ошибки:

- `gemini-flash-latest` — ошибка 404;
- `gemini-3.8-flash` — ошибки 503 и 504.

Для увеличения времени ожидания HTTP-запроса тайм-аут был увеличен до 60 секунд.

Несмотря на наличие значения `GEMINI_API_KEY` в переменных окружения, успешную генерацию ответа через Gemini подтвердить не удалось.

При этом DEMO-режим работал успешно.

## 12. Проверка вопросов, на которые нет полного ответа в базе

Были рассмотрены вопросы, для которых исходная база знаний содержит недостаточно информации.

Например:

- «Сколько стоит доставка?» — в базе указана продолжительность доставки, но не её стоимость;
- «В течение какого срока можно вернуть товар?» — в базе указано наличие возврата, но не конкретный срок.

DEMO-режим возвращает найденный фрагмент, но не выполняет полноценную генерацию и не умеет самостоятельно достоверно определять все отсутствующие сведения.

Поэтому для таких вопросов найденный фрагмент не обязательно является полным ответом.

## 13. Проверка актуальности индекса

Для проверки обновления базы знаний был проведён эксперимент.

Первоначальный текст:

```text
Заказы отправляются по предоплате
```

Затем текст был изменён:

```text
Заказ можно оплатить после получения
```

До повторной индексации поиск продолжал возвращать старый фрагмент:

```text
0.789 | Заказы отправляются по предоплате
0.511 | В нашем магазине предусмотрен возврат
```

После повторной индексации результат изменился:

```text
0.813 | Заказ можно оплатить после получения
0.511 | В нашем магазине предусмотрен возврат
```

После эксперимента исходный текст был восстановлен, а индекс создан повторно.

Контрольный результат:

```text
0.789 | Заказы отправляются по предоплате
0.511 | В нашем магазине предусмотрен возврат
```

Эксперимент показал, что после изменения исходных данных необходимо повторно выполнять индексацию, иначе поиск может использовать устаревшие векторы.

## 14. Практические задания

В папке `practice` были выполнены пять дополнительных заданий:

1. Реализация функции `build_context`, которая формирует контекст из найденных фрагментов.
2. Реализация функции `build_prompt`, которая объединяет вопрос, контекст и инструкции.
3. Реализация `get_ai_response` с поддержкой DEMO-режима и обработки пустого результата.
4. Проверка поиска по вопросу о доставке с использованием нескольких результатов.
5. Подготовка промпта для вопроса «Сколько стоит доставка?» с учётом того, что в базе отсутствует информация о стоимости.

Практические задания помогли закрепить работу с функциями, списками, строками, поиском и обработкой результатов.

## 15. Ответы на контрольные вопросы

**1. Что такое RAG?**

RAG — это подход, при котором перед генерацией ответа система сначала ищет подходящую информацию во внешней базе знаний, а затем использует найденные данные для формирования ответа.

**2. Что такое эмбеддинг?**

Эмбеддинг — это числовое представление текста в виде вектора. Он позволяет сравнивать тексты по смыслу.

**3. Зачем текст разделяется на chunks?**

Разделение текста на небольшие фрагменты упрощает поиск нужной информации и позволяет передавать языковой модели только релевантные части базы знаний.

**4. Что такое семантический поиск?**

Семантический поиск позволяет находить информацию по смыслу запроса, а не только по совпадению отдельных слов.

**5. Что такое cosine similarity?**

Cosine similarity — это метрика, которая оценивает сходство двух векторов по углу между ними. Чем выше значение, тем ближе векторы по направлению.

**6. Для чего нужен параметр top_k?**

`top_k` определяет количество наиболее подходящих фрагментов, которые система должна вернуть после поиска.

**7. Зачем нужен контекст?**

Контекст содержит найденные фрагменты базы знаний, которые используются при подготовке ответа языковой модели.

**8. Почему необходимо обновлять индекс после изменения исходного текста?**

Потому что в индексе хранятся векторные представления старых фрагментов. После изменения текста необходимо создать новые эмбеддинги и обновить индекс.

**9. В чём разница между DEMO-режимом и генерацией через Gemini?**

DEMO-режим возвращает найденный фрагмент без генерации. При использовании Gemini найденный контекст передаётся языковой модели, которая формирует ответ на основе полученной информации.

## 16. Возникшие проблемы и их решение

Во время выполнения лабораторной работы возникли следующие проблемы:

- При запуске погодного примера сначала было указано неправильное имя модуля. После проверки структуры проекта использовалось правильное имя `examples.e20_01_weather_api`.
- При работе с Gemini API возникали ошибки 404, 503 и 504. Увеличение тайм-аута не позволило подтвердить успешную генерацию.
- В файле `practice/__init__.py` находился лишний код, который приводил к дополнительному выводу. Файл был исправлен.

При этом проверка переменной `LAB_STUDENT`, поиск по базе знаний и полный запуск программы в DEMO-режиме завершились успешно.

## 17. Полный запуск MiniRAG

Для проверки всей системы был выполнен запуск основного файла `main.py` из корневой папки проекта.

Команда запуска:

```powershell
& .\.venv\Scripts\python.exe main.py
```

В качестве вопроса был введён:

```text
За сколько дней доставляется заказ?
```

Фактический вывод программы:

```text
Режим: demo
Вопрос: За сколько дней доставляется заказ?
Ответ:
[ДЕМО без генерации]
Доставка занимает 3-5 дней.
```

Перед выводом программа успешно загрузила веса модели Sentence Transformers.

Полный запуск прошёл без ошибок. Система получила вопрос пользователя, выполнила семантический поиск по базе знаний и вернула подходящий фрагмент.

## 18. Заключение

В ходе лабораторной работы была создана небольшая RAG-система на Python.

Были изучены и реализованы основные этапы работы:

- подготовка исходных текстов;
- разделение текста на фрагменты;
- создание эмбеддингов;
- сохранение векторных представлений;
- семантический поиск;
- формирование контекста и промпта;
- использование переменных окружения;
- работа в DEMO-режиме;
- подготовка интеграции с Gemini API.

Удалось проверить полный запуск MiniRAG и получить ответ на пользовательский вопрос из собственной базы знаний.

Также был проведён эксперимент с обновлением индекса, который показал важность повторной индексации после изменения исходных данных.

Основной результат работы — понимание принципа построения простой RAG-системы и взаимодействия её отдельных компонентов.

---

# Laboratory Work 20 — Building MiniRAG with Python

**Student:** Artemii Subota  
**System and Python version:** Windows, Python 3.12.10

## 1. Objective

The objective of this laboratory work is to study the main stages of building a small Retrieval-Augmented Generation (RAG) system using Python.

The work includes preparing a knowledge base, splitting text into chunks, creating vector embeddings with Sentence Transformers, storing them, implementing semantic search, and preparing context for a language model.

## 2. Project and Environment Setup

The project was developed on Windows using Python 3.12.10.

A virtual environment named `.venv` was created. The required libraries were installed, including:

- sentence-transformers
- numpy
- scikit-learn
- google-genai

The project was divided into separate modules: `rag`, `llm`, `examples`, `practice`, `source`, and `database`.

## 3. Weather API Test

The file `examples/e20_01_weather_api.py` was created to test HTTP requests.

The program sends a request to a weather API and displays the returned data.

Actual output:

```text
HTTP-статус: 200
Город: Yerevan
Температура: 10 °C
Ощущается как: 8 °C
Влажность: 64 %
Погода: Overcast
```

The request was successful. HTTP status 200 indicates that the server processed the request successfully.

## 4. Knowledge Base Preparation

The following source text was prepared for the experiments:

```text
Заказы отправляются %#$ по предоплате.
Доставка %#$ занимает 3-5 дней.
В нашем магазине %#$ предусмотрен возврат.
Адрес нашего %#$ магазина - город Берлин.
```

The source text was processed and split into separate chunks.

A total of four chunks were created for further indexing.

## 5. Creating Embeddings

The Sentence Transformers library was used to convert text chunks into numerical vectors.

The model used in the project was:

`sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`

The model supports multiple languages, including Russian.

Each text chunk was converted into a vector using the `model.encode()` method.

The dimension of one vector was:

```text
(384,)
```

This means that each text chunk is represented by 384 numerical values.

## 6. Indexing and Data Storage

After creating the embeddings, the data was saved for subsequent searches.

Actual output:

```text
Сохранено фрагментов: 4
```

The index was saved in:

`database/database.txt`

This makes it possible to use the prepared data without manually rebuilding the knowledge base every time.

## 7. Semantic Search

The search process used the embedding of the user's question and the vector representations of the knowledge base chunks.

Cosine similarity was used to calculate the similarity between vectors.

The `top_k` parameter was used to retrieve several of the most relevant results.

Example search result for a delivery-related question:

```text
2
Доставка занимает 3-5 дней | 0.876
Заказы отправляются по предоплате | 0.462
[ДЕМО без генерации]
Доставка занимает 3-5 дней
```

The first chunk received a higher similarity score and was selected as the most relevant result.

## 8. Context and Prompt Construction

After retrieving relevant chunks, the system builds a context.

The context contains information retrieved from the knowledge base and can be passed to a language model.

The `llm/prompt_builder.py` module is responsible for preparing the prompt.

The prompt combines:

- the user's question;
- the retrieved context;
- instructions for the language model.

This helps restrict the answer to information obtained from the knowledge base.

## 9. Environment Variables and LAB_STUDENT

The project used the following environment variables:

- `GEMINI_API_KEY` — the key for accessing the Gemini API;
- `LAB_STUDENT` — the student's name.

The following PowerShell command was used to set `LAB_STUDENT`:

```powershell
$env:LAB_STUDENT="Anna"
```

The verification command was then executed:

```powershell
& .\.venv\Scripts\python.exe -m examples.e20_12_environment
```

Actual output:

```text
LAB_STUDENT: Anna
```

The test was successful: the Python program correctly read the environment variable.

## 10. DEMO Mode

A `demo` mode was implemented to test the RAG system without calling an external language model.

In this mode, the program searches the knowledge base and returns the retrieved chunk without generating an answer through Gemini.

Example output:

```text
[ДЕМО без генерации]
Заказы отправляются по предоплате
```

If no suitable information is found in the database, the program can return:

```text
В базе нет ответа.
```

The DEMO mode makes it possible to test retrieval and answer preparation independently of external API availability.

## 11. Gemini API Test

The project includes the possibility of calling the Gemini API using the `google-genai` library.

During testing, problems occurred with model availability and request execution.

The following errors were encountered:

- `gemini-flash-latest` — 404 error;
- `gemini-3.8-flash` — 503 and 504 errors.

The HTTP timeout was increased to 60 seconds.

Although a value was present in the `GEMINI_API_KEY` environment variable, successful response generation through Gemini could not be confirmed.

The DEMO mode worked successfully.

## 12. Questions with Missing Information

Questions requiring information that was not fully available in the knowledge base were tested.

Examples:

- "How much does delivery cost?" — the database contains the delivery time but not its price;
- "How long is the return period?" — the database mentions returns but does not specify the period.

The DEMO mode returns a retrieved chunk, but it does not perform full answer generation or independently determine all missing information.

Therefore, the retrieved chunk is not necessarily a complete answer to such questions.

## 13. Index Freshness Test

An experiment was performed to test knowledge base updates.

The original text was:

```text
Заказы отправляются по предоплате
```

It was then changed to:

```text
Заказ можно оплатить после получения
```

Before reindexing, the search continued to return the old chunk:

```text
0.789 | Заказы отправляются по предоплате
0.511 | В нашем магазине предусмотрен возврат
```

After reindexing, the result changed:

```text
0.813 | Заказ можно оплатить после получения
0.511 | В нашем магазине предусмотрен возврат
```

After the experiment, the original text was restored and the index was rebuilt.

The final result was:

```text
0.789 | Заказы отправляются по предоплате
0.511 | В нашем магазине предусмотрен возврат
```

The experiment showed that the index must be rebuilt after changes to the source data. Otherwise, the search may continue using outdated vectors.

## 14. Practical Tasks

Five additional tasks were completed in the `practice` directory:

1. Implementing `build_context` to create context from retrieved chunks.
2. Implementing `build_prompt` to combine the question, context, and instructions.
3. Implementing `get_ai_response` with DEMO mode and empty-result handling.
4. Testing delivery-related search with multiple results.
5. Preparing a prompt for the question "How much does delivery cost?" while accounting for the missing price information.

These tasks helped reinforce the use of functions, lists, strings, search, and result processing.

## 15. Answers to Review Questions

**1. What is RAG?**

RAG is an approach in which a system first searches an external knowledge base for relevant information and then uses the retrieved data to generate an answer.

**2. What is an embedding?**

An embedding is a numerical representation of text in the form of a vector. It allows texts to be compared by meaning.

**3. Why is text split into chunks?**

Splitting text into smaller chunks simplifies information retrieval and allows the language model to receive only relevant parts of the knowledge base.

**4. What is semantic search?**

Semantic search finds information based on the meaning of a query rather than only matching individual words.

**5. What is cosine similarity?**

Cosine similarity is a metric that measures the similarity of two vectors based on the angle between them. A higher value indicates greater directional similarity.

**6. What is the purpose of the `top_k` parameter?**

`top_k` determines how many of the most relevant chunks the system should return after a search.

**7. Why is context needed?**

Context contains retrieved knowledge base chunks that are used when preparing an answer with a language model.

**8. Why must the index be updated after changing the source text?**

The index stores vector representations of the previous chunks. After changing the text, new embeddings must be created and the index must be updated.

**9. What is the difference between DEMO mode and Gemini generation?**

DEMO mode returns a retrieved chunk without generating an answer. When Gemini is used, the retrieved context is passed to the language model, which generates an answer based on the provided information.

## 16. Problems Encountered and Their Resolution

The following problems occurred during the laboratory work:

- The wrong module name was initially used to run the weather example. After checking the project structure, the correct module `examples.e20_01_weather_api` was used.
- Gemini API requests returned errors 404, 503, and 504. Increasing the timeout did not confirm successful generation.
- The `practice/__init__.py` file contained extra code that caused additional output. The file was corrected.

However, the `LAB_STUDENT` test, knowledge base search, and full program execution in DEMO mode were successful.

## 17. Full MiniRAG Execution

The entire system was tested by running the main `main.py` file from the project root directory.

Run command:

```powershell
& .\.venv\Scripts\python.exe main.py
```

The following question was entered:

```text
За сколько дней доставляется заказ?
```

Actual program output:

```text
Режим: demo
Вопрос: За сколько дней доставляется заказ?
Ответ:
[ДЕМО без генерации]
Доставка занимает 3-5 дней.
```

Before displaying the result, the program successfully loaded the Sentence Transformers model weights.

The full execution completed without errors. The system received the user's question, performed semantic search in the knowledge base, and returned the relevant chunk.

## 18. Conclusion

During this laboratory work, a small RAG system was built using Python.

The following stages were studied and implemented:

- source text preparation;
- text chunking;
- embedding generation;
- vector representation storage;
- semantic search;
- context and prompt construction;
- environment variable usage;
- DEMO mode;
- preparation for Gemini API integration.

The full MiniRAG execution was successfully tested, and an answer was retrieved from the custom knowledge base.

An index update experiment was also performed, demonstrating the importance of reindexing after changes to the source data.

The main result of this work is an understanding of how to build a simple RAG system and how its individual components interact.