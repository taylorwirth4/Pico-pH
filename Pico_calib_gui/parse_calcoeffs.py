# splits and parses the raw calibration information response into values we can read
#response = ('RMR1 1 0 30 8082 1028000 57800 -15400 -1480 -2470 0 32500 623000 969700 126300 343 0 0 23515 2395 10310 2000 622201 57293 10888 10300 6000 622367 1416295 -5853 0 0 0 0')

def parse(response):
    s = response.split()
    R1 = str(round((int(s[4])*10**-6),6))
    pH1 = str(round(int(s[5])*10**-3,6)) # pH
    temp1 = str(round(int(s[6])*10**-3,6)) # C
    sal1 = str(round(int(s[7])*10**-3,6)) # g/L
    R2 = str(round(int(s[8])*10**-6,6))
    pH2 = str(round(int(s[9])*10**-3,6)) # pH
    temp2 = str(round(int(s[10])*10**-3,6)) # C) 
    sal2 = str(round(int(s[11])*10**-3,6)) # g/L
    offset = str(round(int(s[12])*10**-3,6)) # pH
    dphi_ref = str(round(int(s[13])*10**-3,6)) # degrees
    att_coeff = str(round(int(s[14])*10**-6,6)) # 1/m
    bAmp = str(round(int(s[15])*10**-3,6)) # mV
    bdphi = str(round(int(s[16])*10**-3,6)) # degrees
    dsf = str(round(int(s[17])*10**-6,6)) 
    dtf = str(round(int(s[18])*10**-6,6))
    pka = str(round(int(s[19])*10**-3,6)) # pH
    slope = str(round(int(s[20])*10**-6,6))
    bottomt = str(round(int(s[21])*10**-6,6)) # 1/K
    topt = str(round(int(s[22])*10**-6,6)) # 1/K
    slope_t = str(round(int(s[23])*10**-6,6)) # 1/K
    pka_t = str(round(int(s[24])*10**-6,6)) # pH/K
    pka1 = str(round(int(s[25])*10**-3,6))
    pka2 = str(round(int(s[26])*10**-3,6))

    calcoefheader = ','.join(['R1','pH1','temp1','salinity1','R2','pH2','temp2','salinity2',
                        'offset','dphi_ref','att_coeff','bkgAmpl','bkgdDphi','dsf_dye',
                        'dtf_dye','pka','slope','bottom_t','top_t','slope_t','pka_t',
                        'pka_is1','pka_is2\n'])
    calcoefstr = [R1,pH1,temp1,sal1,R2,pH2,temp2,sal2,offset,dphi_ref,att_coeff,bAmp,
                    bdphi,dsf,dtf,pka,slope,bottomt,topt,slope_t,pka_t,pka1,pka2]

    return calcoefheader+(','.join(calcoefstr))+'\n'