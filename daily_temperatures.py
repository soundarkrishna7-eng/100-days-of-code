def daily_temperatures(temperatures):
    result = [0] * len(temperatures)
    days = []
    for i in range(len(temperatures)):
        while days != [] and temperatures[i] > temperatures[days[-1]]:
            idx = days.pop()
            result[idx] = i - idx
        days.append(i)

    return result

print(daily_temperatures([73,74,75,71,69,72,76,73]))  
print(daily_temperatures([30,40,50,60]))              
print(daily_temperatures([30,60,90]))     