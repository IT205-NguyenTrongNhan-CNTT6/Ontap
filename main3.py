
class Store:
    def __init__(self,id,name,revenue_day,open_days,bonus,net_revenue,performance_type):
        self.id = id 
        self.name = name 
        self.revenue_day = revenue_day 
        self.open_days = open_days
        self.bonus = bonus 
        self.net_revenue = 0
        self.performance_type = ""
   
    def caculate_net_revenue(self):
        self.net_revenue = (self.revenue_day * self.open_days) + self.bonus
        return self.net_revenue
     
    def classify_performance(self):
        if self.net_revenue < 9000000:
            self.performance_type = "Thấp"
        elif 9000000 >= self.net_revenue < 15000000:
            self.performance_type = "Trung bình"
        elif 15000000 >= self.net_revenue < 30000000:
            self.performance_type = "Khá"
        elif self.net_revenue >= 30000000:
            self.performance_type = "Cao"
    
class StoreManager:
    def __init__(self):
        self.store = []

    def add_store(self):
        self.id = input("Nhập vào mã cừa hàng: ")
        self.name = input("Nhập vào tên cửa hàng: ")
        self.revenue_day = int(input("Doanh thu trong 1 ngày: "))
        self.open_days = int("Số ngày công: ")
        self.bonus = int(input("Nhập vào số tiền thưởng: "))

        new_store = Store(self.id,self.name,self.revenue_day,self.open_days,self.bonus)
        new_store.caculate_net_revenue(self)
        new_store.performance_type(self)
        print("Thêm cừa hàng thành công")

    def show_store(self):
        pass


def menu():
    print("""
================ MENU ================
1. Hiển thị danh sách cửa hàng
2. Thêm cửa hàng mới
3. Cập nhật thông tin cửa hàng
4. Xóa cửa hàng
5. Tìm kiếm cửa hàng
6. Thống kê hiệu năng
7. Thoát
=====================================
""")

def main():
    # store = Store()
    store_manager = StoreManager()
    # store_manager.store.caculate_net_revenue()
    while True:
        menu()
        choice = input("Nhập lượt chọn của bạn: ")
        match choice: 
            case "1":
                pass
            case "2":
                store_manager.add_store()
                pass
            case "7":
                print("Thoát chương trình")
                break
            case _:
                print("Lựa chọn không hợp lệ ")

if __name__ == "__main__":
   main()


