def calculate(interest,principal):
    row1 = [0 for x in range(25)]
    row2 = [0 for x in range(25)]
    row3 = [0 for x in range(25)]
    for x in range(0, 25):
        r = compound_interest(interest,principal,12,x+1)
        row1[x] = r[0]
        row2[x] = r[1]
        row3[x] = r[2]
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
    r[0] = amount
    r[1] = totalCost
    r[2] = percent
    #print r
    return r

def calculateAmortization(years,interest,principal,cuota):
    cuota = compound_interest(interest,principal,12,years)[0]
    months = years * 12
    interest = interest / 1200
    intereses =    [0 for x in range(months)]
    amortizacion = [0 for x in range(months)]
    capital =      [0 for x in range(months)]
    
    # Defino los primeros
    intereses[0]    = principal * interest 
    amortizacion[0] = cuota - intereses[0]
    capital[0]      = principal - amortizacion[0]
    
    # Defino todos los demas
    for x in range(1, months):
        intereses[x]    = capital[x-1] * interest
        amortizacion[x] = cuota - intereses[x]
        capital[x]      = capital[x-1] - amortizacion[x]
    capital[months] = 0
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