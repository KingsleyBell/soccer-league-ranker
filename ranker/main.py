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
    """Calculate soccer team scores given match results"""
    return match_results


def get_ranking_table(scores):
    """Calculate soccer ranking table given team scores"""
    return scores


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
