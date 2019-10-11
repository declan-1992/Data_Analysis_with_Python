def population_growth(year_one, year_two, population_one, population_two):  ## define a function that take the population in a city during a given year and returns the growth rate and annaul growth rate
  
  growth_rate = ((population_two - population_one)/population_two) * 100  ## calculate the growth rate
  
  annual_growth_rate = growth_rate / (year_two - year_one)    ##  calculate annual growth rate
  
  return annual_growth_rate

print(population_growth(1927, 2017, 691000, 15029231))     ## print result
