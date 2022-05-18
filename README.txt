# OBJECTIVE
# To use a regular expression to find newer ancient pieces of art
# that were not created in the BC era. 

# More specifically, my code says to look in data['objectDate'], 
# and if it does not match the regex for "BC" to print out data['title'], 
# data['objectID'], and data['objectBeginDate']. The context I had 
# in mind was that while these are all very old pieces of art, I 
# wanted to find newer ancient pieces that were not created in the BC era

# We are working with the Met's department 3, which is
# Ancient Near Eastern Art.

# We need to open up all 4520 files. (There are actually over 6000,
# but there was some type of disruption during the parsing, so I 
# only ended up with 4520.)

# PROCESS
# 1) I used the file "download_ancient.py" to collect all the data, and each art piece's
# data was collected into its own json file in a folder called "data"
# 2) Then, I used the file "parse_ancient.py" to run the regular expression through all the json 
# files and find all the pieces that did not have "BC" in the date text


# ISSUES
# When I checked in the Terminal, most of the output is correct, but as I scrolled,
# almost all of the 'objectBeginDate' ouput was in the postive, insinuating that it was
# from the AD era. But I saw a line that said, "Bracelet 322384 -1000". When I investigated this
# object ID at https://collectionapi.metmuseum.org/public/collection/v1/objects/322384,
# for "objectDate" it says "n.d.a.", and then for "objectBeginDate," sure enough, it says "-1000"
# which is definitely in the BC era. When investigating initially, I had actually
# changed my regex because of differences I'd found in this field. However, 
# something like "n.d.a." was not something I'd come across.
