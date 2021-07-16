import json

def notMaleOrFemale():
    #open the file
    num = 0
    total = 0
    pat = "MOCK_DATA.json"
    with open(pat) as f:

        records = json.load(f)
    for rec in records:
        total += 1
        if rec['gender'] == "Male" or rec['gender'] == "Female":
            num += 1
    print(f"""
        Records total ====> {total}
        Number not male or female ===> {num}
        """)
    return num


if __name__ == "__main__":
    notMaleOrFemale()