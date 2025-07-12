def main():
    try:
        # initialize book list
        bookslist = []
        infile = open("theBooksList.txt", "r")
        line = infile.readline()
        while line:
            bookslist.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()
    except FileNotFoundError:
        print("the <bookslist.txt> file is not found")
        print("Starting a new books list!")
        bookslist = []


    choice = 0
    while choice != 4:
        print("\n*** Books Manager App ***")
        print("(1.) Add a book")
        print("(2.) Lookup a book")
        print("(3.) Display all-books")
        print("(4.) Quit program")
        choice = int(input())

        if choice == 1:
            print("Adding a book....\n")
            nBook = input("Enter the name of the Book...\n")
            nAuthor = input("Enter the name of the Author ...\n")
            nPages = input("Enter the number of the Pages ...\n")
            bookslist.append([nBook, nAuthor, nPages])
            print("***Book Adition Successful***")
        
        elif choice == 2:
            print("Looking up for a book...\n")
            keyword = input("Enter Search Terms: \n")
            for book in bookslist:
                if keyword in book:
                    print(book)

        elif choice == 3:
            print("Displaying all books...")
            for i in range(len(bookslist)):
                print(bookslist[i])
        elif choice == 4:
            print("\n *** Quitting Program *** \n")
    print("*** Program Terminated!. *** \n")

    #Saving to external txt file
    outfile = open("theBooksList.txt", "w")
    for book in bookslist:
        outfile.write(",".join(book) + "\n")
    outfile.close()


if __name__ == "__main__":
    main()