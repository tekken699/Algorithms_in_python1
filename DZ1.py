import collections

amount_fab = int(input('Введите количество предприятий'))

companies = collections.defaultdict()
prof_c = collections.deque()
unprof_c = collections.deque()
all_profit = 0
quarter = 4

for i in range(amount_fab):
    name_fab = input(f'Введите название {i+1}й компании')
    profit = 0
    q = 1
    while q <= quarter:
        profit += float(input(f'Введите прибыль {q}й кварталл'))
        q += 1
    companies[name_fab] = profit
    print(companies[name_fab])
    all_profit += profit

mid_profit = all_profit / amount_fab

for i, item in companies.items():
    if item >= mid_profit:
        prof_c.append(i)
    else:
        unprof_c.append(i)

print(f'Средняя прибыль для всех компаний составила: {mid_profit}')
print(f'Прибыль выше среднего у {len(prof_c)} компаний:')
print(f'Прибыль ниже среднего у {len(unprof_c)} компаний:')

