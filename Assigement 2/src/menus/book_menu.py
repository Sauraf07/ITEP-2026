class BookMenu:
    def create_book(self):
        try:
            with Session.begin() as session:
