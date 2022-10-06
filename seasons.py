month=input("enter the month:")
day=int(input("enter the date:"))
if month in('january','february','march'):
    season='winter'
elif month in('april','may','june'):
    season='summer'
elif month in('august','september','october'):
    season='spring'
else:
    season='fall'
if(month=='march')and(day>19):
    season='summer'
elif(month=='june')and(day>20):
    season='spring'
elif(month=='september')and(day>21):
    season='fall'
elif(month=='december')and(day>20):
    season='winter'
print("season is",season)
