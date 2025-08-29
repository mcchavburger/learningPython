contacts = {
    'students': [
        {
            "name": "Dave waterfield",
            "email" : "fatDave@hotmail.com",
            "age" : 42
        },
        {
            "name": "Mark Fox",
            "email" : "fastfingersfox@hotmail.com",
            "age" : 41
        },
        {
            "name": "James Webb",
            "email" : "webber@hotmail.com",
            "age" : 44
        },
        {
            "name": "Paul Stone",
            "email" : "pags@hotmail.com",
            "age" : 39
        },
        {
            "name": "Dan Johnson",
            "email" : "Johnson@hotmail.com",
            "age" : 40
        }
    ]
}

for student  in contacts["students"]:
    print(student["email"])