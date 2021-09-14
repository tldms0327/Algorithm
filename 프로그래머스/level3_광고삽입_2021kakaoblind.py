def solution(play_time, adv_time, logs):
    adv_time = time_converter(adv_time)
    play_time = time_converter(play_time)
    watch_logs = [0 for _ in range(play_time + 1)]
    print(play_time, adv_time, len(watch_logs))

    for log in logs:
        s = log.split("-")
        start, end = time_converter(s[0]), time_converter(s[1])
        watch_logs[start] += 1
        watch_logs[end] -= 1

    for i in range(1, play_time):
        watch_logs[i] += watch_logs[i - 1]

    temp = sum(watch_logs[:adv_time])
    max_time = temp
    answer = 0
    s, e = 0, adv_time
    while e < play_time:
        if temp - watch_logs[s] + watch_logs[e] > max_time:
            max_time = temp - watch_logs[s] + watch_logs[e]
            answer = s + 1
        temp = temp - watch_logs[s] + watch_logs[e]
        s += 1
        e += 1

    hh, mm, ss = answer // 3600, (answer % 3600) // 60, answer % 60

    return f"{str(hh).zfill(2)}:{str(mm).zfill(2)}:{str(ss).zfill(2)}"


def time_converter(s):
    time = list(map(int, s.split(":")))
    return 3600 * time[0] + 60 * time[1] + time[2]


p = "99:59:59"
a = "25:00:00"
l = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
print(solution(p, a, l))
