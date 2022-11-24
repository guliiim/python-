from datetime import date ,timedelta

yes=date.today()-timedelta(1)
tod=date.today()
tom=date.today()+timedelta(1)
print(yes,tod,tom)