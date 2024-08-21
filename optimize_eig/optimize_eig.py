"""Module Docstring."""

import cmath as c
import logging

import numpy as np

# TODO(Konstantin Ladutenko): Check how to write todos!
# https://docs.astral.sh/ruff/rules/missing-todo-link/

logger = logging.getLogger("optimize_eig")
logger.info("This is a {word}", extra={"word": "Log"})


def kappa(wavenumber: float, dist: float) -> complex:
    return 1 / dist * c.exp(1j * wavenumber * dist)


def uniform_random_symmetric_matrix(
    n: int, vals: np.ndarray[np.float64]
) -> np.ndarray[np.float64]:
    p = np.ones((n, n))
    p[np.triu_indices(n, 1)] = vals
    p[np.tril_indices(n, -1)] = p.T[np.tril_indices(n, -1)]
    return p


def build_matrix(
    size: int,
    omega: float,
    gamma: float,
    wavenumber: float,
    vals: np.ndarray[np.float64],
) -> np.ndarray[np.complex128]:
    dists = uniform_random_symmetric_matrix(size, vals)
    arr = np.empty(dists.shape, dtype=np.complex128)
    for i in range(dists.shape[0]):
        for j in range(dists.shape[1]):
            arr[i, j] = kappa(wavenumber, dists[i, j])
    for i in range(dists.shape[0]):
        arr[i, i] = omega - 1j * gamma
    return arr


# class Calculator:
#     """Class for simple calculator operations."""

#     @staticmethod
#     def divide(a: float, b: float) -> float:
#         """Divide a by b.

#         Args:
#             a (float): Dividend.
#             b (float): Divisor.

#         Returns:
#             float: The result of the division.

#         Raises:
#             ZeroDivisionError: if b is 0.
#             TypeError: if a or b are not float numbers.

#         Examples:
#             You can run this function as following.

#             >>> Calculator.divide(2,1)
#             2.0

#         """
#         if b == 0:
#             raise ZeroDivisionError
#         elif type(a) not in (float, int) or type(b) not in (float, int):
#             raise TypeError
#         return a / b


if __name__ == "__main__":
    logger.warning("RUNNING!")
