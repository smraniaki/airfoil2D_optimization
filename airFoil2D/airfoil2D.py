import numpy as np
import os
import linecache

from pymoo.algorithms.so_pattern_search import PatternSearch
from pymoo.algorithms.nsga2 import NSGA2
from pymoo.visualization.scatter import Scatter
from pymoo.model.problem import Problem
from pymoo.optimize import minimize
from subprocess import call


##
class MyProblem(Problem):

    def __init__(self):
        super().__init__(n_var=2,
                         n_obj=2,
                         n_constr=2,
                         xl=np.array([-2,-2]),
                         xu=np.array([2,2]))

    def _evaluate(self, X, out, *args, **kwargs):
        call(['bash', './Allrun'])
        f1 = float(linecache.getline("PARM/parm/p1", 1))
        f2 = float(linecache.getline("PARM/parm/p2", 1))
        #f = int(linecache.getline("PARM/parm/u", 1))
        X[:, 0] = float(linecache.getline("PARM/parm/u", 1))
        X[:, 1] = float(linecache.getline("PARM/parm/v", 1))

        g1 = 2*(X[:, 0]-0.1) * (X[:, 0]-0.9) / 0.18
        g2 = - 20*(X[:, 0]-0.4) * (X[:, 0]-0.6) / 4.8

        out["F"] = np.column_stack([f1, f2])
        out["G"] = np.column_stack([g1, g2])


#vectorized_problem = MyProblem()
##



problem = MyProblem()

algorithm = NSGA2(pop_size=100)
#algorithm = PatternSearch()

res = minimize(problem,
               algorithm,
               ('n_gen', 200),
               seed=1,
               verbose=False)

plot = Scatter()
plot.add(problem.pareto_front(), plot_type="line", color="black", alpha=0.7)
plot.add(res.F, color="red")
plot.show()

