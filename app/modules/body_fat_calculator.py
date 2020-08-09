from math import log10

"""

    Height - make sure you stand up straight and barefoot.
    Neck - the circumference should be measured just underneath the larynx (Adam's apple).
    Waist - should be measured horizontally, around the narrowest part of the abdomen for women and at the at the navel level for men.
    Hips - should be measured at the widest part of the buttocks or hip.

"""


def us_navy_body_fat_standards(age, sex, body_fat_percentage):
    if age < 18:
        us_navy_body_fat_standards_met = False

    elif age >= 18 and age <= 21:
        if sex == 'm':
            if body_fat_percentage <= 22:
                us_navy_body_fat_standards_met = True
            else:
                us_navy_body_fat_standards_met = False
        else: # female
            if body_fat_percentage <= 33:
                us_navy_body_fat_standards_met = True
            else:
                us_navy_body_fat_standards_met = False


    elif age >= 22 and age <= 29:
        if sex == 'm':
            if body_fat_percentage <= 23:
                us_navy_body_fat_standards_met = True
            else:
                us_navy_body_fat_standards_met = False
        else: # female
            if body_fat_percentage <= 34:
                us_navy_body_fat_standards_met = True
            else:
                us_navy_body_fat_standards_met = False

    elif age >= 30 and age <= 39:
        if sex == 'm':
            if body_fat_percentage <= 24:
                us_navy_body_fat_standards_met = True
            else:
                us_navy_body_fat_standards_met = False
        else: # female
            if body_fat_percentage <= 35:
                us_navy_body_fat_standards_met = True
            else:
                us_navy_body_fat_standards_met = False

    elif age >= 40:
        if sex == 'm':
            if body_fat_percentage <= 26:
                us_navy_body_fat_standards_met = True
            else:
                us_navy_body_fat_standards_met = False
        else: # female
            if body_fat_percentage <= 36:
                us_navy_body_fat_standards_met = True
            else:
                us_navy_body_fat_standards_met = False

    return us_navy_body_fat_standards_met

def us_navy_body_fat_percentage(sex, height_cm, weight_kg, waist_cm, neck_cm, hip_cm=None):
    # Uses metric formula
    # https://www.omnicalculator.com/health/navy-body-fat#the-us-navy-body-fat-standards

    if sex == 'm':
        # body_fat_percentage = 86.010 * log10(waist - neck) - 70.041 * log10(height) + 30.30
        body_fat_percentage = 495 / ( 1.0324 - 0.19077 * log10( waist_cm - neck_cm ) + 0.15456 * log10( height_cm ) ) - 450
    else:
        # body_fat_percentage = 163.205 * log10(waist + hip - neck) - 97.684 * log10(height) - 104.912
        body_fat_percentage = 495 / ( 1.29579 - 0.35004 * log10( waist_cm + hip_cm - neck_cm ) + 0.22100 * log10( height_cm ) ) - 450


    fat_mass_kg = weight_kg * (body_fat_percentage / 100)
    lean_mass_kg = weight_kg - fat_mass_kg


    return round(body_fat_percentage, 1), round(fat_mass_kg, 1), round(lean_mass_kg, 1)


def us_navy_body_fat_percentage_male(sex, height_cm, weight_kg, waist_cm, neck_cm):
    # Uses metric formula
    # https://www.omnicalculator.com/health/navy-body-fat#the-us-navy-body-fat-standards

    # body_fat_percentage = 86.010 * log10(waist - neck) - 70.041 * log10(height) + 30.30

    body_fat_percentage = 495 / ( 1.0324 - 0.19077 * log10( waist_cm - neck_cm ) + 0.15456 * log10( height_cm ) ) - 450

    fat_mass_kg = weight_kg * (body_fat_percentage / 100)
    lean_mass_kg = weight_kg - fat_mass_kg


    return round(body_fat_percentage, 1), round(fat_mass_kg, 1), round(lean_mass_kg, 1)


def us_navy_body_fat_percentage_female(sex, height_cm, weight_kg, waist_cm, neck_cm, hip_cm):
    # Uses metric formula
    # https://www.omnicalculator.com/health/navy-body-fat#the-us-navy-body-fat-standards

    body_fat_percentage = 495 / ( 1.29579 - 0.35004 * log10( waist_cm + hip_cm - neck_cm ) + 0.22100 * log10( height_cm ) ) - 450


    fat_mass_kg = weight_kg * (body_fat / 100)
    lean_mass_kg = weight_kg - fat_mass_kg


    return round(body_fat_percentage, 1), round(fat_mass_kg, 1), round(lean_mass_kg, 1)


if __name__ == '__main__':
    pass
    # bf, fat_mass, lean_mass = us_navy_body_fat_percentage(
    #     sex='m',
    #     height=177,
    #     weight=77,
    #     waist=86,
    #     neck=39,
    #     hip=0
    # )
    #
    # print('Body fat: {}%'.format(bf))
    # print('Fat mass: {}kg'.format(fat_mass))
    # print('Lean mass: {}kg'.format(lean_mass))
    # print('Weight: {}kg'.format(lean_mass+fat_mass))
