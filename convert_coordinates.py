import pandas as pd
import re

d = pd.read_csv('data/Violent_Missing_Coordinates.csv', encoding='cp1252')

def convert_coordinate(value):
    s = str(value).strip()
    nums = re.findall(r'\d+(?:\.\d+)?', s)

    if not nums:
        return float('nan')

    result = float(nums[0])

    if len(nums) >= 3:
        result += float(nums[1]) / 60 + float(nums[2]) / 3600

    if s.endswith(('S', 'W')):
        result = -result

    return result

d['Lat'] = d['Lat'].apply(convert_coordinate)
d['Long'] = d['Long'].apply(convert_coordinate)

d.to_csv('data/Violent_Missing_Coordinates_Converted.csv', index=False)

print('Total records:', len(d))
print('Missing coordinates:', d[['Lat', 'Long']].isna().any(axis=1).sum())
print(d[['V_Incident_ID', 'Lat', 'Long']].head(10))