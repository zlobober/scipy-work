# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import
import numpy as np
from numpy import (abs, arctan2, asarray, cos, exp, floor, log, log10,
                   arange, pi, prod, roll, sign, sin, sqrt, sum, where,
                   zeros, tan, tanh, dot)

from scipy.misc import factorial
from .go_benchmark import Benchmark


class Langermann(Benchmark):

    """
    Langermann objective function.

    This class defines the Langermann global optimization problem. This
    is a multimodal minimization problem defined as follows:

    .. math::

        f_{\\text{Langermann}}(\\mathbf{x}) = - \\sum_{i=1}^{5} \\frac{c_i \\cos\\left\{\\pi \\left[\\left(x_{1}- a_i\\right)^{2} + \\left(x_{2} - b_i \\right)^{2}\\right]\\right\}}{e^{\\frac{\\left( x_{1} - a_i\\right)^{2} + \\left( x_{2} - b_i\\right)^{2}}{\\pi}}}

    Here, :math:`n` represents the number of dimensions and :math:`x_i \\in [0, 10]` for :math:`i=1,2`.

    *Global optimum*: :math:`f(x_i) = -5.1621259` for :math:`\\mathbf{x} = [2.00299219, 1.006096]`

    """

    def __init__(self, dimensions=2):
        Benchmark.__init__(self, dimensions)

        self._bounds = zip([0.0] * self.N, [10.0] * self.N)

        self.global_optimum = [[2.00299219, 1.006096]]
        self.fglob = -5.1621259

    def fun(self, x, *args):
        self.nfev += 1

        a = [3, 5, 2, 1, 7]
        b = [5, 2, 1, 4, 9]
        c = [1, 2, 5, 2, 3]

        return (-sum(c * exp(-(1 / pi) * ((x[0] - a) ** 2 +
                    (x[1] - b) ** 2)) * cos(pi * ((x[0] - a) ** 2
                                            + (x[1] - b) ** 2))))


class LennardJones(Benchmark):

    """
    LennardJones objective function.

    This class defines the Lennard-Jones global optimization problem. This
    is a multimodal minimization problem defined as follows:

    .. math::

        f_{\\text{LennardJones}}(\\mathbf{x}) = \\sum_{i=0}^{n-2}\\sum_{j>1}^{n-1}\\frac{1}{r_{ij}^{12}} - \\frac{1}{r_{ij}^{6}}


    Where, in this exercise:

    .. math::

        r_{ij} = \\sqrt{(x_{3i}-x_{3j})^2 + (x_{3i+1}-x_{3j+1})^2) + (x_{3i+2}-x_{3j+2})^2}


    Valid for any dimension, :math:`n = 3*k, k=2,3,4,...,20`. :math:`k` is the number of atoms in 3-D space
    constraints: unconstrained type: multi-modal with one global minimum; non-separable

    Value-to-reach: :math:`minima[k-2] + 0.0001`. See array of minima below;
    additional minima available at the Cambridge cluster database:

    http://www-wales.ch.cam.ac.uk/~jon/structures/LJ/tables.150.html

    Here, :math:`n` represents the number of dimensions and :math:`x_i \\in [-4, 4]` for :math:`i=1,...,n`.

    *Global optimum*:

    .. math::

       minima = [-1.,-3.,-6.,-9.103852,-12.712062,-16.505384,-19.821489,-24.113360, \\\\
       -28.422532,-32.765970,-37.967600,-44.326801,-47.845157,-52.322627, \\\\
       -56.815742,-61.317995, -66.530949,-72.659782,-77.1777043]

    """

    def __init__(self, dimensions=6):
        Benchmark.__init__(self, dimensions)

        self._bounds = zip([-4.0] * self.N, [4.0] * self.N)

        self.global_optimum = [[]]

        minima = [
            -1.0, -3.0, -6.0, -9.103852, -12.712062, -
            16.505384, -19.821489, -24.113360, -28.422532,
            -32.765970, -37.967600, -44.326801, -
            47.845157, -52.322627, -56.815742, -61.317995,
            -66.530949, -72.659782, -77.1777043]

        k = int(dimensions / 3)
        self.fglob = minima[k - 2]
        self.change_dimensionality = True

    def fun(self, x, *args):
        self.nfev += 1

        k = int(self.N / 3)
        s = 0.0

        for i in range(k - 1):
            for j in range(i + 1, k):
                a = 3 * i
                b = 3 * j
                xd = x[a] - x[b]
                yd = x[a + 1] - x[b + 1]
                zd = x[a + 2] - x[b + 2]
                ed = xd * xd + yd * yd + zd * zd
                ud = ed * ed * ed
                if ed > 0.0:
                    s += (1.0 / ud - 2.0) / ud

        return s


class Leon(Benchmark):

    """
    Leon objective function.

    This class defines the Leon global optimization problem. This
    is a multimodal minimization problem defined as follows:

    .. math::

        f_{\\text{Leon}}(\\mathbf{x}) = \\left(1 - x_{1}\\right)^{2} + 100 \\left(x_{2} - x_{1}^{2} \\right)^{2}

    Here, :math:`n` represents the number of dimensions and :math:`x_i \\in [-1.2, 1.2]` for :math:`i=1,2`.

    *Global optimum*: :math:`f(x_i) = 0` for :math:`x_i = 1` for :math:`i=1,2`

    """

    def __init__(self, dimensions=2):
        Benchmark.__init__(self, dimensions)

        self._bounds = zip([-1.2] * self.N, [1.2] * self.N)

        self.global_optimum = [[1 for _ in range(self.N)]]
        self.fglob = 0.0

    def fun(self, x, *args):
        self.nfev += 1

        return 100 * (x[1] - x[0] ** 2.0) ** 2.0 + (1 - x[0]) ** 2.0


class Levy03(Benchmark):

    """
    Levy 3 objective function.

    This class defines the Levy 3 global optimization problem. This
    is a multimodal minimization problem defined as follows:

    .. math::

        f_{\\text{Levy03}}(\\mathbf{x}) = \\sin^2(\\pi y_1)+\\sum_{i=1}^{n-1}(y_i-1)^2[1+10\\sin^2(\\pi y_{i+1})]+(y_n-1)^2

    Where, in this exercise:

    .. math::

        y_i=1+\\frac{x_i-1}{4}


    Here, :math:`n` represents the number of dimensions and :math:`x_i \\in [-10, 10]` for :math:`i=1,...,n`.

    *Global optimum*: :math:`f(x_i) = 0` for :math:`x_i = 1` for :math:`i=1,...,n`

    """

    def __init__(self, dimensions=2):
        Benchmark.__init__(self, dimensions)

        self._bounds = zip([-10.0] * self.N, [10.0] * self.N)
        self.custom_bounds = [(-5, 5), (-5, 5)]

        self.global_optimum = [[1 for _ in range(self.N)]]
        self.fglob = 0.0
        self.change_dimensionality = True

    def fun(self, x, *args):
        self.nfev += 1

        y = 1 + (x - 1) / 4
        v = sum((y[: -1] - 1) ** 2 * (1 + 10 * sin(pi * y[1:]) ** 2))
        return sin(pi * y[0]) ** 2 + v + (y[-1] - 1) ** 2


class Levy05(Benchmark):

    """
    Levy 5 objective function.

    This class defines the Levy 5 global optimization problem. This
    is a multimodal minimization problem defined as follows:

    .. math::

        f_{\\text{Levy05}}(\\mathbf{x}) = \\sum_{i=1}^{5} i \\cos \\left[(i-1)x_1 + i \\right] \\times \\sum_{j=1}^{5} j \\cos \\left[(j+1)x_2 + j \\right] + (x_1 + 1.42513)^2 + (x_2 + 0.80032)^2


    Here, :math:`n` represents the number of dimensions and :math:`x_i \\in [-10, 10]` for :math:`i=1,...,n`.

    *Global optimum*: :math:`f(x_i) = -176.1375779` for :math:`\\mathbf{x} = [-1.30685, -1.42485]`.

    """

    def __init__(self, dimensions=2):
        Benchmark.__init__(self, dimensions)

        self._bounds = zip([-10.0] * self.N, [10.0] * self.N)
        self.custom_bounds = ([-2.0, 2.0], [-2.0, 2.0])

        self.global_optimum = [[-1.30685, -1.42485]]
        self.fglob = -176.1375779

    def fun(self, x, *args):
        self.nfev += 1

        i = arange(1, 6)
        a = i * cos((i - 1) * x[0] + i)
        b = i * cos((i + 1) * x[1] + i)

        return sum(a) * sum(b) + (x[0] + 1.42513) ** 2 + (x[1] + 0.80032) ** 2


class Levy13(Benchmark):

    """
    Levy13 objective function.

    This class defines the Levy13 global optimization problem. This
    is a multimodal minimization problem defined as follows:

    .. math::

        f_{\\text{Levy13}}(\\mathbf{x}) = \\left(x_{1} -1\\right)^{2} \\left[\sin^{2}\\left(3 \\pi x_{2}\\right) + 1\\right] + \\left(x_{2} -1\\right)^{2} \\left[\\sin^{2}\\left(2 \\pi x_{2}\\right) + 1\\right] + \\sin^{2}\\left(3 \\pi x_{1}\\right)


    Here, :math:`n` represents the number of dimensions and :math:`x_i \\in [-10, 10]` for :math:`i=1,2`.

    *Global optimum*: :math:`f(x_i) = 0` for :math:`x_i = 1` for :math:`i=1,2`

    """

    def __init__(self, dimensions=2):
        Benchmark.__init__(self, dimensions)

        self._bounds = zip([-10.0] * self.N, [10.0] * self.N)
        self.custom_bounds = [(-5, 5), (-5, 5)]

        self.global_optimum = [[1 for _ in range(self.N)]]
        self.fglob = 0.0

    def fun(self, x, *args):
        self.nfev += 1

        u = sin(3 * pi * x[0]) ** 2
        v = (x[0] - 1) ** 2 * (1 + (sin(3 * pi * x[1])) ** 2)
        w = (x[1] - 1) ** 2 * (1 + (sin(2 * pi * x[1])) ** 2)
        return u + v + w
