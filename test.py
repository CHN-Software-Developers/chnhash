from prettytable import PrettyTable
import compareHash

testCases = [{'input' : ["sha512", "test_files\File.txt", "b1df216b5b05e3965c469492744a5de0c945e0b103c42eb1e57476fbed8f1d489f5cae9b792db37c5d823bc0c6c7d06b056176d6abe5ce076eeadaed414e17a3"], 'expected' : "OK"},
             {'input' : ["sha512", "test_files\File.txt", "test_files\\received_hash.txt"], 'expected' : "OK"}]

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