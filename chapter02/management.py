
food_list = ['바나나', '김치찌개', '삼겹살']

duple = True
# 메뉴
while duple:
    print("-" * 52)
    print('1. 목록 출력 | 2. 추가 | 3. 변경 | 4. 삭제 | 5. 종료')
    print("-" * 52)
    menu = int(input('관리 메뉴를 선택하세요. >>> '))
    if menu == 1:
        for i in food_list:
            print(i)
    elif menu == 2:
        add_menu = input('추가할 매뉴를 입력해주세요. >>> ')
        food_list.append(add_menu)
    elif menu == 3:
        change_menu = input('변경할 매뉴를 입력해주세요. >>> ')
        update_menu = input('변경할 이름을 입력해주세요. >>> ')
        for i in range(0, len(food_list)):
            if food_list[i] == change_menu:
                food_list[i] = update_menu
    elif menu == 4:
        print(food_list)
        delete_menu = input('삭제할 매뉴를 입력해주세요. >>> ')
        if food_list.__contains__(delete_menu):
            del food_list[food_list.index(delete_menu)]
        else:
            print('그런건 없습니다')
    elif menu == 5:
        print('프로그램을 종료합니다.')
        duple = False
    else:
        print('올바른 번호를 입력해주세요.')


