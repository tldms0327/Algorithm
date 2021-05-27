def solution(bridge_length, weight, truck_weights):
    time = 0
    passing =[]
    passing_time = []
    complete = []
    while truck_weights: # 대기중인 차가 없을 때까지
    	time +=1
    	if (sum(passing) + truck_weights[0] <= weight):
    		new = truck_weights.pop(0)
    		passing.append(new)
    		passing_time.append(0)    

    	for idx, truck in enumerate(passing):
    		passing_time[idx] += 1
    	if passing_time[0] >= bridge_length:
    		passing.pop(0)
    		passing_time.pop(0)
    

    if passing_time:
    	return time + bridge_length - passing_time[-1] +1
    else:
    	return time
    	
print(solution(2, 10, [7,4,5,6]))
