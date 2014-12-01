# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import
import numpy as np
from numpy import (abs, arctan2, asarray, cos, exp, floor, log, log10,
                   arange, pi, prod, roll, sign, sin, sqrt, sum, where,
                   zeros, tan, tanh, dot)

from scipy.misc import factorial
from .go_benchmark import Benchmark


class Ackley01(Benchmark):
    """
    Ackley01 objective function.

    The Ackley01 [1]_ global optimization problem is a multimodal minimization
    problem defined as follows:

    .. math::

        f_{{Ackley01}}({x}) = -20e^{-0.2\sqrt{\frac{1}{n} \sum_{i=1}^n
         x_i^2}} - e^{ \frac{1}{n} \sum_{i=1}^n \cos(2 \pi x_i)} + 20 + e

    Here, :math:`n` represents the number of dimensions and :math:`x_i \in [-35,
    35]` for :math:`i=1,...,n`.

    *Global optimum*: :math:`f(x_i) = 0` for :math:`x_i = 0` for
    :math:`i=1,...,n`

    .. [1] Momin Jamil and Xin-She Yang, A literature survey of benchmark
     functions for global optimization problems, Int. Journal of Mathematical
     Modelling and Numerical Optimisation, Vol. 4, No. 2, pp. 150--194 (2013)

    """

    def __init__(self, dimensions=2):
        Benchmark.__init__(self, dimensions)

        self._bounds = zip([-35.0] * self.N, [35.0] * self.N)
        self.global_optimum = [[0 for _ in range(self.N)]]
        self.fglob = 0.0
        self.change_dimensionality = True

    def fun(self, x, *args):
        self.nfev += 1
        u = sum(x ** 2)
        v = sum(cos(2 * pi * x))
        return (-20. * exp(-0.2 * sqrt(u / self.N))
                - exp(v / self.N) + 20. + exp(1.))


class Ackley02(Benchmark):
    """
    Ackley02 objective function.

    The Ackley02 [1]_ global optimization problem is a multimodal minimization
    problem defined as follows:

    .. math::

        f_{Ackley02}(\mathbf{x}) = -200e^{-0.02\sqrt{x_1^2 + x_2^2}}

    Here, :math:`n` represents the number of dimensions and :math:`x_i \in [-32,
     32]` for :math:`i=1,2`.

    *Global optimum*: :math:`f(x_i) = -200` for :math:`\mathbf{x} = [0, 0]`

    .. [1] Momin Jamil and Xin-She Yang, A literature survey of benchmark
     functions for global optimization problems, Int. Journal of Mathematical
     Modelling and Numerical Optimisation, Vol. 4, No. 2, pp. 150--194 (2013)

    """
    def __init__(self, dimensions=2):
        Benchmark.__init__(self, dimensions)

        self._bounds = zip([-32.0] * self.N, [32.0] * self.N)
        self.global_optimum = [[0 for _ in range(self.N)]]
        self.fglob = -200.

    def fun(self, x, *args):
        self.nfev += 1
        return -200 * exp(-0.02 * sqrt(x[0] ** 2 + x[1] ** 2))


class Ackley03(Benchmark):
    """
    Ackley03 [1]_ objective function.

    The Ackley03 global optimization problem is a multimodal minimization
    problem defined as follows:

    .. math::

        f_{Ackley03}(\mathbf{x}) = -200e^{-0.02\sqrt{x_1^2 + x_2^2}} +
            5e^{\cos(3x_1) + \sin(3x_2)}

    Here, :math:`n` represents the number of dimensions and :math:`x_i \in [-32,
    32]` for :math:`i=1,2`.

    *Global optimum*: :math:`f(x_i) = -195.62902825923879` for :math:`\mathbf{x}
    =[-0.68255758, -0.36070859]`

    .. [1] Momin Jamil and Xin-She Yang, A literature survey of benchmark
     functions for global optimization problems, Int. Journal of Mathematical
     Modelling and Numerical Optimisation, Vol. 4, No. 2, pp. 150--194 (2013)

    """

    def __init__(self, dimensions=2):
        Benchmark.__init__(self, dimensions)

        self._bounds = zip([-32.0] * self.N, [32.0] * self.N)
        self.global_optimum = [[-0.68255758, -0.36070859]]
        self.fglob = -195.62902825923879

    def fun(self, x, *args):
        self.nfev += 1
        a = -200 * exp(-0.02 * sqrt(x[0] ** 2 + x[1] ** 2))
        a += 5 * exp(cos(3 * x[0]) + sin(3 * x[1]))
        return a


class Adjiman(Benchmark):

    """
    Adjiman objective function.

    The Adjiman [1]_ global optimization problem is a multimodal minimization
    problem defined as follows:

    .. math::

        f_{{Adjiman}}(\mathbf{x}) = \cos(x_1)\sin(x_2) - \frac{x_1}{(x_2^2 +
        1)}

    Here, :math:`x_1 \in [-1, 2]` and :math:`x_2 \in [-1, 1]`.

    *Global optimum*: :math:`f(x_i) = -2.02181` for :math:`\mathbf{x} = [2.0,
    0.10578]`

    .. [1] Momin Jamil and Xin-She Yang, A literature survey of benchmark
     functions for global optimization problems, Int. Journal of Mathematical
     Modelling and Numerical Optimisation, Vol. 4, No. 2, pp. 150--194 (2013)

    """

    def __init__(self, dimensions=2):
        Benchmark.__init__(self, dimensions)

        self._bounds = ([-1.0, 2.0], [-1.0, 1.0])
        self.global_optimum = [[2.0, 0.10578]]
        self.fglob = -2.02180678

    def fun(self, x, *args):
        self.nfev += 1
        return cos(x[0]) * sin(x[1]) - x[0] / (x[1] ** 2 + 1)


class Alpine01(Benchmark):

    """
    Alpine01 objective function.

    The Alpine01 [1]_ global optimization problem is a multimodal minimization
    problem defined as follows:

    .. math::

        f_{Alpine01}(\mathbf{x}) = \sum_{i=1}^{n} \lvert {x_i \sin \left( x_i
        \right) + 0.1 x_i} \rvert

    Here, :math:`n` represents the number of dimensions and :math:`x_i \in [-10,
    10]` for :math:`i=1,...,n`.

    *Global optimum*: :math:`f(x_i) = 0` for :math:`x_i = 0` for :math:`i=1,...,
    n`

    .. [1] Momin Jamil and Xin-She Yang, A literature survey of benchmark
     functions for global optimization problems, Int. Journal of Mathematical
     Modelling and Numerical Optimisation, Vol. 4, No. 2, pp. 150--194 (2013)

    """

    def __init__(self, dimensions=2):
        Benchmark.__init__(self, dimensions)

        self._bounds = zip([-10.0] * self.N, [10.0] * self.N)
        self.global_optimum = [[0 for _ in range(self.N)]]
        self.fglob = 0.0
        self.change_dimensionality = True

    def fun(self, x, *args):
        self.nfev += 1

        return sum(abs(x * sin(x) + 0.1 * x))


class Alpine02(Benchmark):

    """
    Alpine02 objective function.

    The Alpine02 [1]_ global optimization problem is a multimodal minimization
    problem defined as follows:

    .. math::

        f_{Alpine02}(\mathbf{x}) = \prod_{i=1}^{n} \sqrt{x_i} \sin(x_i)

    Here, :math:`n` represents the number of dimensions and :math:`x_i \in [0,
    10]` for :math:`i=1,...,n`.

    *Global optimum*: :math:`f(x_i) = -6.1295` for :math:`\mathbf{x}=
    [7.91705268, 4.81584232]` for :math:`i=1,2`

    .. [1] Momin Jamil and Xin-She Yang, A literature survey of benchmark
     functions for global optimization problems, Int. Journal of Mathematical
     Modelling and Numerical Optimisation, Vol. 4, No. 2, pp. 150--194 (2013)

    """

    def __init__(self, dimensions=2):
        Benchmark.__init__(self, dimensions)

        self._bounds = zip([0.0] * self.N, [10.0] * self.N)
        # TODO check minima as a function of dimensionality
        self.global_optimum = [[7.91705268, 4.81584232]]
        self.fglob = -6.12950
        self.change_dimensionality = True

    def fun(self, x, *args):
        self.nfev += 1

        return prod(sqrt(x) * sin(x))


class AMGM(Benchmark):

    """
    AMGM objective function.

    The AMGM (Arithmetic Mean - Geometric Mean Equality) global optimization
    problem is a multimodal minimization problem defined as follows

    .. math::

        f_{{AMGM}}(\mathbf{x}) = \left ( \frac{1}{n} \sum_{i=1}^{n} x_i -
         \sqrt[n]{ \prod_{i=1}^{n} x_i} \right )^2

    Here, :math:`n` represents the number of dimensions and :math:`x_i \in [0,
    10]` for :math:`i=1,...,n`.

    *Global optimum*: :math:`f(x_i) = 0` for :math:`x_1 = x_2 = ... = x_n` for
    :math:`i=1,...,n`

    """

    def __init__(self, dimensions=2):
        Benchmark.__init__(self, dimensions)

        self._bounds = zip([0.0] * self.N, [10.0] * self.N)
        self.global_optimum = [[1, 1]]
        self.fglob = 0.0
        self.change_dimensionality = True

    def fun(self, x, *args):
        self.nfev += 1

        f1 = sum(x)
        f2 = prod(x)
        f1 = f1 / self.N
        f2 = f2 ** (1.0 / self.N)
        f = (f1 - f2) ** 2

        return f
