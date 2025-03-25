import unittest
from book import Book
from library import Library

class TestLibrary(unittest.TestCase):  # ✅ מחלקת הבדיקות יורשת מ-unittest.TestCase
    def test_add_book(self):
        library = Library()
        book = Book("The Great Gatsby", "F. Scott Fitzgerald")
        library.add_book(book)
        self.assertIn(book, library.books, "הספר לא נוסף כראוי לספרייה")
    def test_add_user(self):
        library=library()
        user=user()
        library.add_user(user)
        self.assertIn(user,)
    def test_add_user(self):
        library = Library()  # יצירת אובייקט ספרייה
        user = "JohnDoe"  # דוגמת שם משתמש
        library.add_user(user)  # הוספת המשתמש
        self.assertIn(user, library.users, "המשתמש לא נוסף כראוי לספרייה")  # בדיקה אם המשתמש הוסף בהצלחה

        with self.assertRaises(ValueError):  # בדיקה על מצב בו השם ריק
            library.add_user("")  # מנסה להוסיף שם משתמש ריק

    def test_check_out_book(self):
        library = Library()  # יצירת אובייקט ספרייה
        book = Book("The Great Gatsby", "F. Scott Fitzgerald")  # יצירת אובייקט ספר
        library.add_book(book)  # הוספת הספר לספרייה
        library.add_user("JohnDoe")  # הוספת משתמש

        # בדיקה אם הספר נוסע כראוי למילון checked_out_books
        library.check_out_book("JohnDoe", book)
        self.assertIn("JohnDoe", library.checked_out_books)  # בודק אם המשתמש נמצא במילון של הספרים המושאלים
        self.assertEqual(library.checked_out_books["JohnDoe"], book)  # בודק אם הספר שהושאל הוא הספר הצפוי

        # מציאת ספר שלא נמצא בספרייה
        with self.assertRaises(ValueError):  # מצפים לקבל שגיאה אם מנסים לשאול ספר שלא נמצא
            library.check_out_book("JohnDoe", Book("Nonexistent Book", "Unknown Author"))

        # מציאת משתמש שלא רשום
        with self.assertRaises(ValueError):  # מצפים לקבל שגיאה אם המשתמש לא רשום
            library.check_out_book("InvalidUser", book)

        # מציאת ספר שכבר הושאל
        library.check_out_book("JohnDoe", book)  # מוודאים שהספר הושאל שוב
        with self.assertRaises(ValueError):  # מצפים לקבל שגיאה אם הספר כבר הושאל
            library.check_out_book("JohnDoe", book)

            def test_return_book(self):
                library = Library()
                book = Book("The Great Gatsby", "F. Scott Fitzgerald")
                library.add_book(book)
                library.add_user("JohnDoe")


                library.check_out_book("JohnDoe", book)


                library.return_book("JohnDoe", book)


                self.assertNotIn("JohnDoe",
                                 library.checked_out_books)
                self.assertFalse(book.is_checked_out)


                with self.assertRaises(ValueError):
                    library.return_book("JohnDoe", book)


                non_existent_book = Book("Nonexistent Book", "Unknown Author")
                with self.assertRaises(ValueError):
                    library.return_book("JohnDoe", non_existent_book)


                with self.assertRaises(ValueError):
                    library.return_book("InvalidUser", book)


                with self.assertRaises(TypeError):
                    library.return_book("JohnDoe", "Not a book")
if __name__ == "__main__":
    unittest.main()
