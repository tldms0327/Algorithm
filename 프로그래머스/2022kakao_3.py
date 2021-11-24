from collections import defaultdict
from math import ceil


def solution(fees, records):
    answer = []
    cars = []
    basic_time, basic_fee, per_time, per_fee = fees
    in_time = defaultdict(list)
    out_time = defaultdict(list)
    for r in records:
        time, car, status = r.split()
        if status == 'IN':
            in_time[car].append(converter(time))
        else:
            out_time[car].append(converter(time))
        cars.append(car)
    cars = sorted(list(set(cars)))
    for car in cars:
        intime = in_time[car]
        outtime = out_time[car]
        if len(intime) != len(outtime):
            total_time = converter('23:59') + sum(outtime) - sum(intime)
        else:
            total_time = sum(outtime) - sum(intime)
        if total_time <= basic_time:
            answer.append(basic_fee)
        else:
            answer.append(basic_fee + ceil((total_time - basic_time) / per_time) * per_fee)

    return answer


def converter(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m


F = [180, 5000, 10, 600]
R = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
     "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(F, R))
