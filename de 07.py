class LibraryBorrow:
    def __init__(self, id, reader_name, book_name,borrow_days, late_days, fine_per_day):
        self.id = id
        self.reader_name = reader_name
        self.book_name = book_name
        self.borrow_days = borrow_days
        self.late_days = late_days
        self.fine_per_day = fine_per_day
        self.calculate_fine()
        self.classify_fine()

    # Tính tổng tiền phạt
    def calculate_fine(self):
        self.total_fine = self.late_days * self.fine_per_day

    # Phân loại mức phạt
    def classify_fine(self):
        if self.total_fine == 0:
            self.fine_type = "Khong phat"
        elif self.total_fine < 50000:
            self.fine_type = "Nhe"
        elif self.total_fine < 200000:
            self.fine_type = "Trung binh"
        else:
            self.fine_type = "Nang"


class LibraryBorrowManager:
    def __init__(self):
        self.borrow_records = []

    # Thêm phiếu mượn
    def add_borrow_record(self):
        id = input("Ma phieu muon: ")

        if id.strip() == "":
            print("Ma phieu muon khong duoc rong!")
            return

        for r in self.borrow_records:
            if r.id == id:
                print("Trung ma!")
                return

        reader_name = input("Ten ban doc: ")
        book_name = input("Ten sach: ")

        borrow_days = int(input("So ngay muon: "))
        late_days = int(input("So ngay tre: "))

        if late_days > borrow_days:
            print("So ngay tre khong duoc lon hon so ngay muon!")
            return

        fine_per_day = int(input("Tien phat/ngay: "))

        self.borrow_records.append(
            LibraryBorrow(
                id,
                reader_name,
                book_name,
                borrow_days,
                late_days,
                fine_per_day
            )
        )

        print("Them thanh cong!")

    # Hiển thị danh sách
    def show_all(self):
        if not self.borrow_records:
            print("Danh sach rong!")
            return

        for r in self.borrow_records:
            print(
                r.id,
                r.reader_name,
                r.book_name,
                r.borrow_days,
                r.late_days,
                r.fine_per_day,
                r.total_fine,
                r.fine_type
            )

    # Cập nhật phiếu mượn
    def update_borrow_record(self):
        id = input("Nhap ma can sua: ")

        for r in self.borrow_records:
            if r.id == id:

                r.borrow_days = int(input("So ngay muon: "))
                r.late_days = int(input("So ngay tre: "))

                if r.late_days > r.borrow_days:
                    print("So ngay tre khong duoc lon hon so ngay muon!")
                    return

                r.fine_per_day = int(input("Tien phat/ngay: "))

                r.calculate_fine()
                r.classify_fine()

                print("Cap nhat thanh cong!")
                return

        print("Khong tim thay!")

    # Xóa phiếu mượn
    def delete_borrow_record(self):
        id = input("Nhap ma can xoa: ")

        for r in self.borrow_records:
            if r.id == id:

                confirm = input("Ban co chac muon xoa? (Y/N): ")

                if confirm.lower() == "y":
                    self.borrow_records.remove(r)
                    print("Xoa thanh cong!")

                elif confirm.lower() == "n":
                    print("Da huy thao tac!")

                else:
                    print("Lua chon khong hop le!")

                return

        print("Khong tim thay!")

    # Tìm kiếm phiếu mượn

manager = LibraryBorrowManager()

while True:

    print("\n========== MENU ==========")
    print("1. Hien thi danh sach phieu muon")
    print("2. Them phieu muon moi")
    print("3. Cap nhat phieu muon")
    print("4. Xoa phieu muon")
    print("5. Tim kiem phieu muon")
    print("6. Thoat")

    choice = input("Chon: ")

    if choice == "1":
        manager.show_all()

    elif choice == "2":
        manager.add_borrow_record()

    elif choice == "3":
        manager.update_borrow_record()

    elif choice == "4":
        manager.delete_borrow_record()

    elif choice == "5":
        manager.search_borrow_record()

    elif choice == "6":
        print("Cam on ban da su dung chuong trinh!")
        break

    else:
        print("Lua chon khong hop le!")
