"""Mappability Presentation Below is some data from calculating the 
mappability of some regions of the genome for sequencing reads of 
different sizes. 

Read Length    Fragments   Mappable
30  1725    697
40  1713    794
50  1689    912
70  1677    1103
85  1660    1187

From the data calculate the percentage mappability 
(mapped fragments as a percentage of total fragments), 
and then write out the results as nicely formatted text using f-strings.  

Your output should look something like: 
30bp  40.0% 
40bp  46.4% 
Etc. 

To load this data initially copy it into a triple quoted string in your 
script so you can have multiple lines.  
Use the split method to split on newlines (\n) so you can get a list of lines.  
Use a for loop to iterate through the lines so you can split out the different values, 
calculate the mappability, then populate a dictionary with the Read Length as the key, 
and the mappability as the value. 

Once you’ve read the whole dataset and populated the dictionary use a for loop to go 
through the dictionary and generate f-strings to print out nicely formatted versions of your results. """

mapp_string = """Read Length    Fragments   Mappable
30  1725    697
40  1713    794
50  1689    912
70  1677    1103
85  1660    1187"""
mapp_dict = {}

for line in mapp_string.split("\n"):
    sp_line = line.split()
    if len(sp_line) == 3:
        length, frag, mapp = sp_line
        percent = round((float(mapp)/float(frag))*100, 1)
        mapp_dict[length] = percent

for k,v in mapp_dict.items():
   print(f"{k}bp   {v}%")


