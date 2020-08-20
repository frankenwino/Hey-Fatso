from flask import render_template, flash, redirect
from app import app
from app.forms import TDCEForm, IdealBodyWeightForm, BodyFatForm, BodyFatFormMale, BodyFatFormFemale
from app.modules import basal_metabolic_rate_calculator, ideal_body_weight_calculator, utils, body_fat_calculator

# @app.route('/')
# @app.route('/index')
# def index():
#     user = {'username': 'Fatso'}
#     return render_template('index.html', title='Home', user=user)


@app.route('/')
@app.route('/index')
@app.route('/tdce', methods=['GET', 'POST'])
def tdce():
    form = TDCEForm()

    if form.validate_on_submit():
        sex, activity_level, basal_metabolic_rate, daily_maintenance_calories, formula, formula_url = basal_metabolic_rate_calculator.calculate_tdee(sex=form.sex.data, weight_kg=form.weight_kg.data, height_cm=form.height_cm.data, age=form.age.data, activity_level=form.activity_level.data, body_fat_percentage=form.body_fat_percentage.data)
        calorie_deficit = daily_maintenance_calories - 1200
        weight_loss = round(calorie_deficit * 7 / 7000, 1)
        return render_template(
            'tdce_result.html',
            sex=utils.sex_dict[form.sex.data],
            weight_kg=form.weight_kg.data,
            height_cm=int(round(form.height_cm.data)),
            age=int(form.age.data),
            activity_level=activity_level,
            body_fat_percentage=form.body_fat_percentage.data,
            basal_metabolic_rate=basal_metabolic_rate,
            daily_maintenance_calories=daily_maintenance_calories,
            formula=formula,
            formula_url=formula_url,
            calorie_deficit=calorie_deficit,
            weight_loss_weekly=weight_loss
        )

    return render_template('tdce.html', title='TDCE', form=form)


@app.route('/ideal_body_weight', methods=['GET', 'POST'])
def ideal_body_weight():
    form = IdealBodyWeightForm()
    if form.validate_on_submit():
        ideal_weight_kg_average, ideal_weight_kg_jdr, ideal_weight_kg_drm, ideal_weight_kg_bjd, ideal_weight_kg_gjh, ideal_weight_kg_broca, ideal_weight_kg_peterson = ideal_body_weight_calculator.average_ideal_weight_kg_all_formulas(sex=form.sex.data, height_cm=form.height_cm.data)

        return render_template(
            'ideal_body_weight_result.html',
            sex=utils.sex_dict[form.sex.data],
            height_cm=int(round(form.height_cm.data)),
            ideal_weight_kg_peterson=ideal_weight_kg_peterson,
            ideal_weight_kg_jdr=ideal_weight_kg_jdr,
            ideal_weight_kg_drm=ideal_weight_kg_drm,
            ideal_weight_kg_bjd=ideal_weight_kg_bjd,
            ideal_weight_kg_gjh=ideal_weight_kg_gjh,
            ideal_weight_kg_broca=ideal_weight_kg_broca,
            ideal_weight_kg_average=ideal_weight_kg_average
        )

    return render_template('ideal_body_weight.html', title='Ideal Body Weight', form=form)


# @app.route('/body_fat', methods=['GET', 'POST'])
# def body_fat():
#     form = BodyFatForm()
#     if form.validate_on_submit():
#         body_fat, fat_mass_kg, lean_mass_kg = body_fat_calculator.us_navy_body_fat_percentage(
#             sex=form.sex.data,
#             height_cm=form.height_cm.data,
#             weight_kg=form.weight_kg.data,
#             waist_cm=form.waist_cm.data,
#             neck_cm=form.neck_cm.data,
#             hip_cm=form.hip_cm.data
#         )
#
#         # ideal_weight_kg_average, ideal_weight_kg_jdr, ideal_weight_kg_drm, ideal_weight_kg_bjd, ideal_weight_kg_gjh, ideal_weight_kg_broca = ideal_body_weight_calculator.average_ideal_weight_kg_all_formulas(sex=form.sex.data, cm=form.height_cm.data)
#
#         return render_template(
#             'body_fat_result.html',
#             sex=utils.sex_dict[form.sex.data],
#             height_cm=int(round(form.height_cm.data)),
#             body_fat_percentage=body_fat,
#             fat_mass_kg=fat_mass_kg,
#             lean_mass_kg=lean_mass_kg
#         )
#
#     return render_template('body_fat.html', title='Body Fat Percentage', form=form)


@app.route('/body_fat', methods=['GET', 'POST'])
def body_fat():
    # form = BodyFatForm()
    male_form = BodyFatFormMale()
    female_form = BodyFatFormFemale()
    if male_form.validate_on_submit() and not female_form.validate_on_submit():
        body_fat_percentage, fat_mass_kg, lean_mass_kg = body_fat_calculator.us_navy_body_fat_percentage_male(
            sex=male_form.sex,
            height_cm=male_form.height_cm.data,
            weight_kg=male_form.weight_kg.data,
            waist_cm=male_form.waist_cm.data,
            neck_cm=male_form.neck_cm.data
        )

        meets_us_navy_standard = body_fat_calculator.us_navy_body_fat_standards(
            age=male_form.age.data,
            sex=male_form.sex,
            body_fat_percentage=body_fat_percentage
            )


        return render_template(
            'body_fat_result.html',
            sex=utils.sex_dict[male_form.sex],
            height_cm=int(round(male_form.height_cm.data)),
            body_fat_percentage=body_fat_percentage,
            fat_mass_kg=fat_mass_kg,
            lean_mass_kg=lean_mass_kg,
            meets_us_navy_standard=meets_us_navy_standard
        )
    elif female_form.validate_on_submit() and male_form.validate_on_submit():
        body_fat_percentage, fat_mass_kg, lean_mass_kg = body_fat_calculator.us_navy_body_fat_percentage_female(
            sex=female_form.sex,
            height_cm=female_form.height_cm.data,
            weight_kg=female_form.weight_kg.data,
            waist_cm=female_form.waist_cm.data,
            neck_cm=female_form.neck_cm.data,
            hip_cm=female_form.hip_cm.data
        )

        meets_us_navy_standard = body_fat_calculator.us_navy_body_fat_standards(
            age=female_form.age.data,
            sex=female_form.sex,
            body_fat_percentage=body_fat_percentage
            )

        return render_template(
            'body_fat_result.html',
            sex=utils.sex_dict[female_form.sex],
            height_cm=int(round(female_form.height_cm.data)),
            body_fat_percentage=body_fat_percentage,
            fat_mass_kg=fat_mass_kg,
            lean_mass_kg=lean_mass_kg,
            meets_us_navy_standard=meets_us_navy_standard
        )


    return render_template(
        'body_fat_tabs.html',
        title='Body Fat Percentage',
        male_form=male_form,
        female_form=female_form
    )
