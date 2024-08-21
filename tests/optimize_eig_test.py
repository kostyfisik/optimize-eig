import numpy as np

from optimize_eig import optimize_eig as m


def test_build() -> None:
    for size in [3, 5]:
        vals = np.random.uniform(0, 1, size * (size - 1) // 2)  # noqa: NPY002
        arr = m.build_matrix(size=size, omega=1, gamma=1, wavenumber=1, vals=vals)
        for i in range(size):
            assert arr[0, i] == arr[i, 0]
            assert arr[i, size - 1] == arr[size - 1, i]
            assert arr[0, 0] == arr[i, i]
    #     np.set_printoptions(precision=3, suppress=True)
    #     print(arr)
    # assert False


# @pytest.mark.parametrize(
#     ("param1", "param2"),
#     [
#         ("a", "b"),
#         ("c", "d"),
#     ],
# )
# class TestGroup:
#     """A class with common parameters, `param1` and `param2`."""

#     @pytest.fixture
#     def fixt(self: Self) -> int:
#         """This fixture will only be available within the scope of TestGroup.

#         Returns:
#             int: A common value to be used by multiple tests

#         """
#         return 123

#     def test_one(self: Self, param1: str, param2: str, fixt: int) -> None:
#         """Run the first test using the fixture.

#         Args:
#             param1 (str): First parameter.
#             param2 (str): Second parameter.
#             fixt (int): Value from fixture.

#         """
#         assert param1 != param2


# @pytest.mark.parametrize(
#     ("a", "b", "expected"),
#     [
#         (1, 1, 1),
#         (42, 1, 42),
#         (84, 2, 42),
#     ],
# )
# def test_divide_ok(a: float, b: float, expected: float) -> None:
#     """Check if divide works for expected entries.

#     Args:
#         a (float): Dividend.
#         b (float): Divisor.
#         expected (float): expected result.

#     """
#     assert m.Calculator.divide(a, b) == expected


# @pytest.mark.parametrize(
#     ("a", "b", "expected"),
#     [
#         (42, "b", TypeError),
#         ("a", 42, TypeError),
#         (42, 0, ZeroDivisionError),
#     ],
# )
# def test_divide_error(
#     a: str | float, b: str | float, expected: float | Exception
# ) -> None:
#     """Check if divide returns correct Exceptions for known entries.

#     Issue raised by https://github.com/kostyfisik/optimize-eig/issues/1337

#     Args:
#         a (float): Dividend.
#         b (float): Divisor.
#         expected (Exception): expected Exception.

#     """
#     with pytest.raises(expected):
#         m.Calculator.divide(a, b)
