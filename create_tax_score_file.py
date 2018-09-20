#uses the json output of blobtools create to create a file showing the tax,score of selected hits
import json
import sys

genusscore = open (sys.argv[1], "w")
with open (sys.argv[2])as blobdb:
    #load the json from a string to a python format dict
    parsed_blobdb = json.load(blobdb)  
    
    #loop through json until get to correctly structured nodes
    for contigslist in parsed_blobdb["dict_of_blobs"].items():
        contigstats = contigslist[1]
        #print (contigstats[3])
        for tup in contigstats.items():
            if "taxonomy" in tup:
                contigtaxon = tup
                taxdict = contigtaxon[1]
                for t in taxdict.items():
                    genusinfo = t[1].get("genus")
                    score = str(genusinfo.get("score"))
                    tax = genusinfo.get("tax")
                    if tax != "no-hit":
                        genusscore.write(tax)
                        genusscore.write(",")
                        genusscore.write(score)
                        genusscore.write("\n")
genusscore.close()
