a = input()
b = input()
cnt = [0] * 26
offset = ord('a')
for char in a:
	cnt[ord(char) - offset] += 1
print(cnt)
for char in b:
	cnt[ord(char) - offset] -= 1
	print(cnt)
total = 0
print(cnt)
for value in cnt:
	total += abs(value)
print(total)