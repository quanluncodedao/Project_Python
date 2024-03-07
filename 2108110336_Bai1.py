# Dữ liệu sách
mybooks = [
    {"Title": "Android App Development", "Author": "Thanh Tran", "Publisher": "VNU", "Price": "25000", "Published_Year": "2017"},
    {"Title": "Python", "Author": "Thanh Tran", "Publisher": "VNU", "Price": "23000", "Published_Year": "2019"},
    {"Title": "JavaScript", "Author": "Pham Dieu", "Publisher": "SSS", "Price": "38000", "Published_Year": "2018"},
    {"Title": "HTML5", "Author": "Man Nhi", "Publisher": "HCM", "Price": "33000", "Published_Year": "2012"},
    {"Title": "Compiler", "Author": "Thanh Tran", "Publisher": "VNU", "Price": "24000", "Published_Year": "2011"},
    {"Title": "C language", "Author": "Man Nhi", "Publisher": "SSS", "Price": "29000", "Published_Year": "2010"},
    {"Title": "Programming Linguistics", "Author": "Pham Dieu", "Publisher": "HCM", "Price": "41000", "Published_Year": "2009"},
    {"Title": "C# language", "Author": "Thanh Tran", "Publisher": "VNU", "Price": "42000", "Published_Year": "2013"},
    {"Title": "App Inventor", "Author": "Man Nhi", "Publisher": "LD", "Price": "30000", "Published_Year": "2015"},
]

def search_book(books):
    while True:
        print("Chọn để tìm kiếm:")
        print("1. Title")
        print("2. Author")
        print("3. Publisher")
        choice = input("Chọn (1, 2, 3): ")

        if choice not in ['1', '2', '3']:
            print("Vui lòng chọn lại.")
            continue

        keyword = input("Nhập từ khóa cần tìm: ")

        found = False
        for book in books:
            if choice == '1' and keyword.lower() in book["Title"].lower():
                print(book)
                found = True
            elif choice == '2' and keyword.lower() in book["Author"].lower():
                print(book)
                found = True
            elif choice == '3' and keyword.lower() in book["Publisher"].lower():
                print(book)
                found = True

        if not found:
            print("Không tìm thấy sách")

search_book(mybooks)