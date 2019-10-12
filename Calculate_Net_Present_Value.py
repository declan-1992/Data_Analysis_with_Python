import codecademylib3_seaborn
import matplotlib.pyplot as plt

## Cash Flows Here
project_a = [-2000000, 0, 0, 250000, 250000, 500000, 500000, 750000, 750000, 1000000]


## list of discount rates
discount_rate = [0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15]

def calculate_npv(rate, cash_flow):   ##function that takes in values for the rate and cashflow and returns the NPV
    npv = 0
    for t in range(len(cash_flow)):
        npv += cash_flow[t]/(1+rate)**t   ## Calculate NPV
    return npv

npvs_a = list()
for rate in discount_rate:
  npv_a = calculate_npv(rate,project_a)   ## calculate NPV for the given discount rates
  npvs_a.append(npv_a)
  
plt.plot(discount_rate,npvs_a, linewidth = 3.0, color = "green", label = "Project Greenspace")  ##Plot the data
plt.axhline(y=0, linewidth = 0.5, color = "black")
plt.title('NPV Profile: Project Greenspace ')
plt.xlabel('Discount Rate')
plt.ylabel('Net Present Value')
plt.legend()
plt.show()
