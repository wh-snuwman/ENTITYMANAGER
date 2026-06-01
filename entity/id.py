from random import choice
l = [i for i in 'QAZWSXEDCRFVTGBYHNUJMIKOLPqazwsxedcrfvtgbyhnujmikolp1234567890']

def entityId():
    id = ''
    for i in range(20):
        id += choice(l)
    return id