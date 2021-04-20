import json
import pandas as pd


patients_data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg":85 },
                { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166,"WeightKg": 62},
                {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female","HeightCm": 167, "WeightKg": 82}]

def calculate_bmi(patients_data):
    patients_data = json.dumps(patients_data)
    df = pd.read_json(patients_data)
    data_frame = pd.DataFrame(df)
    # print(df.to_string())
    # print(data_frame)
    data_frame['BMI'] = data_frame['WeightKg'] / ((data_frame['HeightCm']/100)**2)
    data_frame.loc[data_frame['BMI'] <= 18.4, 'BMI Category'] = 'Under Weight'
    data_frame.loc[data_frame['BMI'] <= 18.4, 'Health Risk'] = 'Malnutrition Risk'

    data_frame.loc[(18.5 <= data_frame['BMI']) & (data_frame['BMI'] < 25), 'BMI Category'] = 'Normal Weight'
    data_frame.loc[(18.5 <= data_frame['BMI']) & (data_frame['BMI'] < 25), 'Health Risk'] = 'Low Risk'

    data_frame.loc[(25 <= data_frame['BMI']) & (data_frame['BMI'] < 30), 'BMI Category'] = 'Over Weight'
    data_frame.loc[(25 <= data_frame['BMI']) & (data_frame['BMI'] < 30), 'Health Risk'] = 'Enhanced Risk'

    data_frame.loc[(30 <= data_frame['BMI']) & (data_frame['BMI'] < 35), 'BMI Category'] = 'Moderately Obese'
    data_frame.loc[(30 <= data_frame['BMI']) & (data_frame['BMI'] < 35), 'Health Risk'] = 'Medium Risk'

    data_frame.loc[(35 <= data_frame['BMI']) & (data_frame['BMI'] < 40), 'BMI Category'] = 'Severely Obese'
    data_frame.loc[(35 <= data_frame['BMI']) & (data_frame['BMI'] < 40), 'Health Risk'] = 'High Risk'

    data_frame.loc[data_frame['BMI'] >= 40, 'BMI Category'] = 'Very Severely Obese'
    data_frame.loc[data_frame['BMI'] >= 40, 'Health Risk'] = 'Very High Risk'
    

    return data_frame

result = calculate_bmi(patients_data)
print(f"Final Result : {result}")