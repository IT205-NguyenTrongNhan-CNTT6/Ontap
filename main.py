

def get_validate_input(promt:"str",input_type:str = "string"):
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

def classify_player(perform_player):
    rank = ""
    if perform_player < 15:
            rank = "Pháo đần"
    elif perform_player < 30:
            rank = "Dự bị chiến lược"
    elif perform_player < 50:
            rank = "Trụ cột đội bóng"
    else:
            rank = "Ngôi sao"

def add_player(player):
        while True:
            id_player = get_validate_input("Nhập vào một mã cầu thủ: ")
            for item in player:
                if(id_player.lower() == item.get("id").lower()):
                    print("Mã cầu thử trùng lặp! Nhập lại")
                    return
                else: 
                    name_player = get_validate_input("Nhập vào tên cầu thủ: ")
                    match_player = get_validate_input("Nhập vào số trận đấu: ","match")
                    goal_player = get_validate_input("Nhập số bàn thắng: ","int")
                    assists_player = get_validate_input("Nhập số kiến tạo: ","int")
                    perform_player = (match_player * 1) + (assists_player * 2) + (goal_player * 3)
                    classify_player()
                    new_player = {
                        "id": id_player, 
                        "name": name_player,
                        "goal": goal_player,
                        "assists": assists_player,
                        "perform": perform_player
                    }
                    player.append(new_player)
                    break


def remove_player(player):
    del_id = get_validate_input("Nhập vào mã cầu thủ cần xóa: ")
    for item in player:
                if(del_id.lower() == item.get("id").lower()):
                    player.remove()
                    print("Đã bán cầu thử")
                    break
    else:
         print("Không tìm thấy cầu thủ")


def upd_player(player):
        if not player:
            print("Danh sách cầu thủ rỗng!")
            return
        upd_id = get_validate_input("Nhập vào mã cầu thử cần cập nhật: ")
        for item in player:
            if upd_id.lower() == item.get("id").lower():
                match_player = get_validate_input("Nhập vào số trận đấu: ","match")
                goal_player = get_validate_input("Nhập số bàn thắng: ","int")
                assists_player = get_validate_input("Nhập số kiến tạo: ","int")
                perform_player = (match_player * 1) + (assists_player * 2) + (goal_player * 3)


                player["match"] = match_player
                player["goal"] = goal_player
                player["assists"] = assists_player
                player["perform"] = perform_player
                player["rank"] = classify_player(perform_player)
        else: 
                print("Không tìm thấy cầu thủ")

def search_player(player):
    if not player:
            print("Danh sách cầu thủ rỗng!")
            return
    search_id = get_validate_input("Nhập mã cầu thủ hoặc tên cần tìm: ")
    find_player = [
    ] 
    for item in player:
            if search_id.lower() == item.get("id").lower() or search_id.lower() == item.get("name").lower():
                find_player.append(player)
                return
    else : 
         print("Không tìm thấy")
             
                     

def menu():
    print("-"*25)
    print("----Quản Lý Cầu Thủ----")
    print("-"*25)
    print("1.Hiển thị danh sách cầu thủ\n"+
          "2.Tiếp nhận cầu thủ mới\n"+
          "3.Cập nhật thông tin và chỉ số\n"+
          "4.Xóa cầu thủ\n"+
          "5.Tìm kiếm cầu thủ\n"+
          "6.Thống kê phong độ\n"+
          "7.Đánh giá phong độ tự động\n"+
          "8.Thoát chương trình")

def show_player(player: list[dict]):
    if not player:
        print("Danh sách cầu thủ rỗng!")
        return
    print(f"{"Mã CT":<3}| {"Họ và Tên":<20}| {"Số trận thi đấu:":<18}| {"Bàn thắng":<12}| {"Kiến tạo":<10}| {"Hiệu suất":<5}| {"Phong độ":<20} ")    
    for item in player:
        print(f"{item.get("id"):<3}| {item.get("name"):<20}| {item.get("match"):<18}| {item.get("goal"):<12}| {item.get("assists"):<12}| {item.get('perform',"Chưa tính toán")}| {item.get('rank',"Chưa tính toán")} ")

def main():
    menu()
    player = [{
        "id": "CT005",
        "name": "Nguyen Quang Hai",
        "match": 10,
        "goal": 5,
        "assists":4, 
        # "perform": 0
        # "rank": 0  
    },
    {
        "id": "CT006",
        "name": "Nguyen Tuan",
        "match": 15,
        "goal": 9,
        "assists":20,    
        # "perform": 0
        # "rank": 0

    }
    ]
    while True:
        choice = input("Lựa chọn của bạn: ")
        match choice :
            case '1':
                show_player(player)
            case '2':
                add_player(player)
            case '3':
                upd_player(player)
            case '4':
                remove_player(player)
            case '5':
                search_player(player)
            case '6':
                print()
            case '7':
                print()
            case '8':
                print("Đã thoát chương trình")
                break
            case _:
                print("Lựa chọn không hợp lệ!")
                

main()