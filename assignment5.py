books = ['li', 'on']
print('Welcome to the Book Library')
add_cntr = 1
rem_cntr = 1

while True:
    menu = input('Enter your choice:\n1: Add a book 2: Remove a book 3: View all books 4: Exit Program\n')    
    
    #Adding a Book
    if menu == '1':
        book_no = int((input('Enter number of books you want to add: ')))
        while add_cntr>0 and add_cntr <= book_no:
            add_books = input(f'Enter book {add_cntr}\'s title: ')
            add_cntr += 1
            books.append(add_books)

    #Removing a book
    elif menu == '2':
        book_no = int((input('Enter number of books you want to remove: ')))
        while rem_cntr>0 and rem_cntr <=book_no:
            rem_books = input(f'Enter book {rem_cntr}\'s title: ')
            if rem_books not in books:
                print('Book not found')
                break
            else:
                rem_books in books
                books.remove(rem_books)
                rem_cntr+=1
                print(rem_books, 'removed succesfully')
    #View all books
    elif menu == '3':
        print(', '.join(books), 'are the books in your library')
    
    #Exit program
    elif menu == '4':
        print('Goodbye')
        break