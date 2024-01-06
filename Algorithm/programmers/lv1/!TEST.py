my_dict = {'apple': [2, 1, 3], 'banana': [1, 2, 3], 'cherry': [3, 2, 1]}

# value의 첫 번째 요소를 기준으로 딕셔너리 정렬
sorted_dict = sorted(my_dict.items(), key=lambda item: item[1][0])

print(sorted_dict)