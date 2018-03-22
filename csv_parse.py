import csv


def parses_csv(date_range=None, type=None):
    """parses fema data and returns dictionary of states with number of incidents"""

    states_dictionary = {}
    with open('DisasterDeclarationsSummaries.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            state = line['state']
            states_dictionary.setdefault(state,0)
            states_dictionary[state] += 1
    

    print(states_dictionary)



