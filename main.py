class Star_Cinema:
    __hall_list = []

    def entry_hall(self, object):
        self.__hall_list.append(object)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.rows = rows
        self.cols = cols
        self.__hall_no = hall_no
        super().entry_hall(self)

    def entry_show(self, id, movie_name, time):
        self.__id = id
        self.movie_name = movie_name
        self.time = time
        self.__show_list.append((id, movie_name, time))

        # Row and Colums 5 X 5 Martix
        if (self.rows == 5 and self.cols == 5):
            temp_list = []
            row_items = ["A", "B", "C", "D", "E"]
            col_items = ["0", "1", "2", "3", "4"]
            seat_list = [[(j+i)for i in col_items]
                         for j in row_items]
            temp_list.append(self.__id)
            for item in range(len(temp_list)):
                self.__seats[temp_list[item]] = seat_list

    def book_seats(self, name, phone_number, show_id, seat_tuple):
        self.name = name
        self.phone_number = phone_number
        self.show_id = show_id
        self.__seat_tuple = seat_tuple

        print('-'*90)
        for run_movie in self.__show_list:
            if (run_movie[0] == self.show_id):
                print("Show ID: " + run_movie[0] + "\t\tMovie Name: " +
                      run_movie[1]+"\t\tShow Time: " + run_movie[2])

        print('-'*90)
        print()

        Flag = False
        temp_book_seat = []
        if (self.show_id in self.__seats.keys()):
            # self.update_col = []
            for check in self.__seat_tuple:
                if any(check in nested_check_list for nested_check_list in self.__seats.get(self.show_id)):
                    update_list = []
                    for check_row in self.__seats.get(self.show_id):
                        col = []
                        for check_col in check_row:
                            if (check_col == "X" and check == check_col):
                                check_col = 'X'
                                col.append(check_col)
                                print(f"Already Booked: {check_col}")
                            elif (check_col == check):
                                print(f"Successful Booked: {check_col}")
                                Flag = True
                                temp_book_seat.append(check_col)
                                check_col = 'X'
                                col.append(check_col)

                            elif (check != check_col):
                                col.append(check_col)
                            else:
                                print("Not Abailable This seat")
                        update_list.append(col)
                    self.__seats[self.show_id] = update_list
                else:
                    print("Seat Not Valid Or Already Booked!")

            if (Flag):
                print('-'*90)
                print(F"Hall Name   : {self.__hall_no}")
                print(F"Name        : {self.name}")
                print(F"Phone Number: {self.phone_number}")
                print("Booked Seat List: ")
                for seat_book in temp_book_seat:
                    print(seat_book, end=" ")
            else:
                print('-'*90)
                print(F"\tUser Name:{self.name}")
                print(F"\tUser Phone Number:{self.phone_number}")
                print("Invalied Seat or Already Booked")
                print("Thanks")

        else:
            print("Show ID Invalid!")

    def view_show_list(self):
        print("\n\t\t\t\t-:VIEW SHOW LIST:-")
        print('-'*90)
        for run_movie in self.__show_list:
            print("SHOW ID: " + run_movie[0]+"\t\tMOVIE NAME: " +
                  run_movie[1]+"\t\tSHOW TIME: " + run_movie[2])
        print()

    def view_available_seats(self, view_id):
        if self.__seats.get(view_id):
            print()
            print('-'*90)
            for running_movie in self.__show_list:
                if (running_movie[0] == view_id):
                    print("\tShow ID: " + running_movie[0] + "\n\tMovie Name: " +
                          running_movie[1]+"\n\tShow Time: " + running_movie[2])

            print('-'*90)
            print(f"\t\t\t\t-:AVAILABLE SEAT:-")
            print("X -> Already Booked")
            print('-'*90)
            temp = self.__seats.get(view_id)
            for seat_d in temp:
                for s in seat_d:
                    print(s, end="\t\t")
                print()
        else:
            print("Show ID Invalid! Try Again.")


Sony_Hall = Hall(5, 5, "H12A")
Sony_Hall.entry_show("acg12", "Man of Life", "Nov 12  2022 12.30PM")
Sony_Hall.entry_show("xyz67", "Time Travel", "Nov 5   2022  2.30PM")
Sony_Hall.entry_show("baf31", "the Future",  "Nov 10  2022 10.30PM")

while True:
    print("\n\r")
    print("\t\tCINAMA HALL TRICKET BOOKING SYSTEM")
    print('-'*90)
    print("\t1.VIEW ABILABLE SITE\n\t2.VIEW RUNNING SHOW\n\t3.BOOKING THE SHOW")
    print("\t4.EXIT")
    print("**Selected Show List Above")
    item_choose = int(input("Enter Choise Option: "))
    if (item_choose == 4):
        print("\tThank You!")
        break
    elif (item_choose == 1):
        chk_id = input("Enter Show ID: ")
        Sony_Hall.view_available_seats(chk_id)
    elif (item_choose == 2):
        Sony_Hall.view_show_list()
    elif (item_choose == 3):
        user_name = input("Enter User Name: ")
        phone_number = input("Enter User Phone Number: ")
        curr_show_id = input("Enter Current Show ID: ")
        num_count = int(input("Number of Seat: "))
        seat_list = []
        for cnt in range(num_count):
            seat_row = str(input(f"{cnt+1} Seat Number: "))
            seat_list.append(seat_row)

        # print()
        seat_str = " ".join(seat_list)
        book_seat_tuple = tuple(seat_str.split(" "))
        Sony_Hall.book_seats(user_name, phone_number,
                             curr_show_id, book_seat_tuple)
    else:
        print("\tInvalid Option Selecte.Try Again")
