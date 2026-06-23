

def get_validate_input(prompt:str,input_type:str = "str"):
    while True:
        user_input = input(prompt)
        if not user_input:
            print("Dữ liệu không được rỗng")
            continue
        if input_type == "int":
            try :
                value = int(user_input)
                if value < 0 :
                    print("Dữ liệu không hợp lệ")
                    continue
                elif value > 1000 :
                    print("Dữ liệu quá lớn")
                    continue
                return value
            except ValueError:
                    print("Dữ liệu không hợp lệ")
                    continue
        if input_type == "float":
            try :
                value = float(user_input)
                if value < 0 :
                    print("Dữ liệu không được âm")
                    continue
                return value
            except ValueError:
                    print("Dữ liệu không hợp lệ")
                    continue
        return user_input


class Product:
    def __init__(self,id,name,import_price,quantity,storage_fee):
        self.id = id 
        self.name = name 
        self.import_price = import_price
        self.quantity = quantity
        self.storage_fee = storage_fee
        self.total_value = 0 
        self.stock_status = ""

    def calculate_total_value(self):
        self.total_value = (self.import_price * self.quantity) + self.storage_fee
    def classify_stock_status(self):
        if self.total_value < 9000000:
            self.stock_status = "Thấp"
        elif 9000000 <= self.total_value < 15000000:
            self.stock_status = "Trung Bình"
        elif 15000000 <= self.total_value < 30000000:
            self.stock_status = "Cao"
        else: 
            self.stock_status = "Rất Cao"  
    
class ProductManager:
        def __init__(self):
            self.products = []
        
        def add_products(self):
            while True:
                self.id = get_validate_input("Nhập mã SP: ")
                for pro in self.products :
                    if self.id == pro.id:
                        print("Mã sản phẩm không được trùng")
                        return
                self.name = get_validate_input("Nhập vào tên sẩn phẩm: ")
                self.import_price = get_validate_input("Nhập vào giá nhập sản phẩm: ","float")
                self.quantity = get_validate_input("Nhập vào số lượng: ","int")
                self.storage_fee = get_validate_input("Nhập vào chi phí kho: ","float")

                new_pro = Product(self.id,self.name,self.import_price,self.quantity,self.storage_fee)
                new_pro.calculate_total_value()
                new_pro.classify_stock_status()
                self.products.append(new_pro)
                print("Đã thêm sản phẩm thành công")
                break

        def show_all(self):
            if not self.products:
                print("Danh sách rỗng")
                return
            print(f"{"Mã SP":<10}| {"Tên sản phẩm":<15}| {"Giá nhập":<15}| {"Số lượng":<12}| {"Chi phí kho":<15}| {"Tổng giá trị":<15}| {"Trạng thái tồn kho":<12}")
            for pro in self.products:
                print(f"{pro.id:<10}| {pro.name:<15}| {pro.import_price:<15}| {pro.quantity:<12}| {pro.storage_fee:<15}| {pro.total_value:<15}| {pro.stock_status:<12}")
        
        def update_products(self): 
                if not self.products:
                    print("Danh sách rỗng")
                    return
                self.id = get_validate_input("Nhập mã SP cần cập nhật: ")
                for pro in self.products:
                    if pro.id == self.id:
                        self.import_price = get_validate_input("Nhập giá nhập mới: ","float")
                        self.quantity = get_validate_input("Nhập số lượng mới: ","int")
                        self.storage_fee = get_validate_input("Nhập chi phí kho mới: ","float")

                        pro.import_price = self.import_price
                        pro.quantity = self.quantity
                        pro.storage_fee = self.storage_fee
                        pro.calculate_total_value()
                        pro.classify_stock_status()
                        print("Đã cập nhật")
                        break
                else:
                    print("Không tìm thấy mã SP")
        
        def delete_products(self):
            if not self.products:
                print("Danh sách rỗng")
                return
            self.id = get_validate_input("Nhập mã SP cần xóa: ")    
            for pro in self.products:
                if pro.id == self.id :
                    really = input("Bạn chắc chắn muốn xóa (Y/N): ")
                    if really.lower() == "Y".lower():
                        self.products.remove(pro)
                        print("Đã xóa")
                        break
                    elif really.lower() == "N".lower():
                        print("Đã thoát")
                        break
            else:
                        print("Không tìm thấy")
        
        def search_products(self):
            if not self.products : 
                    print("Danh sách rỗng")
                    return
            found = False
            for pro in self.products:
                if self.name.lower() in pro.name.lower():
                    print("Đã tìm thấy sản phẩm")
                    print(f"Tên: {pro.name}")
                    found = True

            if not found:
                print("Không tìm thấy mã sản phẩm phù hợp")


def main():
    manager = ProductManager()
    while True: 
        print("""
================ MENU ================
1. Hiển thị danh sách sản phẩm trong kho
2. Nhập sản phẩm mới vào kho
3. Cập nhật thông tin sản phẩm
4. Xóa sản phẩm khỏi kho
5. Tìm kiếm sản phẩm theo tên
6. Thoát
=====================================
""")
        choice = get_validate_input("Nhập lựa chọn của bạn: ")
        match choice:
            case "1":
                manager.show_all()
            case "2":
                manager.add_products()
            case "3":
                manager.update_products()
            case "4":
                manager.delete_products()
            case"5":
                manager.search_products()
            case "6":
                print("Đã thoát")
                break
            case _:
                print("Dữ liệu không hợp lệ")   



if __name__  == "__main__":
   main()
     