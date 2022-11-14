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


# for every pair of users <i,j>, pair the person with the small friendship
# to the friendship of the other person.
def Map(i: User, j: User):
    if (i.friends_count > j.friends_count):
        return (i.friendship, j)
    else:
        return (j.friendship, i)



# for every person in the potential list
def Reduce(potential: dict[str, Person], target: User):
    if len(potential) == 0 or len(target.friendship) == 0:
        return {}
    else: 
        common: dict[str, Person] = dict()
        for person in potential:
            if person in target.friendship:
                common[person] = potential[person]
        return common


def MapReduce(i: User, j: User):
    potential, target = Map(i, j)
    common: dict[str, Person] = Reduce(potential, target)
    user_pair = sorted([i.person.name, j.person.name])
    return (tuple(user_pair), common)


def main():
    Alice = Person('Alice')
    Bob   = Person('Bob')
    John  = Person('John')
    Jane  = Person('Jane')
    
    a = User(Person('Jack'), {
        f"{Bob}": Bob,
        f"{Jane}": Jane,
        f"{Alice}": Alice,
        "f{John}": John
    })
    b = User(Person('Mary'), {
        f"{Jane}": Jane,
        f"{Bob}": Bob,
        f"{Alice}": Alice
    })
    
    result = MapReduce(a, b)
    
    for person in result[1]:
        print(result[1][person].name)


if __name__ == "__main__":
    main()
