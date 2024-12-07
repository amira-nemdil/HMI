import 'dart:math';

class LibraryBook {
  String bookID;
  String title;
  bool available;

  // Default constructor
  LibraryBook(this.bookID, this.title, this.available);

  // Named constructor 'newBook'
  LibraryBook.newBook(this.title)
      : bookID = _generateRandomBookID(),
        available = true;

  // Method to generate a random 8-character bookID
  static String _generateRandomBookID() {
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    final random = Random();
    return List.generate(8, (index) => characters[random.nextInt(characters.length)])
        .join();
  }

  // Method to display book details
  void displayDetails() {
    print('Book ID: $bookID');
    print('Title: $title');
    print('Available: $available');
  }
}

void main() {
  // Using the default constructor
  LibraryBook book1 = LibraryBook('AB123456', 'Dart Programming', true);
  book1.displayDetails();

  print('\n');

  // Using the named constructor
  LibraryBook book2 = LibraryBook.newBook('Flutter for Beginners');
  book2.displayDetails();
}
