import json, csv

with open('Israel_2002.json', encoding='utf8') as file:  
    data = json.load(file)


#test_1 = {"id": 175957, "relid": "ISR-2002-3-666-4", "year": 2002, "active_year": False, "code_status": "Clear", "type_of_violence": 3, "conflict_dset_id": "666", "conflict_new_id": 483, "conflict_name": "Government of Israel - Civilians", "dyad_dset_id": "666", "dyad_new_id": 950, "dyad_name": "Government of Israel - Civilians", "side_a_dset_id": "666", "side_a_new_id": 121, "side_a": "Government of Israel", "side_b_dset_id": "9999", "side_b_new_id": 1, "side_b": "Civilians", "number_of_sources": 2, "source_article": "\"Agence France-Presse,2002-03-01,Israeli army kills Palestinian boy in Gaza Strip\";\"Reuters News,2002-03-01,Palestinian boy, 7, shot \"playing near Israeli tank\".\"", "source_office": "Agence France-Presse;Reuters News", "source_date": "2002-03-01;2002-03-01", "source_headline": "Israeli army kills Palestinian boy in Gaza Strip;Palestinian boy, 7, shot \"playing near Israeli tank\".", "source_original": "Palestinian medical sources", "where_prec": 2, "where_coordinates": "Erez crossing", "where_description": "Gaza Strip village near the Erez crossing", "adm_1": "Gaza Strip", "adm_2": "", "latitude": 31.5582, "longitude": 34.544839, "geom_wkt": "POINT (34.544839 31.558200)", "priogrid_gid": 175390, "country": "Israel", "country_id": 666, "region": "Middle East", "event_clarity": 1, "date_prec": 1, "date_start": "2002-03-01T00:00:00", "date_end": "2002-03-01T00:00:00", "deaths_a": 0, "deaths_b": 0, "deaths_civilians": 1, "deaths_unknown": 0, "best": 1, "high": 1, "low": 1}

# data_1 = data[1]
# print(data_1)



with open('Israel_2002.csv', 'w', encoding='utf8') as file:
    file.write('Country,Fatalities,Year,\n')    
    for incidence in data:
        file.write(f'{incidence["country"]},{incidence["best"]},{incidence["year"]} \n')

