def solution(bridge_length, weight, truck_weights):
	q = []
	total_weight = truck_weights[0]
	q.append(truck_weights.pop(0))
	t = 0
	while q:
		t += 1
		if len(q) == bridge_length:
			total_weight -= q.pop(0)

		if truck_weights == []:
			break
		if (total_weight + truck_weights[0] <= weight):
			total_weight += truck_weights[0]
			q.append(truck_weights.pop(0))
		else:
			q.append(0)
		

	return t + bridge_length

print(solution(2, 10, [7,4,5,6]))