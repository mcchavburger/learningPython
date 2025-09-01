names = {
    'Dan' : 'Johnson',
    'Deb' : 'Johnson',
    'Fia' : 'Johnson',
    'Ri' : 'Johnson',
    'Ellisia' : 'Johnson'
}

try:
    missing = names['Charlie']
except:
    print('Charlie does not exist')
finally:
    for i in names:
        print("Only Names Availble",i)