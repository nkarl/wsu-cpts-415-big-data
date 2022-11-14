class Person:
    def __init__(self, name: str):
        self.name: str = name


class User:
    """
    Each User object contains:
        - key:
            a Person, a unique object in database
        - value:
            friendship, a dict associated with the primary key, where each
            entry use the address of the person in database as key for
            uniqueness.
    """
    def __init__(self, person: Person, friends: dict[str, Person]):
        self.person: Person                = person
        self.friendship: dict[str, Person] = friends
        self.friends_count: int            = len(self.friendship)

    def __repr__(self):
        return f"({self.person.name}, {[name for name in self.friendship]})"


# for every pair of users <i,j>, pair the person with the small friendship
# to the friendship of the other person.
def Map(i: User, j: User):
    """
    Compare the two User objects and return a new 2-tuple:
        - first: the shorter friend list as upper bound for potential friends
        - second: the other person as target for matching
    """
    if (i.friends_count > j.friends_count):
        return (i.friendship, j)
    else:
        return (j.friendship, i)



def Reduce(potential: dict[str, Person], target: User):
    """
    From a list of potential friends and a target, check every
    key in the potential list against the target's frienship.
    Return the dictionary of common keys.
    """
    if len(potential) == 0 or len(target.friendship) == 0:
        return []
    else: 
        common: list[Person] = list()
        for person in potential:
            if person in target.friendship:
                common += [potential[person]]
        return common


def MapReduce(i: User, j: User):
    """
    Map and Reduce together.
    - key:
        the pair of users
    - value:
        a list of their common friends
    """
    potential, target = Map(i, j)
    common: list[Person] = Reduce(potential, target)
    user_pair = sorted([i.person.name, j.person.name])
    return {"pair": tuple(user_pair), "common": common}


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
    print(result["pair"], result["common"])
    

if __name__ == "__main__":
    main()
