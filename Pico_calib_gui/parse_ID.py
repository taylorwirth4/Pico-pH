# splits and parses the unique ID number response into values we can read
#response = ('#IDNR 2636648693379505685')
def parse(response):

    spl = response.split()
    ID = spl[1]

    return ID
