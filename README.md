Unit-тестирование
Ниже приведен список тестов, которые были осуществлены в tests.py
Тесты покрывают всю функциональность кода из main.py


### Описание тестов

1. **Добавление книг:**
    - `test_add_new_book_add_two_books`: Проверяет корректное добавление двух книг в коллекцию.
    - `test_add_new_book_without_genre_add_one_book`: Проверяет добавление книги без жанра.
    - `test_add_new_book_name_more_40_add_no_book`: Проверяет, что книга не добавляется, если её название более 40 символов.
    - `test_add_new_book_name_40_add_one_book`: Проверяет корректное добавление книги с названием, длина которого 40 символов.
    - `test_add_new_book_name_39_add_one_book`: Проверяет корректное добавление книги с названием, длина которого 39 символов.
    - `test_the_same_book_copy_is_not_added`: Проверяет, что копии книги не добавляются в коллекцию.
    - `test_the_triple_book_copy_is_not_added`: Проверяет, что три копии книги не добавляются в коллекцию.

2. **Установка жанра для книг:**
    - `test_set_book_genre_name_genre_in_books_genre`: Проверяет установку жанра для книги и его корректное отображение.
    - `test_set_book_genre_name_not_added_zero`: Проверяет, что при установке жанра для несуществующей книги ничего не добавляется.
    - `test_set_book_genre_is_not_existed_none`: Проверяет, что при установке жанра для несуществующей книги ничего не добавляется.

3. **Получение книг по жанру:**
    - `test_get_books_with_specific_genre_valid_genre`: Проверяет получение книг с заданным жанром.
    - `test_get_books_with_specific_genre_genre_not_found`: Проверяет получение пустого списка при запросе книг с несуществующим жанром.
    - `test_get_books_with_specific_genre_invalid_genre`: Проверяет получение пустого списка при запросе книг с некорректным жанром.

4. **Получение информации о книгах и жанрах:**
    - `test_get_books_genre_by_name_genre`: Проверяет корректное получение информации о книгах и их жанрах.
    - `test_get_books_genre_with_no_data_empty`: Проверяет получение пустого словаря при отсутствии данных.
    - `test_get_books_genre_by_name_no_genre`: Проверяет корректное получение информации о книгах без установленных жанров.

5. **Фильтрация книг для детей:**
    - `test_get_books_for_children_adult_genre_empty`: Проверяет получение пустого списка при наличии взрослого жанра.
    - `test_get_books_for_children_genre_for_children_empty`: Проверяет корректное получение списка книг для детей.

6. **Добавление в избранное и удаление из избранного:**
    - `test_add_book_in_favorites_only_one_one_book_added`: Проверяет корректное добавление книги в избранное.
    - `test_add_book_in_favorites_add_existed_no_book_added`: Проверяет, что добавление существующей книги в избранное не приводит к добавлению дубликата.
    - `test_delete_book_from_favorites_delete_all_empty_list`: Проверяет корректное удаление всех книг из избранного.
    - `test_get_list_of_favorites_books_with_no_data_empty_list`: Проверяет получение пустого списка избранных книг без данных.
    - `test_get_list_of_favorites_books_with_data_list_of_favourite`: Проверяет корректное получение списка избранных книг с данными.

7. **Примечание:**
    - Все тесты создают экземпляр `BooksCollector` перед выполнением операций, чтобы начать с чистого состояния.
