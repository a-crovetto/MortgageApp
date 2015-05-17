def calculate(interest,principal):
    # row = [0 for x in range(25)]
    # row1 = [[0 for x in range(25)] for x in range(3)]
    row1 = [0 for x in range(25)]
    row2 = [0 for x in range(25)]
    row3 = [0 for x in range(25)]
    for x in range(1, 26):
        r = compound_interest(interest,principal,12,x)
        row1[x-1] = r[0]
        row2[x-1] = r[1]
        row3[x-1] = r[2]
    rows = zip(row1,row2,row3)
    #print type(rows)
    return rows

def compound_interest(interest,principal,period,years):
    intCuota = interest/100/period    
    cuota = years*period
    amount = principal*(intCuota*((1+intCuota)**cuota)/((1+intCuota)**(cuota)-1))
    totalCost =  amount*cuota
    percent = totalCost/principal*100
    r = [0 for x in range(3)]
    r[0] = int(round(amount,0))
    r[1] = int(round(totalCost,0))
    r[2] = round(percent,2)
    #print r
    return r

def calculateAmortization(years,interest,principal,cuota):
    months = years * 12
    interest = interest / 12
    intereses =    [0 for x in range(months)]
    amortizacion = [0 for x in range(months)]
    capital =      [0 for x in range(months)]
    
    # Defino los primeros
    intereses[0]    = int(round(principal / interest / 100))
    amortizacion[0] = int(round(cuota - intereses[0]))
    capital[0]      = int(round(principal - amortizacion[0]))
    
    # Defino todos los demas
    for x in range(1, months):
        intereses[x]    = int(round(capital[x-1] / interest / 100))
        amortizacion[x] = int(round(cuota - intereses[x]))
        capital[x]      = int(round(capital[x-1] - amortizacion[x]))
    rows = zip(intereses,amortizacion,capital)
    #print type(rows)
    return rows


"""
def compound_interest(interest,principal,period,years):
    intCuota = interest/100/period    
    cuota = years*period
    amount = principal*(intCuota*((1+intCuota)**cuota)/((1+intCuota)**(cuota)-1))
    totalCost =  amount*cuota
    percent = totalCost/principal
    return int(round(amount,0)), totalCost, percent
    return {'amount': int(round(amount,0)),'totalCost': int(round(totalCost,0)),'percent': round(percent,2)}
"""