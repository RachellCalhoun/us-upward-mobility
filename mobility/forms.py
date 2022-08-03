
from secrets import choice
from django import forms

class MetricForm(forms.Form):

    METRIC_CHOICES = (
        ('proportion_homeless', 'Proportion Homeless'),
        ('HPSA Score', 'HPSA Score'),
        ('proportion_voter', 'Proportion Voter'),
        ('proportion_high_poverty_neighborhood',
         'Proportion High Poverty Neighborhood'),

        ('median_family_income', 'Median Family Income'),
        ('income_20_percentile', 'Income 20 Percentile'),
        ('income_80_percentile', 'Income 80 Percentile'),
        ('median_family_income_white', 'Median Family Income White'),
        ('median_family_income_black', 'Median Family Income Black'),
        ('median_family_income_indigenous', 'Median Family Income Indigenous'),
        ('median_family_income_asian', 'Median Family Income Asian'),
        ('median_family_income_hispanic', 'Median Family Income Hispanic'),

        ('low_birth_rate', 'Low Birth Rate'),
        ('Not Hispanic or Latino_low_birth_rate',
         'Not Hispanic Or Latino Low Birth Rate'),
        ('Hispanic or Latino_low_birth_rate',
         'Hispanic Or Latino Low Birth Rate'),
        ('Unknown or Not Stated_low_birth_rate',
         'Unknown Or Not Stated Low Birth Rate'),
        ('Black or African American_low_birth_rate',
         'Black Or African American Low Birth Rate'),
        ('White_low_birth_rate', 'White Low Birth Rate'),
        ('Asian_low_birth_rate', 'Asian Low Birth Rate'),
        ('More than one race_low_birth_rate',
         'More Than One Race Low Birth Rate'),
        ('American Indian or Alaska Native_low_birth_rate',
         'American Indian Or Alaska Native Low Birth Rate'),
        ('Native Hawaiian or Other Pacific Islander_low_birth_rate',
         'Native Hawaiian Or Other Pacific Islander Low Birth Rate'),

        ('hispanic_or_latino_exposure', 'Hispanic Or Latino Exposure'),
        ('white_exposure', 'White Exposure'),
        ('black_exposure', 'Black Exposure'),
        ('native_american_exposure', 'Native American Exposure'),
        ('Asian Exposure', 'asian_exposure'),
        ('hawaiian_exposure', 'Hawaiian Exposure'),
        ('some_other_race_alone_exposure',
         'Some Other Race Alone Exposure'),
        ('two_more_races_exposure', 'Two More Races Exposure'),

        ('transit_trips_index', 'Transit Trips Index'),
        ('transit_low_cost_index', 'Transit Low Cost Index'),
        ('crime_rate', 'Crime Rate'),

        ('juvenile_crime_rate', 'Juvenile Crime Rate'),
        ('avg_edu_prof_diff', 'Avg Edu Prof Diff'),

        ('preschool_enroll', 'Preschool Enroll'),
        ('white_under_5', 'White Under 5'),
        ('black_under_5', 'Black Under 5'),
        ('indigenous_under_5', 'Indigenous Under 5'),
        ('asian_under_5', 'Asian Under 5'),
        ('hispanic_under_5', 'Hispanic Under 5'),
        ('two_or_more_race_under_5', 'Two Or More Race Under 5'),
        ('some_other_race_under_5', 'Some Other Race Under 5'),
        ('preschool_enrollment_white', 'Preschool Enrollment White'),
        ('preschool_enrollment_black', 'Preschool Enrollment Black'),
        ('preschool_enrollment_hispanic', 'Preschool Enrollment Hispanic'),
        ('preschool_enrollment_indigenous', 'Preschool Enrollment Indigenous'),
        ('preschool_enrollment_asian', 'Preschool Enrollment Asian'),

        ('population', 'Population'),
        ('white_employed_16_64', 'White Employed 16 64'),
        ('black_employed_16_64', 'Black Employed 16 64'),
        ('american_indian_employed_16_64', 'American Indian Employed 16 64'),
        ('asian_employed_16_64', 'Asian Employed 16 64' ),
        ('some_other_race_alone_employed_16_64', 'Some Other Race Alone Employed 16 64'),
        ('two_or_more_race_employed_16_64', 'Two Or More Race Employed 16 64'),
        ('hispanic_or_latino_employed_16_64', 'Hispanic Or Latino Employed 16 64'),
        ('employed_25_54_population', 'Employed 25 54 Population'),
        ('employed_16_64_population', 'Employed 16 64 Population')

    )

    metric = forms.ChoiceField(choices=METRIC_CHOICES)
