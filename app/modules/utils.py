def cm_to_inch(cm):
    inches = cm / 2.54

    return round(inches, 1)

def cm_to_feet(cm):
    inches = cm / 2.54
    feet = int(inches / 12)
    inch = int(inches % 12)

    return {'ft': feet, 'in': inch}


sex_dict = {
    'm': 'Male',
    'f': 'Female'
}


if __name__ == '__main__':
    from pprint import pprint
    cm = 177
    inches = cm_to_inch(cm)
    feet = cm_to_feet(cm)

    pprint({
        'cm': cm,
        'inches': inches,
        'feet': feet
    })
