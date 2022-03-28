deposed_sum = float(input())
pay_time = int(input())
yearly_smth = float(input())

accumulated_interest = deposed_sum * (yearly_smth / 100)
interest_one = (accumulated_interest / 12)
result = deposed_sum + pay_time * interest_one

print(result)
