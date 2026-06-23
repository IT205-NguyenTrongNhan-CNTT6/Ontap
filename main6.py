
def get_validate_input(prompt:str,input_type:str = "str"):
    while True:
        user_input = input(prompt)
        if not user_input:
            print("Dữ liệu không được rỗng")
            continue
        if input_type == "int":
            try:
                value = int(user_input)
                if value < 1 or value > 5000 :
                    print("Dữ liệu không hợp lệ")
                    continue
                return value
            except ValueError:
                print("Dữ liệu không hợp lệ")
                continue
        if input_type == "float":
            try:
                value = float(user_input)
                if value <= 0 :
                    print("Dữ liệu không âm")
                    continue
                return value
            except ValueError:
                print("Dữ liệu không hợp lệ")
                continue
        return user_input
                

class DeliveryOrder:
    def __init__(self,order_id,receiver_name,base_fee,distance,surcharge):
        self.id = order_id
        self.name = receiver_name
        self.fee = base_fee
        self.distance = distance
        self.surcharge = surcharge
        self.total_delivery_cost = 0
        self.delivery_status = ""

    def calculate_total_cost(self):
        self.total_delivery_cost = (self.fee * self.distance) + self.surcharge

    def classify_delivery_status(self):
        if self.total_delivery_cost < 100000:
            self.delivery_status = "Đơn hàng Tiêu Chuẩn"
        elif 100000 <= self.total_delivery_cost < 300000:
            self.delivery_status = "Đơn hàng Cận tỉnh" 
        elif 300000 <= self.total_delivery_cost < 600000:
            self.delivery_status = "Đơn hàng Đường dài"
        elif self.total_delivery_cost >= 600000 :
            self.delivery_status = "Đơn hàng đặc biệt"

class OrderManager:
    def __init__(self):
        self.orders: list[DeliveryOrder] = []
    

    def add_order(self):
        while True:
            self.id = get_validate_input("Nhập mã đơn hàng của bạn: ")
            for ord in self.orders:
                if ord.id == self.id:
                    print("Đã trùng mã đơn")
                    return
            self.name = get_validate_input("Nhập tên đơn: ")
            self.fee = get_validate_input("Nhập vào cước nền của đơn: ","float")
            self.distance = get_validate_input("Nhập khoảng cách: ","int")
            self.surcharge = get_validate_input("Nhập vào phụ phí: ","float")

            new_ord = DeliveryOrder(self.id,self.name,self.fee,self.distance,self.surcharge)
            new_ord.calculate_total_cost()
            new_ord.classify_delivery_status()
            self.orders.append(new_ord)
            print("Đã thêm đơn thành công")
            break
    
    def show_all_order(self):
        if not self.orders:
            print("Danh sách rỗng")
            return
        print(f"{"Mã Đơn":<10}| {"Tên Người Nhận":<15}| {"Cước Nền":<15}| {"Khoảng Cách(Km)":<15}| {"Phụ Phí":<12}| {"Tổng Chi Phí":<12}| {"Trạng Thái Đơn":<20}")
        for ord in self.orders:
            print(f"{ord.id:<10}| {ord.name:<15}| {ord.fee:<15}| {ord.distance:<15}| {ord.surcharge:<12}| {ord.total_delivery_cost:<12}| {ord.delivery_status:<20}")
    
    def update_order(self):
        if not self.orders:
            print("Danh sách rỗng")
            return
        self.id = get_validate_input("Nhập mã đơn hàng cần cập nhật: ")
        for ord in self.orders:
                if ord.id == self.id:
                    self.fee = get_validate_input("Nhập vào cước nền mới: ","float")
                    self.distance = get_validate_input("Nhập vào khoảng cách mới: ","int")
                    self.surcharge = get_validate_input("Nhập vào phụ phí mới: ","float")

                    ord.fee = self.fee 
                    ord.distance = self.distance
                    ord.surcharge = self.surcharge
                    ord.calculate_total_cost()
                    ord.classify_delivery_status()
                    print("Đã cập nhật")
                    break
        else:
            print("Không tìm thấy đơn")

    def delete_order(self):
        if not self.orders:
            print("Danh sách rỗng")
            return
        self.id = get_validate_input("Nhập mã đơn hàng cần xóa: ")
        for ord in self.orders:
                if ord.id == self.id:
                    really = get_validate_input("Bạn có chắc chứ(Y/N): ")
                    if really.lower() == "Y".lower():
                        self.orders.remove(ord)
                        print("Đã xóa")
                        break
                    elif really.lower() == "N".lower():
                        print("Không xóa sản phẩm")
                        break
        else:
            print("Không tìm thấy đơn")
        
    def search_by_receiver(self):
        if not self.orders:
            print("Danh sách rỗng")
            return
        found = False
        self.name = get_validate_input("Nhập vào tên đơn cần tìm: ")
        for ord in self.orders:
            if self.name.lower() in ord.name.lower():
                print("Đã tìm thấy đơn")
                print(f"Tên Đơn: {ord.name}")
                found = True
        if not found:
            print("Không tìm thấy đơn")



def main():
    manager = OrderManager()
    while True:
        print("""
================ MENU ================
1. Hiển thị danh sách vận đơn trong hệ thống
2. Nhập vận đơn mới
3. Cập nhật thông tin vận đơn
4. Xóa vận đơn khỏi hệ thống
5. Tìm kiếm vận đơn theo tên người nhận
6. Thoát
=====================================
""")
        choice = get_validate_input("Nhập vào lựa chọn của bạn: ")
        match choice:
            case "1":
                manager.show_all_order()
            case "2":
                manager.add_order()
            case "3":
                manager.update_order()
            case "4":
                manager.delete_order()
            case "5":
                manager.search_by_receiver()
            case "6":
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý vận đơn!")
                break
            case _:
                print("Dữ liệu không hợp lệ")



if __name__ == "__main__":
    main()
             