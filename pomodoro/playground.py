check_mark = ''
reps = 1

for reps in range(8):
    if reps % 2 == 0:
        check_mark = check_mark + '✔'

print(check_mark)