def display_as_percentage(val):  #function to return a number (val) as a percentage 
  return '{:.1f}%'.format(val * 100)


def calculate_simple_return(start_price, end_price, dividend=0):  # calculate the simple rate of return with the dividend given a default value of 0
  return (end_price-start_price+dividend)/start_price

simple_return = calculate_simple_return(200, 250, 20)

print("The simple rate of return is " + display_as_percentage(simple_return))   #print to terminal
