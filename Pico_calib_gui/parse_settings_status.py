# splits and parses the raw settings response into values we can read
#response = ('RMR1 30 0 24 1178796032 3 6 756 576 222757027 0 0 1 0 8 0 0 0 0 1000 0 0 0 0 0 0 0 0')
def parse(response):

    spl = response.split()
    codetype = int(spl[4]).to_bytes(4,'big').decode('utf-8')
    codetype = codetype.rstrip('\x00')
    codeLED = int(spl[5])
    let = ['A','B','C','D','E','F','G','H']
    codeLED = let[codeLED]
    codePD = int(spl[6])+1

    midblock = str(spl[7])
    lastblock = str(spl[8])

    sensorcode = codetype+codeLED+str(codePD)+'-'+midblock+'-'+lastblock
    SN = str(spl[9])

    settings_header = 'SensorCode,SerialNumber,UniqueID,FirmwareVersion,BuildNumber\n'
    parsed_settings_status = settings_header+sensorcode+','+SN+','

    return parsed_settings_status
