seconds = int(input("Enter the number of seconds: "))
minutes = seconds / 60
sec = seconds % 60
sec2 = seconds % (60*60)
sec3 = seconds % (60*60*60)
hours = minutes / 60
days = hours / 24


if seconds >= 86400 :
    print('{} seconds are equal to:'.format(seconds))
    print('{} full minutes(s) and {} seconds.'.format(minutes, sec))
    print(str(int(hours)) + ' full hours(s) and ' + str(int(sec2)) + ' seconds.')
    print(str(int(days)) + ' full days(s) and ' + str(int(sec3)) + ' seconds.')
elif seconds >= 3600:
    print(str(int(seconds)) + ' seconds are equal to:')
    print(str(int(minutes)) + ' full minutes(s) and '+ str(int(sec)) + ' seconds.')
    print(str(int(hours)) + ' full hours(s) and ' + str(int(sec2)) + ' seconds.')          
elif seconds >= 60:
    print(str(int(seconds)) + ' seconds are equal to:')
    print(str(int(minutes)) + ' full minutes(s) and '+ str(int(sec)) + ' seconds.')
else:
    print(str(int(seconds)) + ' seconds.')

#branch Hyebin에서 수정함
#tobigs fighthing:)
    
