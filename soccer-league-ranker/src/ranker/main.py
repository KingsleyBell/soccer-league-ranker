import argparse


def calculate_ranking_table(match_results):
    """Calculate soccer ranking table given match results"""
    return match_results


def run():
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

    ranking_table = calculate_ranking_table(match_results)

    # Check output
    if args.ofile:
        open(args.ofile, 'w').write(ranking_table)
    else:
        print(ranking_table)

    print("Ranking table successfully calculated!")
