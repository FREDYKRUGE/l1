number_of_chicken_menu = int(input())
number_of_fish_menu = int(input())
number_of_vege_menu = int(input())

price_for_chiken_menu = number_of_chicken_menu * 10.35
price_for_fish_menu = number_of_fish_menu * 12.40
price_for_vege_menu = number_of_vege_menu * 8.15
total_sum_for_menus = price_for_vege_menu + price_for_fish_menu + price_for_chiken_menu
desert_price = total_sum_for_menus * 0.20
total_sum = total_sum_for_menus + desert_price + 2.50

print(total_sum)