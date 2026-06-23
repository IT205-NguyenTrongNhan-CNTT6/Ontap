class Student :
    def __init__(self, id, name, theory_score,practice_score, project_score):
        self.__id = id
        self.__name = name
        self.__theory_score = theory_score
        self.__practice_score = practice_score
        self.__project_score = project_score
        self.__final_score  = 0
        self.__academic_rank = ""
    @property
    def id(self):
        return self.__id
    @property
    def name(self):
        return self.__name
    @property
    def theory_score(self):
        return self.__theory_score
    @property
    def practice_score(self):
        return self.__practice_score
    @property
    def project_score(self):
        return self.__project_score
    @property
    def final_score(self):
        return self.__final_score
    @property
    def academic_rank(self):
        return self.__academic_rank
    def update_theory_score(self, theory_score):
        self.__theory_score = theory_score
    def update_practice_score(self, practice_score):
        self.__practice_score = practice_score
    def update_project_score(self, project_score):
        self.__project_score = project_score 
    
    def calculate_final_score(self):
        self.__final_score = (self.__theory_score*0.2) + (self.__practice_score*0.3) + (self.__project_score*0.5)
    def classify_academic_rank(self):
        if self.__final_score > 10 or self.__final_score < 0:
            print("điểm không hợp lệ")
            return
        if self.__final_score < 5:
            self.__academic_rank = "yếu"
        elif self.__final_score < 7 :
            self.__academic_rank = "Trung bình"
        elif self.__final_score < 8.5:
            self.__academic_rank = "Khá"
        else: 
            self.__academic_rank = "giỏi"

class StudentManager :
    def __init__(self):
        self.students : list[Student] = []
    def add_student(self):
        while True:
            stu_id = input("nhập mã SV")
            stu_name = input("nhập tên SV:")
            if not stu_id or not stu_name:
                print("mã SV hoặc tên SV không được để trống")
            else :
             break
        for stu in self.students:
            if stu.id == stu_id:
                print("mã SV đã tồn tại")
                return
        stu_theory_score = float(input("nhập điểm lý thuyết:"))
        stu_practice_score = float(input("nhập điểm thực hành"))
        stu_project_score = float(input("nhập điểm đồ án"))
        new_stu = Student(stu_id,stu_name,stu_theory_score,stu_practice_score,stu_project_score)
        new_stu.calculate_final_score()
        new_stu.classify_academic_rank()
        self.students.append(new_stu)
    def show_all(self):
        if not self.students:
            print("không sinh viên nào")
            return 
        print(f"{"Mã SV" :<10 } | {"Họ tên":< 20} |{" Điểm Lý Thuyết":<5} | {"Điểm Thực Hành":<5} | {"Điểm Đồ Án":< 5} | {"Điểm Tổng Kết":<5} | {"Học Lực":< 10}")
        for stu in self.students:
            print(f"{stu.id :<10 } | {stu.name:< 20} |{stu.theory_score:<5} | {stu.practice_score:<5} | {stu.project_score:< 5} | {stu.final_score:<5} | {stu.academic_rank:< 10}")
    def update_student(self):
        stu_id = input("nhập mã SV cần cập nhật:")
        for stu in self.students:
            if stu.id == stu_id:
                stu_theory_score = float(input("nhập điểm lý thuyết:"))
                stu_practice_score = float(input("nhập điểm thực hành"))
                stu_project_score = float(input("nhập điểm đồ án"))
                stu.update_theory_score(stu_theory_score)
                stu.update_practice_score(stu_practice_score)
                stu.update_project_score(stu_project_score)
                stu.calculate_final_score()
                stu.classify_academic_rank()
                print("cập nhật thành công")
        else: 
            print("không tìm thấy sinh viên cần cập nhật:")
    def delete_student(self):
        stu_id = input('nhập mã sinh viên cần xóa')
        for stu in self.students:
                    if stu.id == stu_id:
                        print(f"đã tìm thấy SV: {stu.id}")
                        choice = input("Bạn có chắc muốn xóa sinh viên này không? (Y/N): ").lower()
                        match choice:
                            case "y":
                                 self.students.remove(stu)
                                 print("đã xóa SV thành công")

                            case "n":
                                print("Thao tác đã được hủy bỏ")
                                return
        else: 
            print("không tìm thấy sinh viên")
    def search_student(self):
        stu_name = input("nhập Tên sinh viên cần tìm: ")
        list_student  = StudentManager()
        for stu in self.students:
            if stu_name in stu.name:
                list_student.add_student(stu)
        list_student.show_all()
        if not list_student:
            print("không tìm thấy sinh viên phù hợp")
      
def main():
    pass 





    



                



     