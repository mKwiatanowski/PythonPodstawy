# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 14:46:07 2023

@author: mateu
"""



# ustalenie czy dany dzien jest dniem roboczym 


def GiveWorkindDay():
    
    # prints the nearest working day date
    
    from datetime import date
    from datetime import timedelta
    
    #day = date.today()
    day = date(2017,9,30)
    
    
    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day
    
    
    print("Working day for", day, "is", workingday)

    return


GiveWorkindDay()



from datetime import date


def DayToEndOfYear():

    date_today = date.today()
    current_year = date_today.year
    date_end_year = date(current_year,12,31)
    delta = date_end_year - date_today
    print(delta.days)

    return



DayToEndOfYear()























