import copy

original = [1,2,3]
# target = original
target = copy.deepcopy(original)
print(original, target)
original[0] = 10000
print(original, target)

#e동일한 디렉토리인 모듈에서 찾음
