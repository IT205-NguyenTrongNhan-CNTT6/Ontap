# import sys

def menu():
    print("=" * 60)
    print("1. Hiển thị danh sách cầu thủ\n" +
          "2. Tiếp nhận cầu thủ mới\n" +
          "3. Cập nhật thông tin và chỉ số\n" +
          "4. Xóa cầu thủ\n" +
          "5. Tìm kiếm cầu thủ\n" +
          "6. Thống kê loại phong độ\n" +
          "7. Đánh giá phong độ tự động\n" +
          "8. Thoát!")
    print("=" * 60)

def validate_input(prompt: str, input_type: str = "string"):
    while True:
        user_input = input(prompt)
        if not user_input:
            print("Dữ liệu không được để trống, Nhập lại!")
            continue
        
        if input_type == "int":
            try:
                value = int(user_input)
                if value < 0:
                    print("Dữ liệu phải là số nguyên dương!")
                    continue
                return value
            except ValueError:
                print("Dữ liệu không hợp lệ, Nhập lại!")
                continue

        if input_type == "match":
            try:
                value = int(user_input)
                if value < 0 or value > 50:
                    print("Dữ liệu phải nằm trong khoảng từ 0 đến 50")
                    continue
                return value
            except ValueError:
                print("Dữ liệu không hợp lệ, Nhập lại!")
                continue
        return user_input

def classify_player(perform_player):
    if perform_player < 15:
        return "Cần thanh lý"
    elif perform_player < 30:
        return "Dự bị"
    elif perform_player < 50:
        return "Trụ cột"
    else:
        return "Ngôi sao"

def display_players(players: list[dict]):
    if not players:
        print("Danh sách cầu thủ rỗng!")
        return
    print("====Danh sách cầu thủ=====")
    print(f"{"Mã CT":<8} | {"Họ tên":<20} | {"Số trận đấu":<15} | {"Số bàn thắng":<15} | {"Số kiến tạo":<15} | {"Hiệu suất":<15} | {"Phong độ":<20}")

    for player in players:
        print(f"{player.get('id').upper():<8} | {player.get('name'):<20} | {player.get('match'):<15} | {player.get('goal'):<15} | {player.get('assist'):<15} | {player.get('perform', 'Chưa tính toán'):<15} | {player.get('rank', 'Chưa tính toán'):<20}")

def add_player(players):
    while True:
        id_player = validate_input("Nhập vào mã cầu thủ: ")
        for player in players:
            if (id_player.lower() == player.get("id").lower()):
                print("Mã cầu thủ trùng lặp, Nhập lại")
                break
        else:
            name_player = validate_input("Nhập vào tên cầu thủ: ")
            match_player = validate_input("Nhập vào số trận đấu: ", "match")
            goal_player = validate_input("Nhập vào số bàn thắng: ", "int")
            assist_player = validate_input("Nhập vào số kiến tạo: ", "int")
            perform_player = (match_player * 1) + (goal_player * 3) + (assist_player * 2)
            
            new_player = { 
                "id": id_player, 
                "name": name_player, 
                "match": match_player, 
                "goal": goal_player, 
                "assist": assist_player,
                "perform": perform_player,
                "rank": classify_player(perform_player)
            }
            players.append(new_player)
            break

def update_player(players):
    if not players:
        print("Danh sách cầu thủ rỗng!")
        return
    id_update = validate_input("Nhập vào mã cầu thủ cần cập nhật: ")
    for player in players:
        if (id_update.lower() == player.get("id").lower()):
            print("Đã tìm thấy, hãy nhập thông tin mới!")
            match_player = validate_input("Nhập vào số trận đấu: ", "match")
            goal_player = validate_input("Nhập vào số bàn thắng: ", "int")
            assist_player = validate_input("Nhập vào số kiến tạo: ", "int")
            perform_player = (match_player * 1) + (goal_player * 3) + (assist_player * 2)
            player["match"] = match_player
            player["goal"] = goal_player
            player["assist"] = assist_player
            player["perform"] = perform_player
            player["rank"] = classify_player(perform_player)
            print("Đã tiến hành cập nhật!")
            break
    else:
        print("Không tìm thấy cầu thủ")

def remove_player(players):
    if not players:
        print("Danh sách cầu thủ rỗng!")
        return
    id_delete = validate_input("Nhập vào mã cầu thủ cần xóa: ")
    for player in players:
        if (id_delete.lower() == player.get("id").lower()):
            players.remove(player)
            print("Cầu thủ đã thanh lý!")
            break
    else:
        print("Không tìm thấy cầu thủ!")

def search_player(players):
    if not players:
        print("Danh sách cầu thủ rỗng!")
        return
    input_search = validate_input("Nhập vào Mã hoặc tên cầu thủ cần tìm: ")
    find_player = []
    for player in players:
        if (input_search.lower() == player.get("id").lower() or input_search.lower() in player.get("name").lower()):
            find_player.append(player)
    if not find_player:
        print("Không tìm thấy!")
    else:
        display_players(find_player)

def chart_player(players):
    player_star = 0
    player_core = 0
    player_mechalin = 0
    player_buy = 0
    for player in players:
        if player.get("rank") == "Ngôi sao":
            player_star += 1
        elif player.get("rank") == "Trụ cột":
            player_core += 1
        elif player.get("rank") == "Dự bị":
            player_mechalin += 1
        elif player.get("rank") == "Cần thanh lý":
            player_buy += 1
    print(f"Danh sách cầu thủ ngôi sao là: {player_star}")
    print(f"Danh sách cầu thủ trụ cột là: {player_core}")
    print(f"Danh sách cầu thủ dự bị là: {player_mechalin}")
    print(f"Danh sách cầu thủ cần thanh lý là: {player_buy}")
    

def main():
    players = [
        {"id": "CT001", "name": "Nguyên", "match": 10, "goal": 20, "assist": 40},
        {"id": "CT002", "name": "Nhật Huy", "match": 10, "goal": 2, "assist": 6}
    ]
    while True:
        menu()
        choice = input("Nhập vào lựa chọn của bạn (1-8): ")
        match choice:
            case "1":
                display_players(players)
            case "2":
                add_player(players)
            case "3":
                update_player(players)
            case "4":
                remove_player(players) 
            case "5":
                search_player(players)
            case "6":
                chart_player(players)
            case "8":
                print("Thoát chương trình!")
                break
                # sys.exit(0) 
            case _:
                print("Lựa chọn không hợp lệ!")

main()