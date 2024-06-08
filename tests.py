from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг


    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    #1 Добавление книги
    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book("1984")
        assert "1984" in collector.get_books_genre().keys()

    #2 Проверка превышения длины наименования книги
    def test_add_new_book_name_length_limit(self):
        collector = BooksCollector()
        long_book_name = "а" * 42  # создаем имя книги, превышающее ограничение длины
        collector.add_new_book(long_book_name)
        assert long_book_name not in collector.get_books_genre().keys()

    #3 Тестирование установки жанра книге
    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("1984")
        collector.set_book_genre("1984", "Фантастика")
        assert collector.get_book_genre("1984") == "Фантастика"

    #4 Получение книг по жанру
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("1984")
        collector.set_book_genre("1984", "Фантастика")
        assert "1984" in collector.get_books_with_specific_genre("Фантастика")

    #5 Получение книг для детей
    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Малыш и Карлсон")
        collector.set_book_genre("Малыш и Карлсон", "Мультфильмы")
        assert "Малыш и Карлсон" in collector.get_books_for_children()

    #6 Добавление книг в избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("1984")
        collector.add_book_in_favorites("1984")
        assert "1984" in collector.get_list_of_favorites_books()

    #7 Удаление книг из Избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("1984")
        collector.add_book_in_favorites("1984")
        collector.delete_book_from_favorites("1984")
        assert "1984" not in collector.get_list_of_favorites_books()

    #8 Проверка что у книги нет жанра
    def test_new_book_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Джейн Эйр")
        assert collector.get_book_genre("Джейн Эйр") == ""

    #9 Проверка, что книги нет в списки для детей
    def test_books_with_age_rating_not_in_children_list(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Ужасы")
        assert "Гарри Поттер" not in collector.get_books_for_children()