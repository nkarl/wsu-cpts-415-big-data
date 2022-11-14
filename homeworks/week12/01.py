class Person:
    def __init__(self, name: str):
        self.name: str = name


class User:
    def __init__(self, person, friends):
        self.person: Person     = person
        self.friends: list[str] = friends
        self.friends_count: int = len(self.friends)

    def __repr__(self):
        return f"({self.person.name}, {self.friends})"



def Map(i: User, j: User):
    person: User
    if (i.friends_count > j.friends_count):
        person = j
        return (person, i.friends)
    else:
        person = i
        return (person, j.friends)



def Reduce(user: User, others_friends: list[str]):
    potential: list[str] = list()
    if len(others_friends) == 0 or len(user.friends) == 0:
        return []
    else: 
        for name in others_friends:
            if name in user.friends:
                potential.append(name)
    return potential 


def MapReduce(i: User, j: User):
    user, others_friends = Map(i, j)
    common: list = Reduce(user, others_friends)
    return ((i, j), common)


John = Person('John')
Jane = Person('Jane')

a = User(Person('Jack'), [John.name, Jane])
b = User(Person('Mary'), [Jane])

print(a)
