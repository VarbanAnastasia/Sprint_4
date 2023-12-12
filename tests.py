from main import BooksCollector

# не 9-10 конечно, но мне очень захотелось отработать эту тему

class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.books_genre) == 2

    def test_add_new_book_without_genre_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Eat.Pray.Love')
        assert len(collector.books_genre) == 1


    def test_add_new_book_name_more_40_add_no_book(self):
        collector = BooksCollector()
        name = 'SoLongNameOfTheFilmItShouldBeMoreThan40Symbols'
        collector.add_new_book(name)
        assert len(collector.books_genre) == 0

    def test_add_new_book_name_40_add_one_book(self):
        collector = BooksCollector()
        name = 'SoLongNameOfTheFilmItShouldBe40Symbolsss'
        collector.add_new_book(name)
        collector.add_new_book(name)
        assert len(collector.books_genre) == 1

    def test_add_new_book_name_39_add_one_book(self):
        collector = BooksCollector()
        name = 'SoLongNameOfTheFilmItShouldBe40Symbols'
        collector.add_new_book(name)
        collector.add_new_book(name)
        assert len(collector.books_genre) == 1

    def test_the_same_book_copy_is_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.books_genre) == 1

    def test_the_triple_book_copy_is_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.books_genre) == 1

    def test_set_book_genre_name_genre_in_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_set_book_genre_name_not_added_zero(self):
        collector = BooksCollector()
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert len(collector.books_genre) == 0

    def test_set_book_genre_is_not_existed_none(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Драма')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    def test_get_books_with_specific_genre_valid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость')
        collector.add_new_book('Eat.Pray.Love')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Гордость', 'Ужасы')
        collector.set_book_genre('Eat.Pray.Love', 'Фантастика')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Гордость и предубеждение и зомби', 'Гордость']

    def test_get_books_with_specific_genre_genre_not_found(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость')
        collector.add_new_book('Eat.Pray.Love')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Гордость', 'Ужасы')
        collector.set_book_genre('Eat.Pray.Love', 'Фантастика')
        assert collector.get_books_with_specific_genre('Детектив') == []

    def test_get_books_with_specific_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Гордость', 'Ужасы')

        assert collector.get_books_with_specific_genre('Драмкомедия') == []

    def test_get_books_genre_by_name_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Гордость', 'Ужасы')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': 'Ужасы', 'Гордость': 'Ужасы'}

    def test_get_books_genre_with_no_data_empty(self):
        collector = BooksCollector()

        assert collector.get_books_genre() == {}

    def test_get_books_genre_by_name_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость')

        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': '', 'Гордость': ''}

    def test_get_books_for_children_adult_genre_empty(self):
        collector = BooksCollector()
        collector.add_new_book('The little prince')
        collector.set_book_genre('The little prince', 'Ужасы')
        assert collector.get_books_for_children() == []

    def test_get_books_for_children_genre_for_children_empty(self):
        collector = BooksCollector()
        collector.add_new_book('The little prince')
        collector.set_book_genre('The little prince', 'Фантастика')
        assert collector.get_books_for_children() == ['The little prince']

    def test_add_book_in_favorites_only_one_one_book_added(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

    def test_add_book_in_favorites_add_existed_no_book_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_delete_all_empty_list(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_with_no_data_empty_list(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_with_data_list_of_favourite(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби', 'Гордость']













