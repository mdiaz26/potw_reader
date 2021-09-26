import csv

position_to_index = {
    'QB': 0,
    'RB': 1,
    'WR': 2,
    'TE': 3,
    'K': 4,
    'DST': 5
}

position_replacement_numbers = {
    'QB': 21,
    'RB': 21,
    'WR': 31,
    'TE': 11,
    'K': 11,
    'DST': 11
}

division_teams = {
    'mario': ['HAR', 'VA', 'CR', 'LIC', 'YON'],
    'luigi': ['FLU', 'OAK', 'MARS', 'NE', 'GK']
}

# def get_position(csv_input):
#     result = ([], [], [], [], [], [])
#     next(csv_input)
#     for line in csv_input:
#         line_position = line[3]
#         tuple_index = position_to_index[line_position]
#         if len(result[tuple_index]) <= position_replacement_numbers[line_position]:
#             result[tuple_index].append([line[1], line[5], line[10]])
#     return result

def get_position(csv_input):
    result = ([], [], [], [], [], [])
    next(csv_input)
    for line in csv_input:
        line_position = line[3]
        position_array = [line_position] if ',' not in line_position else line_position.split(',')
        for position in position_array:
            tuple_index = position_to_index[position]
            if len(result[tuple_index]) <= position_replacement_numbers[position]:
                result[tuple_index].append([line[1], line[5], line[10]])
    return result

def get_top_players(positional_tuple):
    mario_division = ['', '', '', 0]
    luigi_division = ['', '', '', 0]
    for position in positional_tuple:
        top_mario = top_player_by_division(position, 'mario')
        top_luigi = top_player_by_division(position, 'luigi')
        if top_mario[3] > mario_division[3]:
            mario_division = top_mario
        if top_luigi[3] > luigi_division[3]:
            luigi_division = top_luigi
    return (mario_division, luigi_division)

def top_player_by_division(list_of_players, division_name):
    last_players_score = list_of_players[-1][2]
    for row in list_of_players:
        if row[1] in division_teams[division_name]:
            return [row[0], row[1], row[2], float(row[2]) - float(last_players_score)]

with open('scores.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    positional_tuple = get_position(csv_reader)

    (top_mario_player, top_luigi_player) = get_top_players(positional_tuple)

    print(f'Mario Division potw: {top_mario_player[0]}')
    print(f'Luigi Division potw: {top_luigi_player[0]}')