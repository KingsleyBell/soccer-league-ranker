import pytest

from ranker.main import get_points, get_team_name_and_score


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
