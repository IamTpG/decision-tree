import csv

def IsInt(n):
    try:
        float_n = float(n)
        int_n = int(float_n)
    except ValueError:
        return False
    else:
        return float_n == int_n


def IsFloat(n):
    try:
        float_n = float(n)
    except ValueError:
        return False
    else:
        return True
    

def StandardiseColumn(rows, id):
    """Convert an entire column to a float or integer if possible."""

    isInt = True
    isFloat = True

    for i in range(1, len(rows)):
        if (not IsInt(rows[i][id])):
            isInt = False
        if (not IsFloat(rows[i][id])):
            isFloat = False
        if (not isInt and not isFloat):
            return rows
    
    for i in range(1, len(rows)):
        rows[i][id] = float(rows[i][id])
        if (isInt):
            rows[i][id] = int(rows[i][id])

    return rows


def ReadFile(filename):
    """Read data and return it as rows"""

    filename = "source\\dataset\\" + filename + ".csv"
    rows = []

    with open(filename, newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            rows.append(row)

    for j in range(len(rows[0])):
        rows = StandardiseColumn(rows, j)

    return rows


def StandardiseFile(filename):
    """Remove rows having unknown data"""

    newfile = "source\\dataset\\standardised." + filename + ".csv"
    filename = "source\\dataset\\origin." + filename + ".csv"
    rows = []

    with open(filename, newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            if not ('?' in row or "NA" in row):
                rows.append(row)

    for j in range(len(rows[0])):
        rows = StandardiseColumn(rows, j)

    f = open(newfile, "w")
    f.close()

    with open(newfile, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in rows:
            spamwriter.writerow(row)