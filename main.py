# part 1

person = [{
    'name': 'Mohammed Mansour',
    'age': '19',
    'hobbies': ['Birds' , 'gaming' , 'android']
},
]


print(person[0]['name'])
print(person[0]['age'])

# part 2

person[0]['age'] = '20'

person[0]['country'] = 'portugal'

print(person)
print(len(person))

# part 3

person[0]['hobbies'].append("Minecraft")


def check_hobbies(person):
    if len(person[0]['hobbies']) > 3:
        print("WOW YOU ARE AMAZING")

check_hobbies(person)



