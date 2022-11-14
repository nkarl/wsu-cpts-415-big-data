class Person:
    def __init__(self, name: str):
        self.name: str = name


class User:
    def __init__(self, person: Person, friends: dict[str, Person]):
        self.person: Person                = person
        self.friendship: dict[str, Person] = friends
        self.friends_count: int            = len(self.friendship)

    def __repr__(self):
        return f"({self.person.name}, {[name for name in self.friendship]})"


def Map(i: User, j: User):
    if (i.friends_count > j.friends_count):
        return (j, i.friendship)
    else:
        return (i, j.friendship)



def Reduce(a: User, b_friendship: dict[str, Person]):
    if len(a.friendship) == 0 or len(b_friendship) == 0:
        return {}
    else: 
        common: dict[str, Person] = dict()
        for person in a.friendship:
            if person in b_friendship:
                common[person] = a.friendship[person]
        return common


def MapReduce(i: User, j: User):
    user, others_friends = Map(i, j)
    common: dict[str, Person] = Reduce(user, others_friends)
    friendship = sorted([i.person.name, j.person.name])
    return (tuple(friendship), common)


Alice = Person('Alice')
Bob   = Person('Bob')
John  = Person('John')
Jane  = Person('Jane')

a = User(Person('Jack'), {f"{Bob}": Bob, f"{Jane}": Jane, f"{Alice}": Alice, "f{John}": John})
b = User(Person('Mary'), {f"{Jane}": Jane, f"{Bob}": Bob, f"{Alice}": Alice})

result = MapReduce(a, b)

for person in result[1]:
    print(result[1][person].name)
