def Map(R: list[list[str]]):
	bag: dict[str, int] = dict()
	for r in R:
		for word in r:
			bag[word] = bag.get(word, 0) + 1
	return bag

def Reduce(bag: dict[str, int]):
	dict(sorted(bag.items(), key=lambda item: item[1]))
	return list(bag.items())[-1][0]

