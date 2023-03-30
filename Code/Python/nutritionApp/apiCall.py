import requests
import json

# Required Vars:
app_id = 'da882c7a'
api_key = '8e742f0e087a388c85aca0f739a33764'

HEADERS = {
    'x-app-id': app_id,
    'x-app-key': api_key,
    'content-type': 'application/json'
}

end_pt_url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'

def apiResults(item):
    query = {
        "query": item
    }

    r = requests.post(end_pt_url, headers=HEADERS, json=query)
    data = json.loads(r.text)
    new_string = json.dumps(data, indent=2)
    print(new_string)

    print('FOR LOOP')
    for nutritionvalue in data['foods']:
        servingSize = nutritionvalue['serving_weight_grams']
        calories = nutritionvalue['nf_calories']
        fat = nutritionvalue['nf_total_fat']
        cholesterol = nutritionvalue['nf_cholesterol']
        sodium = nutritionvalue['nf_sodium']
        carb = nutritionvalue['nf_total_carbohydrate']
        sugars = nutritionvalue['nf_sugars']
        protein = nutritionvalue['nf_protein']
        print(servingSize, calories, fat, cholesterol, sodium, carb, sugars, protein)
        return [servingSize, calories, fat, cholesterol, sodium, carb, sugars, protein]