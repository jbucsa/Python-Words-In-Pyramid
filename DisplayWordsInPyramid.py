def decode(message_file):

    pyramid = {}  # Create a dictionary to store the pyramid structure
    with open(message_file, 'r') as file:
        for line in file:
            # print(line)
            num, word = line.strip().split()  # Split each line into number and word
            pyramid[int(num)] = word  # Add the number and word to the pyramid dictionary
    
    # decoded_message = ' '.join([pyramid[i] for i in sorted(pyramid.keys())])  # Join the words based on the sorted keys


    myPyramidKeys = list(pyramid.keys())
    myPyramidKeys.sort()
    sortedPyramid = {i: pyramid[i] for i in myPyramidKeys}
    # print(sortedPyramid.values())

    # decoded_message = ' '.join(sortedPyramid[i] for i in sortedPyramid.keys())
    decodeMessage = ""
    i = 1
    k = 2
    newLine = "\n"

    for key, value in sortedPyramid.items():
        if i == key:
            # print(i)
            # print(key)
            decodeMessage += ' ' + value + newLine
            i = i + k
            k += 1 
        else:
            decodeMessage += ' ' + value

    return decodeMessage

# Example usage
message_file = 'coding_qual_input.txt'
decodeMessage = decode(message_file)

print(decodeMessage)  