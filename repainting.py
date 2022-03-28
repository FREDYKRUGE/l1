needed_vol_nylon = int(input())
needed_vol_paint = int(input())
vol_thinner = int(input())
hours_needed = int(input())
bags = 0.40

nylon = (needed_vol_nylon + 2) * 1.50
paint = (needed_vol_paint + (needed_vol_paint * 0.10)) * 14.50
thinner = vol_thinner * 5.00
total_sum = nylon + paint + thinner + bags
money_for_master = (total_sum * 0.30) * hours_needed
end_sum = total_sum + money_for_master

print(end_sum)