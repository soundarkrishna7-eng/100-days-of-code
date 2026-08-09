def car_fleet(target, position, speed):
    pairs = sorted(zip(position, speed), reverse=True)
    stack = []
    for position, speed in pairs:
        calculated_time = (target - position) / speed
        if stack == [] or calculated_time > stack[-1]:
            stack.append(calculated_time)

    return len(stack)

print(car_fleet(12, [10,8,0,5,3], [2,4,1,1,3]))  # expected: 3
print(car_fleet(10, [3], [3]))                     # expected: 1
print(car_fleet(100, [0,2,4], [4,2,1]))            # expected: 1