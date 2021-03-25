day = 0
dayOfMonth = 0
month = 0
dva = 1

monthName = ''

for month in range (1,13):

   
        
        if(month==1) or (month==3) or (month==5) or (month==7) or (month==8) or (month==10) or (month==12):
            for dayOfMonth in range (1,32):
                day=day+1
                for dva in range (1,9):
                    if (day==2**dva):
                        if(month==1):
                            monthName='января'
                        if(month==3):
                            monthName='апреля'
                        if(month==5):
                            monthName='мая'
                        if(month==7):
                            monthName='июля'
                        if(month==8):
                            monthName='августа'
                        if(month==10):
                            monthName='октября'
                        if(month==12):
                            monthName='декабря'
                        print(dayOfMonth,' , ', monthName)
                
        if(month==4) or (month==6) or (month==9) or (month==11):
            for dayOfMonth in range (1,31):
                day=day+1
                for dva in range (1,9):
                    if (day==2**dva):
                        if(month==4):
                            monthName='апреля'
                        if(month==6):
                            monthName='июня'
                        if(month==9):
                            monthName='сентября'
                        if(month==11):
                            monthName='ноября'
                        print(dayOfMonth,' , ', monthName)
                
        if(month==2):
            for dayOfMonth in range (1,29):
                day=day+1
                for dva in range (1,9):
                    if (day==2**dva):    
                        print(dayOfMonth,' , февраля')
    

