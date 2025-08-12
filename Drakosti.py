import random as rn
stat = []
sample = 1000000
for i in range(sample):
    dice_amount = rn.randint(1, 6)
    dur_value = 0
    prev_value = 9999999
    counter = 0

    while prev_value >= dur_value:
        for i in range(dice_amount):
            dur_value += rn.randint(1, 6)
        # print(prev_value, dur_value, dice_amount, counter % 2 + 1)
        if dur_value == prev_value:
            dur_value = 0
            continue
        if dice_amount > 1:
            dice_amount -= 1
        if prev_value > dur_value:
            prev_value = dur_value
            dur_value = 0

        else:
            # print('Игрок ' + str((counter % 2 + 1)) + ' проебал')
            stat.append(counter % 2 + 1)
            break
        counter += 1
print(str(int(stat.count(1)/sample * 100)) + '% - процент побед 1 игрока')
print(str(int(stat.count(2)/sample * 100)) + '% - процент побед 2 игрока')
