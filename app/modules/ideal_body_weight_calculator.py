from app.modules import utils
from statistics import mean

def inches_over_five_ft(height_cm):
    inches = utils.cm_to_inch(height_cm)
    inches_over_five_ft = inches - 60
    if inches_over_five_ft > 0:
        pass
    else:
        inches_over_five_ft = 0

    return inches_over_five_ft


def gj_hamwi(sex, height_cm):
    inch_over_five_ft = inches_over_five_ft(height_cm)

    if sex == 'm':
        ibw_kg = 48.0 + (2.7 * inch_over_five_ft)
    else:
        ibw_kg = 45.5 + (2.2 * inch_over_five_ft)

    return round(ibw_kg, 1)


def bj_devine(sex, height_cm):
    inch_over_five_ft = inches_over_five_ft(height_cm)

    if sex == 'm':
        ibw_kg = 50.0 + (2.3 * inch_over_five_ft)
    else:
        ibw_kg = 45.5 + (2.3 * inch_over_five_ft)

    return round(ibw_kg, 1)


def jd_robinson(sex, height_cm):
    inch_over_five_ft = inches_over_five_ft(height_cm)

    if sex == 'm':
        ibw_kg = 52 + (1.9 * inch_over_five_ft)
    else:
        ibw_kg = 49 + (1.7 * inch_over_five_ft)

    return round(ibw_kg, 1)


def dr_miller(sex, height_cm):
    inch_over_five_ft = inches_over_five_ft(height_cm)

    if sex == 'm':
        ibw_kg = 56.2 + (1.41 * inch_over_five_ft)
    else:
        ibw_kg = 53.1 + (1.36 * inch_over_five_ft)

    return round(ibw_kg, 1)


def broca(sex, height_cm):
    inch_over_five_ft = inches_over_five_ft(height_cm)

    if sex == 'm':
        ibw_kg = (height_cm - 100) - ((height_cm -100) * 0.1)
    else:
        ibw_kg = (height_cm - 100) - ((height_cm -100) * 0.15)

    return round(ibw_kg, 1)


def peterson(height_cm):
    # https://www.topendsports.com/testing/tests/peterson-equation.htm
    bmi_target = 22
    height_m = height_cm / 100.0

    ibw_kg = 2.2 * bmi_target + 3.5 * bmi_target * (height_m - 1.5)

    return round(ibw_kg, 1)


def average_ideal_weight_kg_all_formulas(sex, height_cm):
    ideal_weight_kg_jdr = jd_robinson(sex, height_cm)
    ideal_weight_kg_drm = dr_miller(sex, height_cm)
    ideal_weight_kg_bjd = bj_devine(sex, height_cm)
    ideal_weight_kg_gjh = gj_hamwi(sex, height_cm)
    ideal_weight_kg_broca = broca(sex, height_cm)
    ideal_weight_kg_peterson = peterson(height_cm)

    ideal_weight_kg_list = [
        ideal_weight_kg_jdr,
        ideal_weight_kg_drm,
        ideal_weight_kg_bjd,
        ideal_weight_kg_gjh,
        ideal_weight_kg_broca,
        ideal_weight_kg_peterson
    ]

    average = mean(ideal_weight_kg_list)

    return round(average, 1), ideal_weight_kg_jdr, ideal_weight_kg_drm, ideal_weight_kg_bjd, ideal_weight_kg_gjh, ideal_weight_kg_broca, ideal_weight_kg_peterson

if __name__ == '__main__':
    sex = 'm'
    height_cm = 177

    ideal_weight_kg_jdr = jd_robinson(sex=sex, height_cm=height_cm)
    print('ideal_weight_kg_jdr: {}kg'.format(ideal_weight_kg_jdr))

    ideal_weight_kg_drm = dr_miller(sex=sex, height_cm=height_cm)
    print('ideal_weight_kg_drm: {}kg'.format(ideal_weight_kg_drm))

    ideal_weight_kg_bjd = bj_devine(sex=sex, height_cm=height_cm)
    print('ideal_weight_kg_bjd: {}kg'.format(ideal_weight_kg_bjd))

    ideal_weight_kg_gjh = gj_hamwi(sex=sex, height_cm=height_cm)
    print('ideal_weight_kg_gjh: {}kg'.format(ideal_weight_kg_gjh))

    ideal_weight_kg_broca = broca(sex=sex, height_cm=height_cm)
    print('ideal_weight_kg_broca: {}kg'.format(ideal_weight_kg_broca))

    ideal_weight_kg_average, ideal_weight_kg_jdr, ideal_weight_kg_drm, ideal_weight_kg_bjd, ideal_weight_kg_gjh, ideal_weight_kg_broca = average_ideal_weight_kg_all_formulas(sex=sex, height_cm=height_cm)
    print('ideal_weight_kg_average: {}kg'.format(ideal_weight_kg_average))
