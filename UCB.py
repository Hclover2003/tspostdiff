from typing import List
from math import sqrt
import numpy as np
from numpy import random


def UCB(pb: int, pa: int, n: int, c: float):
    narm = 2
    arm_a_successes = np.array([0])
    arm_b_successes = np.array([0, 0])
    if np.random.uniform(1) < pa:
        arm_a_successes[0] = 1
    if np.random.uniform(1) < pb:
        arm_b_successes[1] = 1
    arm_a_successes[1] = arm_a_successes[0]
    na = np.array([1, 1])
    nb = np.array([0, 1])

    for i in range(narm+1, n+1):
        ae = arm_a_successes[i-1]/na[i-1]
        be = arm_b_successes[i-1]/nb[i-1]
        if (ae + c * sqrt(i/na[i-1])) > (be + c * sqrt(i/nb[i-1])):
            na[i] = na[i-1] + 1
            nb[i] = nb[i-1]
            arm_a_successes[i] = arm_a_successes[i-1]
            arm_b_successes[i] = arm_b_successes[i-1]
            if np.random.uniform(1) < pa:
                arm_a_successes[i] = arm_a_successes[i-1] + 1
            else:
                nb[i] = nb[i-1] + 1
                na[i] = na[i-1]
                arm_a_successes[i] = arm_a_successes[i-1]
                arm_b_successes[i] = arm_b_successes[i-1]
                if np.random.uniform(1) < pb:
                    arm_b_successes[i] = arm_b_successes[i-1] + 1
    # na: the of times arm A was pulled. nb: vice versa.

    pa_est = arm_b_successes/na
    pb_est = arm_b_successes/nb
    WaldScore = (pa_est - pb_est)/sqrt(pa_est * (1 - pa_est) / na + pb_est *
                                       (1 - pb_est) / nb)
    return [WaldScore, na, nb, arm_a_successes, arm_b_successes]









