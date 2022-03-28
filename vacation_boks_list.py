pages = int(input())
pages_for_one_hour = int(input())
days = int(input())

total_time_for_reading_a_book = pages / pages_for_one_hour
needed_hours = total_time_for_reading_a_book / days

print(round(needed_hours))
