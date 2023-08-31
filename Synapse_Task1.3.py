encoded_lists = [[1,2,3,4,6], [5,7,8,9,15],[12,14,16,18],[10,11,12,13,16,17,18,20]]

def exploded_chains(lst): # Function to remove the consecutive codes

    for sublist  in lst:
        for j, element in enumerate(sublist):
            
            if j <= len(sublist)-2 and sublist[j]+1 == sublist[j+1] and sublist[j+1]+1 == sublist[j+2]:
                sublist.remove(sublist[j+2])  # Removing the consecutive numbers in reverse order
                sublist.remove(sublist[j+1])
                sublist.remove(sublist[j])

       
    return lst

result = exploded_chains(encoded_lists) # Function calling
print(result)