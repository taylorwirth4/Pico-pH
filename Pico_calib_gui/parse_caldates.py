 
# splits and parses the raw calibration dates response into dates we can read
#response = ('RMR1 31 0 7 1054220830 977220831 900001231 0 0 0 0')
import datetime as datetime
def parse(response):
    spl = response.split()
    if spl[6] == spl[7]: # only zeros in response
        caldates_header = 'topR1date'+','+'bottomR2date'+','+'offsetdate\n'
        parsed_cal_dates = '12/31/2000 00:00:00,12/31/2000 00:00:00,12/31/2000 00:00:00\n'
    else:
        spl = response.split()
        R1date = int(spl[4])
        R1day = R1date-100*(R1date//100)
        R1mon = ((R1date//100)-100*((R1date//100)//100))
        R1year = ((R1date//10000)-100*((R1date//10000)//100))+2000
        R1hour = (R1date//1000000)//60
        R1min = ((R1date//1000000)-60*((R1date//1000000)//60))
        R1str = str(datetime.datetime(R1year,R1mon,R1day,R1hour,R1min))

        R2date = int(spl[5])
        R2day = R2date-100*(R2date//100)
        R2mon = ((R2date//100)-100*((R2date//100)//100))
        R2year = ((R2date//10000)-100*((R2date//10000)//100))+2000
        R2hour = (R2date//1000000)//60
        R2min = ((R2date//1000000)-60*((R2date//1000000)//60))
        R2str = str(datetime.datetime(R2year,R2mon,R2day,R2hour,R2min))

        offdate = int(spl[6])
        offday = offdate-100*(offdate//100)
        offmon = ((offdate//100)-100*((offdate//100)//100))
        offyear = ((offdate//10000)-100*((offdate//10000)//100))+2000
        offhour = (offdate//1000000)//60
        offmin = ((offdate//1000000)-60*((offdate//1000000)//60))
        offstr = str(datetime.datetime(offyear,offmon,offday,offhour,offmin))

        caldates_header = 'topR1date'+','+'bottomR2date'+','+'offsetdate\n'
        parsed_cal_dates = R1str+','+R2str+','+offstr+'\n'
    return caldates_header+parsed_cal_dates