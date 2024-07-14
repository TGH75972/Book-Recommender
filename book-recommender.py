import random

class Book:
    def __init__(self, title, author, rating):
        self.title = title
        self.author = author
        self.rating = rating

class BookRecommender:
    def __init__(self):
        self.books = []
    
    def add_book(self, title, author, rating):
        self.books.append(Book(title, author, rating))
    
    def recommend_books(self, min_rating=4.0, num_books=5):
        filtered_books = [book for book in self.books if book.rating >= min_rating]
        recommended_books = random.sample(filtered_books, min(num_books, len(filtered_books)))
        return recommended_books
    
    def list_books(self):
        return self.books

book_recommender = BookRecommender()
book_recommender.add_book('The Great Gatsby', 'F. Scott Fitzgerald', 4.2)
book_recommender.add_book('To Kill a Mockingbird', 'Harper Lee', 4.5)
book_recommender.add_book('1984', 'George Orwell', 4.4)
book_recommender.add_book('Pride and Prejudice', 'Jane Austen', 4.6)
book_recommender.add_book('The Catcher in the Rye', 'J.D. Salinger', 4.0)
book_recommender.add_book('Moby Dick', 'Herman Melville', 3.9)
book_recommender.add_book('War and Peace', 'Leo Tolstoy', 4.3)
book_recommender.add_book('The Odyssey', 'Homer', 4.1)
book_recommender.add_book('Ulysses', 'James Joyce', 3.8)
book_recommender.add_book('The Divine Comedy', 'Dante Alighieri', 4.5)
book_recommender.add_book('Crime and Punishment', 'Fyodor Dostoevsky', 4.6)
book_recommender.add_book('The Brothers Karamazov', 'Fyodor Dostoevsky', 4.7)
book_recommender.add_book('One Hundred Years of Solitude', 'Gabriel Garcia Marquez', 4.4)
book_recommender.add_book('Don Quixote', 'Miguel de Cervantes', 4.3)
book_recommender.add_book('The Iliad', 'Homer', 4.2)
book_recommender.add_book('Brave New World', 'Aldous Huxley', 4.1)
book_recommender.add_book('The Lord of the Rings', 'J.R.R. Tolkien', 4.7)
book_recommender.add_book('Harry Potter and the Sorcerer\'s Stone', 'J.K. Rowling', 4.8)
book_recommender.add_book('The Hobbit', 'J.R.R. Tolkien', 4.5)
book_recommender.add_book('Fahrenheit 451', 'Ray Bradbury', 4.4)
book_recommender.add_book('Jane Eyre', 'Charlotte Bronte', 4.2)
book_recommender.add_book('Wuthering Heights', 'Emily Bronte', 4.1)
book_recommender.add_book('Anna Karenina', 'Leo Tolstoy', 4.6)
book_recommender.add_book('The Picture of Dorian Gray', 'Oscar Wilde', 4.4)
book_recommender.add_book('Les Misérables', 'Victor Hugo', 4.6)
book_recommender.add_book('The Count of Monte Cristo', 'Alexandre Dumas', 4.8)
book_recommender.add_book('The Alchemist', 'Paulo Coelho', 4.2)
book_recommender.add_book('The Old Man and the Sea', 'Ernest Hemingway', 4.1)
book_recommender.add_book('The Sun Also Rises', 'Ernest Hemingway', 4.0)
book_recommender.add_book('Catch-22', 'Joseph Heller', 4.3)
book_recommender.add_book('The Sound and the Fury', 'William Faulkner', 3.9)
book_recommender.add_book('Lolita', 'Vladimir Nabokov', 4.0)
book_recommender.add_book('Of Mice and Men', 'John Steinbeck', 4.3)
book_recommender.add_book('East of Eden', 'John Steinbeck', 4.6)
book_recommender.add_book('A Tale of Two Cities', 'Charles Dickens', 4.5)
book_recommender.add_book('David Copperfield', 'Charles Dickens', 4.4)
book_recommender.add_book('The Grapes of Wrath', 'John Steinbeck', 4.7)
book_recommender.add_book('Dracula', 'Bram Stoker', 4.2)
book_recommender.add_book('Frankenstein', 'Mary Shelley', 4.3)
book_recommender.add_book('The Catcher in the Rye', 'J.D. Salinger', 4.0)
book_recommender.add_book('The Road', 'Cormac McCarthy', 4.2)
book_recommender.add_book('Life of Pi', 'Yann Martel', 4.1)
book_recommender.add_book('Gone with the Wind', 'Margaret Mitchell', 4.5)

my_reads = [
    ("A Thousand Splendid Suns", "Great story"),
    ("48 Laws of Power", "Great read"),
    ("Power of Subconscious Mind", "")
]

while True:
    command = input("Enter command (recommend, list, myreads, exit): ").strip().lower()
    if command == 'recommend':
        min_rating = float(input("Minimum rating (default 4.0): ").strip() or 4.0)
        num_books = int(input("Number of books (default 5): ").strip() or 5)
        recommendations = book_recommender.recommend_books(min_rating, num_books)
        for book in recommendations:
            print(f"{book.title} by {book.author} (Rating: {book.rating})")
    elif command == 'list':
        books = book_recommender.list_books()
        for book in books:
            print(f"{book.title} by {book.author} (Rating: {book.rating})")
    elif command == 'myreads':
        for idx, (title, review) in enumerate(my_reads, 1):
            print(f"{idx}. {title} - {review}")
    elif command == 'exit':
        break
    else:
        print("Invalid command.")
