from pprint import pprint
import sys
from app.modules import utils


def bmr_mifflin(weight_kg, height_cm, age, activity_level, sex):
    if sex.lower() == 'm':
        diff = 5
    else:
        diff = -161

    basal_metabolic_rate = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + diff
    daily_maintenance_calories = basal_metabolic_rate * activity_level

    return int(round(basal_metabolic_rate)), int(round(daily_maintenance_calories))


def bmr_katch_mcardle(lean_body_mass_kg, activity_level):
    basal_metabolic_rate = 370 + (21.6 * lean_body_mass_kg)
    daily_maintenance_calories = basal_metabolic_rate * activity_level

    return int(round(basal_metabolic_rate)), int(round(daily_maintenance_calories))


def lean_body_mass_kg(sex, weight_kg, height_cm):
    """
    https://en.wikipedia.org/wiki/Lean_body_mass
    """

    # Boer equation
    lbm_formula = 'Boer'
    if sex == 'm':
        lbm_kg = (0.407 * weight_kg) + (0.267 * height_cm) - 19.2
    else:
        lbm_kg = (0.252 * weight_kg) + (0.473 * height_cm) - 48.3

    # # Hume equation
    # lbm_formula = 'Hume'
    # if sex == 'm':
    #     lbm_kg = (0.32810 * weight_kg) + (0.33929 * height_cm) - 29.5336
    # else:
    #     lbm_kg = (0.29569 * weight_kg) + (0.41813 * height_cm) - 43.2933

    return lbm_kg, lbm_formula



def calculate_tdee(sex, weight_kg, height_cm, age, activity_level, body_fat_percentage):
    if body_fat_percentage is None:
        formula = 'Mifflin-St Jeor'
        formula_url = 'https://en.wikipedia.org/wiki/Basal_metabolic_rate#BMR_estimation_formulas'

        basal_metabolic_rate, daily_maintenance_calories = bmr_mifflin(
            weight_kg=weight_kg,
            height_cm=height_cm,
            age=age,
            activity_level=activity_level_dict[activity_level]['multiplier'],
            sex=sex
        )


    else:
        lbm_kg, lbm_formula = lean_body_mass_kg(sex=sex, weight_kg=weight_kg, height_cm=height_cm)
        formula = 'Katch-McArdle (using {} for lean mass calculation.)'.format(lbm_formula)
        formula_url = 'https://en.wikipedia.org/wiki/Basal_metabolic_rate#BMR_estimation_formulas'



        basal_metabolic_rate, daily_maintenance_calories = bmr_katch_mcardle(
            lean_body_mass_kg=lbm_kg,
            activity_level=activity_level_dict[activity_level]['multiplier']
        )


    return utils.sex_dict[sex], activity_level_dict[activity_level]['note'], basal_metabolic_rate, daily_maintenance_calories, formula, formula_url


# valid_sex_choices = ['m', 'f']
# valid_activity_level_range = range(1,6)
activity_level_dict = {
    '1': {
        'note': 'Sedentary (little or no exercise)',
        'multiplier': 1.2
    },
    '2': {
        'note': 'Lightly active (light exercise or sports 1-3 days/week)',
        'multiplier': 1.375
    },
    '3': {
        'note': 'Moderately active (moderate exercise 3-5 days/week)',
        'multiplier': 1.55
    },
    '4': {
        'note': 'Very active (hard exercise 6-7 days/week)',
        'multiplier': 1.725
    },
    '5': {
        'note': 'Super active (very hard exercise and a physical job)',
        'multiplier': 1.9
    }
}


if __name__ == '__main__':
    pass
