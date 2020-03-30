import argparse


def get_team_name_and_score(team_name_score):
    """Parse team name and score from match score string"""
    team_split = team_name_score.split(' ')
    team_score = int(team_split[-1])
    team_name = ' '.join(team_split[:-1]).strip()

    return team_name, team_score


def get_points(team1_score, team2_score):
    """Get team points from on match score"""
    if team1_score > team2_score:
        return 3, 0
    elif team2_score > team1_score:
        return 0, 3

    return 1, 1


def calculate_scores(match_results):
    """Calculate soccer team scores from match results"""
    results_list = list(filter(None, match_results.split('\n')))
    scores = {}

    for result in results_list:
        team1, team2 = result.split(',')

        team1_name, team1_score = get_team_name_and_score(team1)
        team2_name, team2_score = get_team_name_and_score(team2)

        team1_points, team2_points = get_points(team1_score, team2_score)

        # Add points to scores dict
        scores[team1_name] = scores.get(team1_name, 0) + team1_points
        scores[team2_name] = scores.get(team2_name, 0) + team2_points

    return scores


def get_ranking_table(scores):
    """Calculate soccer ranking table from team scores"""
    output_str_list = []
    sorted_scores = sorted(scores.items(), key=lambda x: (-x[1], x[0].lower()))

    previous_score = -1
    current_place = 0
    place_plus = 0
    for score in sorted_scores:
        team_name = score[0]
        team_score = score[1]
        pts_plural = 's' if team_score != 1 else ''

        if team_score == previous_score:
            place_plus += 1
        else:
            current_place += place_plus + 1
            place_plus = 0

        previous_score = team_score
        output_str_list.append(f'{current_place}. {team_name}, {team_score} pt{pts_plural}')

    return '\n'.join(output_str_list)


def run():
    """Main CLI tool method"""
    parser = argparse.ArgumentParser(epilog=(
        'Soccer League Ranker. A handy ranking table calculator.'
    ))

    parser.add_argument('stdin', help='Std input of games results', nargs='?', default=None)
    parser.add_argument('-ifile', help='Path to input file')
    parser.add_argument('-ofile', help='Path to output file')

    args = parser.parse_args()

    # Check input
    if args.stdin:
        match_results = args.stdin
    elif args.ifile:
        match_results = open(args.ifile, 'r').read()

    scores = calculate_scores(match_results)
    ranking_table = get_ranking_table(scores)

    # Check output
    if args.ofile:
        open(args.ofile, 'w').write(ranking_table)
    else:
        print(ranking_table)

    print('Ranking table successfully calculated!')
