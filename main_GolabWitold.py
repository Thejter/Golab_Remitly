import resourceChecker_GolabWitold as rc

print("This method will return False if JSON Resource field contains a single asterisk and True in any other case.")
print("This method returned:", rc.checkResourceFieldInJsonFile("data.json"))