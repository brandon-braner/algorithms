from problems.two_crystal_balls.crystal_balls import crystal_balls

class TestCrystalBalls:
    def test_crystal_balls_breaks(self):
        assert crystal_balls(
            [False, False, False, False, False, False, False, False, True, True, True, True, True, True, True]) == 8

        assert crystal_balls(
            [False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False,
             True, True, True, True, True, True, True, True, True]) == 56

        assert crystal_balls(
            [False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False,
             True, True, True, True, True, True, True, True, True,
             True, True, True, True, True, True, True, True,
             True, True, True, True, True, True, True, True,]) == 72

    def test_crystal_balls_does_not_break(self):
        assert crystal_balls(
            [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]) == -1

        assert crystal_balls(
            [False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False,]) == -1

