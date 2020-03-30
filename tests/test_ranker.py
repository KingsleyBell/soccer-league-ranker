import pytest

from ranker.main import calculate_scores, get_points, get_ranking_table, get_team_name_and_score


class TestRanker:
    @pytest.mark.parametrize(
        'team_name_and_score, expected_name, expected_score',
        [
            ('Team Name 3', 'Team Name', 3),
            ('Snakes 0', 'Snakes', 0),
        ]
    )
    def test_get_team_name_and_score(self, team_name_and_score, expected_name, expected_score):
        name, score = get_team_name_and_score(team_name_and_score)

        assert name == expected_name
        assert score == expected_score

    @pytest.mark.parametrize(
        'team1_score, team2_score, expected_team1_points, expected_team2_points',
        [
            (0, 0, 1, 1),
            (0, 1, 0, 3),
            (1, 0, 3, 0),
            (5, 4, 3, 0),
        ]
    )
    def test_get_points(self, team1_score, team2_score, expected_team1_points, expected_team2_points):
        team1_points, team2_points = get_points(team1_score, team2_score)

        assert team1_points == expected_team1_points
        assert team2_points == expected_team2_points

    @pytest.mark.parametrize(
        'match_scores_string, expected_scores',
        [
            ('Team1 1, Team2 0', {"Team1": 3, "Team2": 0}),
            ('Team1 1, Team2 1\nTeam1 5, Team3 3', {"Team1": 4, "Team2": 1, "Team3": 0}),
            ('T1 1, T2 0\nT1 5, T3 3\nT2 4, T3 4', {"T1": 6, "T2": 1, "T3": 1}),
        ]
    )
    def test_calculate_scores(self, match_scores_string, expected_scores):
        scores = calculate_scores(match_scores_string)

        assert scores == expected_scores

    @pytest.mark.parametrize(
        'scores, expected_ranking_table',
        [
            ({'T1': 0, 'T2': 3}, '1. T2, 3 pts\n2. T1, 0 pts'),
            (
                    {'T1': 0, 'T2': 3, 'T4': 1, 'T3': 1},
                    '1. T2, 3 pts\n2. T3, 1 pt\n2. T4, 1 pt\n4. T1, 0 pts'
            ),
        ]
    )
    def test_get_ranking_table(self, scores, expected_ranking_table):
        ranking_table = get_ranking_table(scores)

        assert ranking_table == expected_ranking_table
