"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from thinkbayes import Pmf

pmf = Pmf()
#the probability that you will pick from bowl 1 or 2 
#half as likely for both so .5 and .5
#prior distribution : contains priors for the hypothesis
pmf.Set('Bowl 1', 0.5)
pmf.Set('Bowl 2', 0.5)

#update the distribution based on new data(vanilla cookie)
#multiply each prior by corresponding likelihood
pmf.Mult('Bowl 1', 0.75)
pmf.Mult('Bowl 2', 0.5)

#need to renormalize- hypothesis are mutually exclusive//collectively exhaustive
#does a posterior distribution 
pmf.Normalize()

#now you can get posterior probability!
print pmf.Prob('Bowl 1')
