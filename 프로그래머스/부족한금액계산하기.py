def solution(price, money, count):
    total_price = price * (count * (count + 1) // 2)
    answer = total_price - money

    return answer if answer > 0 else 0
