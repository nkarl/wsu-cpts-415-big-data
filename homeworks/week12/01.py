class Person:
    def __init__(self, name: str):
        self.name = name

class User:
    def __init__(self, person, friends):
        self.person = person
        self.friends = friends
        self.friends_count = len(self.friends)



def Map(i: User, j: User):
    iterable_friends: tuple
    if (i.friends_count > j.friends_count):
        iterable_friends = (j, i.friends)
    else:
        iterable_friends = (i, j.friends)

    return iterable_friends


def Reduce(user: User, other_friendlist: list):
    common_friends = list()
    for person in other_friendlist:
        if person in user.friends:
            common_friends += [person]
    return common_friends


def MapReduce(i: User, j: User):
    user, others_friends = Map(i, j)
    common: list = Reduce(user, others_friends)
    return ((i, j), common)

