from prettytable import PrettyTable
    
mytable = PrettyTable()

mytable.field_names = ["Course name", "Meeting Days", "Location", "Instructor"]

mytable.add_row(["CPS3500", "MW", "Virtual", "Y. Kumar"])
mytable.add_row(["CPS3320", "W", "Virtual", "R. Domanski"])
mytable.add_row(["COMM1402", "F", "Virtual", "J. Ernst"])
mytable.add_row(["MATH2416", "MW", "Virtual", "F. Jamedar"])
mytable.add_row(["CPS3250", "TTH", "Virtual", "E. Emmanoulidis"])
mytable.add_row(["CPS3962", "TTH", "Virtual", "J. Chu"])

mytable.del_row(5)

print(mytable)