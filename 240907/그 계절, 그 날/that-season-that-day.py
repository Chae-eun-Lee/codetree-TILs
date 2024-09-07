y, m, d = map(int, input().split())
def s_year(n):
    if n%400 == 0:
        return True
    if n%100 == 0:
        return False
    if n%4 == 0:
        return True
def season(y, m, d):
    s_month = [2, 4, 6, 9, 11]
    if (m in s_month) and d == 31:
        return -1
    if (m == 2) and (d == 29):
        if not s_year(y):
            return -1
    if (m == 2) and (d == 30):
        return -1
    if m >= 3 and m <= 5:
        return 'Spring'
    elif m >= 6 and m <=8:
        return 'Summer'
    elif m >=9 and m <= 11:
        return 'Fall'
    else:
        return 'Winter'
print(season(y, m, d))