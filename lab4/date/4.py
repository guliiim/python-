from datetime import datetime ,time

d1=datetime.strptime('2000-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')
d2=datetime.strptime('2022-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')

def diff(d1,d2):
    d=d2-d1
    return d.days*24*3600+d.seconds

print(diff(d1,d2))