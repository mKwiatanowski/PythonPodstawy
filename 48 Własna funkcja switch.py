# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 11:40:28 2023

@author: mateu
"""

'''
# tworzenie wlasnej funkcji switch / case. W pythonie nie ma czegos takiego, co jest w innych jezykach programowania


function(argument){
    
    # tak bysmy to zrobili w innych jezykach programowania polega to na przetlumaczeniu numeru dnia tygodnia
    # na jak w tym wypadku jezyk francuski
    switch(argument)
    
        case 0:
            return "lundi";
        case 1:
            return "mardi";
        case 2:
            return "mercredi";
        case 3:
            return "jeudi";
        case 4:
            return "vendredi";
        case 5:
            return "samedi";
        case 6:
            return "dimanche";
        default :
            return "! error !";

    }:
}:
    
niestety powyyzszy zapis nie jest dostepny w pythonie

'''

# obejscie na gazomierzu 


def WeekDayInFrench (dayNumber):
    
    names = {
        0: "lundi",
        1: "mardi",
        2: "mercredi",
        3: "jeudi",
        4: "vendredi",
        5: "samedi",
        6: "dimanche"
        }
    # get(x,"gdyby nic nie zostalo znalezione") zwrocenie dla names dayNumber
    
    return names.get(dayNumber,"Error")
    


print(WeekDayInFrench(8))











































