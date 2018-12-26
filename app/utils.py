from random import randint

yes_or_no_keywrods = [
    ['Yes', 'Yup', 'Yeah', 'Yea', 'Sure'],
    ['No', 'Nay', 'Nope', 'Nah', 'No way']
]


def yes_or_no():
    return yes_or_no_keywrods[randint(0, 1)][randint(0, 4)]
