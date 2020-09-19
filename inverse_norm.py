#Import
from scipy import stats, optimize

#Functions
def IND(y, mean, std): #Inverse Normal Distribution
    norm = stats.norm(mean, std)
    return optimize.fsolve(lambda x:norm.pdf(x)-y, norm.mean()-norm.std())


def ISND(y): #Inverse Standard Normal Distribution
    norm = stats.norm(loc=0, scale=1)
    return optimize.fsolve(lambda x:norm.pdf(x)-y, norm.mean()+norm.std())


mean, std = 180, 2000
norm_test = stats.norm(mean, std).pdf(6)
print('Normal Test: ', norm_test)

standard_norm_test = stats.norm(0, 1).pdf(1.22)
print('Standard Normal Test: ', standard_norm_test)

print(IND(norm_test, mean, std))
print(ISND(standard_norm_test))