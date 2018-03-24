import csv
import json

#provides mapping reference of state abbreviations to full state names
states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AS': 'American Samoa',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'FM': 'Marshall Islands',
    'GA': 'Georgia',
    'GU': 'Guam',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MH': 'Marshall Islands',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MP': 'Northern Mariana Islands',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'PR': 'Puerto Rico',
    'PW': 'Palau',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VI': 'Virgin Islands',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}

#initializes a dictionary by full state name
# states_dictionary = {
#     'Alaska': 0,
#     'Alabama': 0,
#     'Arkansas': 0,
#     'American Samoa': 0,
#     'Arizona': 0,
#     'California': 0,
#     'Colorado': 0,
#     'Connecticut': 0,
#     'District of Columbia': 0,
#     'Delaware': 0,
#     'Florida': 0,
#     'Marshall Islands': 0,
#     'Georgia': 0,
#     'Guam': 0,
#     'Hawaii': 0,
#     'Iowa': 0,
#     'Idaho': 0,
#     'Illinois': 0,
#     'Indiana': 0,
#     'Kansas': 0,
#     'Kentucky': 0,
#     'Louisiana': 0,
#     'Massachusetts': 0,
#     'Maryland': 0,
#     'Maine': 0,
#     'Marshall Islands': 0,
#     'Michigan': 0,
#     'Minnesota': 0,
#     'Missouri': 0,
#     'Northern Mariana Islands': 0,
#     'Mississippi': 0,
#     'Montana': 0,
#     'North Carolina': 0,
#     'North Dakota': 0,
#     'Nebraska': 0,
#     'New Hampshire': 0,
#     'New Jersey': 0,
#     'New Mexico': 0,
#     'Nevada': 0,
#     'New York': 0,
#     'Ohio': 0,
#     'Oklahoma': 0,
#     'Oregon': 0,
#     'Pennsylvania': 0,
#     'Puerto Rico': 0,
#     'Palau': 0,
#     'Rhode Island': 0,
#     'South Carolina': 0,
#     'South Dakota': 0,
#     'Tennessee': 0,
#     'Texas': 0,
#     'Utah': 0,
#     'Virginia': 0,
#     'Virgin Islands': 0,
#     'Vermont': 0,
#     'Washington': 0,
#     'Wisconsin': 0,
#     'West Virginia': 0,
#     'Wyoming': 0
#     }


def parses_csv(begin=None, end=None, incident_filter=None):
    """parses fema data and returns dictionary of states with number of incidents"""
    states_dictionary = {}
    begin = int(begin)
    end = int(end)
    with open('DisasterDeclarationsSummaries.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            state_abbr = line['state']
            state = states[state_abbr]
            year = int(line['fyDeclared'])
            incident_type = line['incidentType']
            if (begin <= year <= end) and (incident_filter == incident_type):
                states_dictionary.setdefault(state, 0)
                states_dictionary[state] += 1
    print(states_dictionary)
    return states_dictionary


