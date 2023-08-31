jumbled_list = ['DocToR_sTRAngE','sPidERmaN','MoON_KnigHT','caPTAIN_aMERIca','hULK']

indices = []
decoded_names =[]

for index, superhero in enumerate(jumbled_list):
    indices.append(index)
    superhero = superhero.lower().replace("_", " ")  # Converting the names to lowercase and replacing the underscore with a whitespace
    decoded_names.append(superhero)  # Appending the decoded names into the new list

name_lengths =[]

name_lengths = map(lambda hero: len(hero),decoded_names)  # Calculating the length of the decoded names by using the lambda function

name_lengths = list(name_lengths) 

indices.sort(key = lambda name: name_lengths[name])  # Sorting the indices with respect to name lengths

for index in indices: 
    print(decoded_names[index].title())   # Printing the decoded names based on sequence of indices and converting the case to title case

print (indices)
print(decoded_names)
print(name_lengths)

