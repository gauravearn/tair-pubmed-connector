import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
def readTairNCBI(input, output, arg_id):
    """
    _summary_
    this function establishes the missing link between the 
    tair and the pubmed, given the file ATH_GO_GOSLIM.txt
    and an output file name and the specific locus or the
    gene id, it will first fetch the corresponding pubmed id
    and then will fetch the corresponding abstract for those 
    pubmed id. Establishes a connecting link between the 
    gene and locus to language model training. 

    Arguments:
        input -- _description_
        ATH_GO_GOSLIM.txt from the TAIR release
        output -- _description_
        the output file name
        arg_id -- _description_
        gene or locus id. 

    Returns:
        _description_
        A nested list with the pubmed id and the corresponding 
        publication details.
    """
    with open(input, "r") as file_read:
        with open(output, "w") as file_out:
            for line in file_read.readlines():
                if line.startswith("!"):
                    continue
                file_out.write(line)
    with open(output, "r") as file_re_read:
        read_file = pd.read_csv(output, sep = "\t")
        correspondence = read_file.iloc[::,[1,12]].iloc[::,1]. \
                           apply(lambda n: n.split("|")).to_list()
        gene_id = list(map(lambda n: n.replace("gene:", ""), \
                            map(lambda n: n.replace("locus:", ""), \
                                         read_file.iloc[::,1].to_list())))
    pubmed = []
    for i in range(len(correspondence)):
        pubmed.append([gene_id[i],correspondence[i]])
    format_id = set([j.replace("PMID:", "") for i in ([i.split() \
                    for i in ([j for i in [pubmed[i][1] for i \
                                in range(len(pubmed)) if pubmed[i][0] == arg_id] \
                                          for j in i]) if "PMID" in i]) for j in i])
    format_id_links = list(format_id)
    format_check = [] 
    for i in range(len(format_id_links)):
        format_check.append(f"https://pubmed.ncbi.nlm.nih.gov/{format_id_links[i]}/")
    ncbi_derive_information = {}
    for i in range(len(format_check)):
        ncbi_derive_information[format_check[i]] = ''.join([i.get_text().strip() \
            for i in BeautifulSoup(urlopen(format_check[i]), \
                "html.parser").find_all("div", class_ = "abstract-content selected")])
    return [(k,v) for k,v in ncbi_derive_information.items() if k or v != ""] 
