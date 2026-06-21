
def get_validate_input(promt:str,input_type:str = "str"):
    while True:
        user_input = input(promt)
        if not user_input:
            print("Dữ liệu không được trống")
            continue
        if input_type == "match":
                value = int(user_input)
                if value < 0 and value > 50 :
                    print("Dữ liệu trong khoảng 0 đến 50")
                    continue
        if input_type == "int":
            try:
                value = int(user_input)
                if value <= 0 :
                    print("Dữ liệu không âm")
                    continue
                return value
            except ValueError:
                print("Dữ liệu không hợp lệ")
                continue
        if input_type == "float":
            try:
                value = int(user_input)
                if value <= 0 :
                    print("Dữ liệu không âm")
                    continue
                return value
            except ValueError:
                print("Dữ liệu không hợp lệ")
                continue
        return user_input



class Student:
    def __init__(self,id,name,theory_srore,practice_score,project_score):
        self.id = id 
        self.name = name
        self.theory_score = theory_srore
        self.practice_score = practice_score
        self.project_score = project_score
        self.final_score = 0
        self.academic_rank = ""

    def calculate_final_score(self):
        self.final_score = (self.theory_score * 0.2) + (self.practice_score * 0.3) + (self.project_score * 0.5)
    
    def classify_academic_rank(self):
        if self.final_score < 5.0 :
            self.academic_rank = "Yếu"
        elif 5.0 <= self.final_score < 7.0 :
            self.academic_rank = "Trung Bình"
        elif 7.0 <= self.final_score < 8.5 :
            self.academic_rank = "Khá"
        elif self.final_score >= 8.5 :
            self.academic_rank = "Giỏi"


class StudentManager:
    def __init__(self):
        self.students = []
    
    def add_student(self):
            self.id = get_validate_input("Nhập vào mã sinh viên: ")
            for stu in self.students:
                if stu.id == self.id :
                    print("Id không được trùng")
                    return
            self.name = get_validate_input("Nhập vào tên sinh viên: ")
            self.theory_score = get_validate_input("Nhập vào điểm lý thuyết: ","float")
            self.practice_score = get_validate_input("Nhập vào điểm thực hành: ","float")
            self.project_score = get_validate_input("Nhập vào điểm thực hành: ","float")

            new_stu = Student(self.id,self.name,self.theory_score,self.practice_score,self.project_score)
            new_stu.calculate_final_score()
            new_stu.classify_academic_rank()
            self.students.append(new_stu)
            print("Thêm sinh viên thành công")


    def show_all(self): 
            if not self.students : 
                print("Danh sách rỗng")
                return
            print(f"{"Mã SV":<8}| {"Họ tên":<20}| {"Điểm Lý Thuyết":<15}| {"Điểm Thực Hành":<15}| {"Điểm Đồ Án":<15}| {"Điểm Tổng Kết":<15}| {"Học Lực":<10}")
            for stu in self.students:
                print(f"{stu.id:<8}| {stu.name:<20}| {stu.theory_score:<15}| {stu.practice_score:<15}| {stu.theory_score:<15}| {stu.project_score:<15}| {stu.academic_rank:<10}")

    def update_student(self):
        if not self.students : 
                print("Danh sách rỗng")
                return
        self.id = get_validate_input("Nhập mã số sinh viên: ")
        for stu in self.students:
            if stu.id == self.id :
                self.theory_score = get_validate_input("Nhập điểm lý thuyết cần đổi: ","float")
                self.practice_score = get_validate_input("Nhập điểm thực hành muốn đổi: ","float")
                self.project_score = get_validate_input("Nhập điểm đồ ấn cần đổi: ","float")
                
                stu.theory_score = self.theory_score
                stu.practice_score = self.practice_score
                stu.project_score = self.project_score
                print("Đã cập nhật")
            else :
                print("Không tìm thấy sinh viên")
    def delete_student(self):
        if not self.students : 
                print("Danh sách rỗng")
                return
        self.id = get_validate_input("Nhập mã số sinh viên: ")
        for stu in self.students:
            if stu.id == self.id :
                really = input("Bạn chắc chắn muốn xóa (Y/N): ")
                if really == "Y":
                    self.students.remove(stu)
                    print("Đã xóa")
                elif really == "N":
                    print("Đã thoát")
                    break
    def search_student(self):
        if not self.students : 
                print("Danh sách rỗng")
                return
        self.name = get_validate_input("Nhập tên sinh viên: ")
        for stu in self.students:
            if stu.name.lower() == self.name.lower() :
                print("Đã tìm thấy sinh viên")
                print(f"Tên: {stu.name}")
            else:
                print("Không tìm thấy")


def menu():
     print("""
================ MENU ================
1. Hiển thị danh sách sinh viên
2. Thêm sinh viên mới
3. Cập nhật thông tin sinh viên
4. Xóa sinh viên
5. Tìm kiếm sinh viên theo tên
6. Thoát
=====================================
""")

def main():
    # students = Student()
    manager = StudentManager()
    while True:
        menu()
        choice = get_validate_input("Nhập lựa chọn của bạn: ")
        match choice :
            case "1":
                manager.show_all()
            case "2":
                manager.add_student()
            case "3":
                manager.update_student()
            case "4": 
                manager.delete_student()
            case "5":
                manager.search_student()
            case "6":
                print("Đã thoát chương trình")
                break
            case _:
                print("Lựa chọn không hợp lệ")



if __name__ == "__main__":
    main()