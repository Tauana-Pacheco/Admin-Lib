class Loan: 
    def __init__(self, status, start_date, end_date, user_name, id_book):
        self.status = status
        self.start_date = start_date
        self.end_date = end_date
        self.user_name = user_name
        self.id_book = id_book
    
    # Getters
    def get_status(self):
        return self.status

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_user_name(self):
        return self.user_name

    def get_id_book(self):
        return self.id_book

    # Setters
    def set_status(self, status):
        self.status = status

    def set_start_date(self, start_date):
        self.start_date = start_date

    def set_end_date(self, end_date):
        self.end_date = end_date

    def set_user_name(self, user_name):
        self.user_name = user_name

    def set_id_book(self, id_book):
        self.id_book = id_book