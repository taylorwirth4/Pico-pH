# splits and parses the version settings response into values we can read
# response = ('#VERS 4 1 405 1071 2 271')
def parse(response):

    spl = response.split()
    firmver = f'{float(spl[3])/100:.2f}'
    build = spl[5]

    parsed_version_info = firmver+','+build    

    return parsed_version_info