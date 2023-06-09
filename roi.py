# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 14:38:41 2023

@author: kyliewise
"""
import math 
from datetime import date, timedelta

class returns:

    # fd_percent
    def fd_percent(shares):
      total_shares = sum(shares)
      percentages = [(share / total_shares) for share in shares]
      return percentages
    
    # calculates the preferred return given money in, PIK, start date, end date (the return value of this should be plugged into interest_back function as interest)
    def preferred_return(money_in, PIK, start_date, end_date):
        # calculates the number of days in between start date and end date
        days = (end_date - start_date).days
        result = money_in * math.pow((1 + PIK), days / 365) - money_in
        return result
    
    # calculates interest_back, if the difference between exit equity and money in is greater than interest then returns interest, otherwise returns the difference (the return value of this should be plugged into the returns function as interest_back)
    def interest_back(exit_equity, money_in, interest):
        difference = exit_equity - money_in
        if difference > interest:
            return interest
        else:
            return difference  

    # calculates money back and MoM
    def returns(exit_equity, money_in, interest_back, percent):
        remaining = exit_equity - money_in - interest_back
        back = remaining * percent
        back_final = back + money_in + interest_back
        mom = back_final / money_in
        return print("Return (PP): {}".format(back_final)+"\n"+"The MoM is (PP): {}".format(mom))

    #### PP framework (Participating Preferred) ###
    def finalpp(money_in, PIK, start_date, end_date, exit_equity, percent):
      interest = returns.preferred_return(money_in, PIK, start_date, end_date)
      interest_back1 = returns.interest_back(exit_equity, money_in, interest)
      remaining_split = returns.returns(exit_equity, money_in, interest_back1, percent)
      return remaining_split

    ### CP framework (Common Catch-Up on Preferred####
    def finalcp(money_in, PIK, start_date, end_date, exit_equity, percent):
      interest = returns.preferred_return(money_in, PIK, start_date, end_date)
      interest_back1 = returns.interest_back(exit_equity, money_in, interest)
      cp = (interest_back1/percent) * (1-percent)
      remaining = exit_equity - money_in - interest_back1 - cp
      back = remaining * percent
      back_final = back + money_in + interest_back1
      mom = back_final / money_in
      return print("Return (CP): {}".format(back_final)+"\n"+"The MoM is (CP): {}".format(mom))

money_in = 50
PIK = 0.1
start_date = date(2017, 12, 31)
end_date = date(2022, 12, 31)
exit_equity = 200
percent = returns.fd_percent([50, 100, 50])[0] ## always put you first in the list

returns.finalpp(money_in, PIK, start_date, end_date, exit_equity, percent)
returns.finalcp(money_in, PIK, start_date, end_date, exit_equity, percent)

money_in = 50
PIK = 0.1
start_date = date(2017, 12, 31)
end_date = date(2022, 12, 31)
exit_equity = 500
percent = 0.25

returns.finalpp(money_in, PIK, start_date, end_date, exit_equity, percent)

shares = [50, 100, 50, 150]
shareholder1 = returns.fd_percent(shares)[0] 
shareholder2 = returns.fd_percent(shares)[1]
shareholder3 = returns.fd_percent(shares)[2]
shareholder4 = returns.fd_percent(shares)[3]
print(shareholder1)
print(shareholder2)
print(shareholder3)
print(shareholder4)
