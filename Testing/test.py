"""
chnhash provides you with the functionalities of generating and comparing hash values.
Copyright (C) 2022-2023 Himashana Suraweera (Email : Himashana@chnsoftwaredevelopers.com)

This file is part of chnhash.

chnhash is free software: you can redistribute it and/or modify it under the terms of the GNU General
Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

chnhash is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even
the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with chnhash. If not, see
<https://www.gnu.org/licenses/>.

"""

from prettytable import PrettyTable
import compareHash

testCases = [{'input' : ["sha512", "File.txt", "b1df216b5b05e3965c469492744a5de0c945e0b103c42eb1e57476fbed8f1d489f5cae9b792db37c5d823bc0c6c7d06b056176d6abe5ce076eeadaed414e17a3"], 'expected' : "OK"},
             {'input' : ["sha512", "File.txt", "received_hash.txt"], 'expected' : "OK"}]

testResultsTable = PrettyTable(["", "Input", "Expected", "Actual", "Result"])

print("Inputs: ")

for num, test in enumerate(testCases):
    result = compareHash.compareHash(test['input'][0], test['input'][1], test['input'][2])
    
    testInfo = "Test " + str(num + 1) + " "
    inputId = "#" + str(num + 1)

    print(inputId + " : " + str(test['input']))

    if result[3] == test['expected']:
        status = "PASSED"
    else:
        status = "FAILED"

    testResultsTable.add_row([testInfo, inputId, test['expected'], result[3], status])

print("\n")
print(testResultsTable)