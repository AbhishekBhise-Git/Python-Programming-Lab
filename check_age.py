def check_age_eligibility(age):
    print(id(age))
    if age>18:
        return "valid"
    else:
        return "not valid"
a = 34
print(id(a))
print(check_age_eligibility(a))
