import json

genusscore = open ("/Users/rachelgrant/Google Drive/Denver Lab/Blobs/binning_blobs/scoreandgenus.txt", "w")
with open ("/Users/rachelgrant/Google Drive/Denver Lab/Blobs/binning_blobs/Pp_GH2_blob.json")as blobdb:
    #load the json from a string to a python format dict
    parsed_blobdb = json.load(blobdb)
    
    #this takes us to the correct level where we have the score and the genus name under tax
#    genusinfo = parsed_blobdb["dict_of_blobs"]["contig_9"]["taxonomy"]["bestsum"]["genus"]    
    
    for contigslist in parsed_blobdb["dict_of_blobs"].items():
        contigstats = contigslist[1]
        #print (contigstats[3])
        for tup in contigstats.items():
            if "taxonomy" in tup:
                contigtaxon = tup
                taxdict = contigtaxon[1]
                for t in taxdict.items():
                    #print(t[1])
                    genusinfo = t[1].get("genus")
                    score = str(genusinfo.get("score"))
                    tax = genusinfo.get("tax")
                    if tax != "no-hit":
                        genusscore.write(tax)
                        genusscore.write(",")
                        genusscore.write(score)
                        genusscore.write("\n")
genusscore.close()
