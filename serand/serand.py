import os
import secrets
import math
import bisect
import itertools
from typing import Any, List, Sequence, Union


class SecureRandom:
    def __init__(self):
        self._state = None

    def seed(self, a: Union[None, int, float, str, bytes, bytearray] = None, version: int = 2):
        if a is None:
            a = os.urandom(16)
        elif isinstance(a, (str, bytes, bytearray)):
            if version == 2:
                a = int.from_bytes(a.encode() if isinstance(a, str) else a, 'big')
            else:
                raise ValueError("Version 1 not supported for strings")
        elif not isinstance(a, int):
            raise TypeError("Seed must be None, int, float, str, bytes, or bytearray")
        self._state = secrets.SystemRandom(a).randrange(2**32)

    def getstate(self):
        return self._state

    def setstate(self, state: Any):
        self._state = state

    @staticmethod
    def randbytes(n: int) -> bytes:
        return os.urandom(n)

    @staticmethod
    def randrange(start: int, stop: Union[int, None] = None, step: int = 1) -> int:
        if stop is None:
            start, stop = 0, start
        return secrets.randbelow((stop - start + step - 1) // step) * step + start

    @staticmethod
    def randint(a: int, b: int) -> int:
        return SecureRandom.randrange(a, b + 1)

    @staticmethod
    def getrandbits(k: int) -> int:
        return secrets.randbits(k)

    @staticmethod
    def choice(seq: Sequence) -> Any:
        if not seq:
            raise IndexError("Cannot choose from an empty sequence")
        return seq[secrets.randbelow(len(seq))]

    @staticmethod
    def choices(population: Sequence, weights: Union[Sequence[float], None] = None, cum_weights: Union[Sequence[float], None] = None, k: int = 1) -> List:
        if weights is not None and cum_weights is not None:
            raise TypeError("Cannot specify both weights and cum_weights")
        if weights is None and cum_weights is None:
            return [SecureRandom.choice(population) for _ in range(k)]
        if cum_weights is None:
            cum_weights = list(itertools.accumulate(weights))
        total = cum_weights[-1]
        return [population[bisect.bisect(cum_weights, secrets.randbelow(total))] for _ in range(k)]

    @staticmethod
    def shuffle(x: List):
        n = len(x)
        for i in range(n - 1, 0, -1):
            j = secrets.randbelow(i + 1)
            x[i], x[j] = x[j], x[i]

    @staticmethod
    def sample(population: Sequence, k: int, counts: Union[Sequence[int], None] = None) -> List:
        if counts is not None:
            population = [item for item, count in zip(population, counts) for _ in range(count)]
        if k > len(population):
            raise ValueError("Sample larger than population")
        return secrets.SystemRandom().sample(population, k)

    @staticmethod
    def binomialvariate(n: int = 1, p: float = 0.5) -> int:
        return sum(1 for _ in range(n) if secrets.randbelow(10000) < p * 10000)

    @staticmethod
    def random() -> float:
        return secrets.randbits(53) / (1 << 53)

    @staticmethod
    def uniform(a: float, b: float) -> float:
        return a + (b - a) * SecureRandom.random()

    @staticmethod
    def triangular(low: float, high: float, mode: float) -> float:
        u = SecureRandom.random()
        c = (mode - low) / (high - low)
        if u <= c:
            return low + math.sqrt(u * (high - low) * (mode - low))
        else:
            return high - math.sqrt((1 - u) * (high - low) * (high - mode))

    @staticmethod
    def betavariate(alpha: float, beta: float) -> float:
        y1 = SecureRandom.gammavariate(alpha, 1)
        y2 = SecureRandom.gammavariate(beta, 1)
        return y1 / (y1 + y2)

    @staticmethod
    def expovariate(lambd: float) -> float:
        return -math.log(1.0 - SecureRandom.random()) / lambd

    @staticmethod
    def gammavariate(alpha: float, beta: float) -> float:
        if alpha <= 0.0 or beta <= 0.0:
            raise ValueError('gammavariate: alpha and beta must be > 0.0')
        if alpha > 1.0:
            # Uses R.C.H. Cheng, "The generation of Gamma variables with non-integral shape parameters",
            # Applied Statistics, (1977), 26, No. 1, p71-74
            ainv = math.sqrt(2.0 * alpha - 1.0)
            bbb = alpha - math.log(4.0)
            ccc = alpha + ainv

            while True:
                u1 = SecureRandom.random()
                if not (1e-7 < u1 < 0.9999999):
                    continue
                u2 = 1.0 - SecureRandom.random()
                v = math.log(u1 / (1.0 - u1)) / ainv
                x = alpha * math.exp(v)
                z = u1 * u1 * u2
                r = bbb + ccc * v - x
                if r + (1.0 + math.log(4.5)) - 4.5 * z >= 0.0 or r >= math.log(z):
                    return x * beta
        elif alpha == 1.0:
            return -math.log(1.0 - SecureRandom.random()) * beta
        else:
            while True:
                u = SecureRandom.random()
                b = (math.e + alpha) / math.e
                p = b * u
                if p <= 1.0:
                    x = p ** (1.0 / alpha)
                else:
                    x = -math.log((b - p) / alpha)
                u1 = SecureRandom.random()
                if p > 1.0:
                    if u1 <= x ** (alpha - 1.0):
                        break
                elif u1 <= math.exp(-x):
                    break
            return x * beta

    @staticmethod
    def gauss(mu: float = 0.0, sigma: float = 1.0) -> float:
        while True:
            x2pi = SecureRandom.random() * 2.0 * math.pi
            g2rad = math.sqrt(-2.0 * math.log(1.0 - SecureRandom.random()))
            z = math.cos(x2pi) * g2rad
            return mu + z * sigma

    @staticmethod
    def lognormvariate(mu: float, sigma: float) -> float:
        return math.exp(SecureRandom.gauss(mu, sigma))

    @staticmethod
    def normalvariate(mu: float = 0.0, sigma: float = 1.0) -> float:
        return SecureRandom.gauss(mu, sigma)

    @staticmethod
    def vonmisesvariate(mu: float, kappa: float) -> float:
        if kappa <= 1e-6:
            return 2.0 * math.pi * SecureRandom.random()
        a = 1.0 + math.sqrt(1.0 + 4.0 * kappa ** 2)
        b = (a - math.sqrt(2.0 * a)) / (2.0 * kappa)
        r = (1.0 + b ** 2) / (2.0 * b)

        while True:
            u1 = SecureRandom.random()
            z = math.cos(math.pi * u1)
            f = (1.0 + r * z) / (r + z)
            c = kappa * (r - f)
            u2 = SecureRandom.random()
            if u2 < c * (2.0 - c) or u2 <= c * math.exp(1.0 - c):
                break

        u3 = SecureRandom.random()
        if mu < math.pi:
            return mu + math.acos(f) * (1 if u3 < 0.5 else -1)
        else:
            return mu - math.acos(f) * (1 if u3 < 0.5 else -1)

    @staticmethod
    def paretovariate(alpha: float) -> float:
        return 1.0 / (1.0 - SecureRandom.random()) ** (1.0 / alpha)

    @staticmethod
    def weibullvariate(alpha: float, beta: float) -> float:
        return alpha * (-math.log(1.0 - SecureRandom.random())) ** (1.0 / beta)
