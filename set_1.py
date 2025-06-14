
def savings(gross_pay, tax_rate, expenses):
    applied_tax_rate = gross_pay*tax_rate
    final_value = int(gross_pay-applied_tax_rate-expenses)
    return(final_value)


def material_waste(total_material, material_units, num_jobs, job_consumption):
    total_consumption= num_jobs*job_consumption
    remaining_material= str(total_material-total_consumption)+material_units
    return(remaining_material)


def interest(principal, rate, periods):
    final_value= int(principal+(rate*periods*principal))
    return(final_value)
