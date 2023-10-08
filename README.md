# tair_pubmed_connector
There is no function to fetch automatically the information on the reported pubmed articles links in the tair to be used for the language models, so i coded this function which will take the tair information, a gene or locus tag and will fetch the corresponding pubmed and then from the pubmed the corresponding abstracts, which can be directly used for the text summarization into langchain or the llm models. 
```python
readTairNCBI("/Users/gauravsablok/Desktop/CodeCheck/release/ATH_GO_GOSLIM.txt", \
                  "/Users/gauravsablok/Desktop/CodeCheck/release/ATH_GO_GOSLIM.out", \
                          "2200935")
# this is just a reference id for checking the functionality
[('https://pubmed.ncbi.nlm.nih.gov/30356219/',
  'Nitrogen is an essential macronutrient for plant growth and basic metabolic processes. 
  The application of nitrogen-containing fertilizer increases yield, which has been a 
  substantial factor in the green revolution1. Ecologically, however, excessive application 
  of fertilizer has disastrous effects such as eutrophication2. A better understanding 
  of how plants regulate nitrogen metabolism is critical to increase plant yield and reduce 
  fertilizer overuse. Here we present a transcriptional regulatory network and twenty-one 
  transcription factors that regulate the architecture of root and shoot systems in response 
  to changes in nitrogen availability. Genetic perturbation of a subset of these transcription 
  factors revealed coordinate transcriptional regulation of enzymes involved in nitrogen metabolism. 
  Transcriptional regulators in the network are transcriptionally modified by feedback via 
  genetic perturbation of nitrogen metabolism. The network, genes and gene-regulatory modules 
  identified here will prove critical to increasing agricultural productivity.'),
 ('https://pubmed.ncbi.nlm.nih.gov/34562334/',
  'Unraveling gene function is pivotal to understanding the signaling cascades that control plant 
  development and stress responses. As experimental profiling is costly and labor intensive, 
  there is a clear need for high-confidence computational annotation. In contrast to detailed 
  gene-specific functional information, transcriptomics data are widely available for both model and 
  crop species. Here, we describe a novel automated function prediction method, which leverages 
  complementary information from multiple expression datasets by analyzing study-specific gene 
  co-expression networks. First, we benchmarked the prediction performance on recently characterized 
  Arabidopsis thaliana genes, and showed that our method outperforms state-of-the-art expression-based 
  approaches. Next, we predicted biological process annotations for known (n = 15 790) and unknown 
  (n = 11 865) genes in A. thaliana and validated our predictions using experimental protein-DNA and 
  protein-protein interaction data (covering >220 000 interactions in total), obtaining a set of 
  high-confidence functional annotations. Our method assigned at least one validated annotation to 
  5054 (42.6%) unknown genes, and at least one novel validated function to 3408 (53.0%) genes with 
  computational annotations only. These omics-supported functional annotations shed light on a 
  variety of developmental processes and molecular responses, such as flower and root development, 
  defense responses to fungi and bacteria, and phytohormone signaling, and help fill the information 
  gap on biological process annotations in Arabidopsis. An in-depth analysis of two context-specific 
  networks, modeling seed development and response to water deprivation, shows how previously 
  uncharacterized genes function within the respective networks. Moreover, our automated function 
  prediction approach can be applied in future studies to facilitate gene discovery for crop improvement.'),
 ('https://pubmed.ncbi.nlm.nih.gov/11118137/',
  'The completion of the Arabidopsis thaliana genome sequence allows a comparative analysis of 
  transcriptional regulators across the three eukaryotic kingdoms. Arabidopsis dedicates over 
  5% of its genome to code for more than 1500 transcription factors, about 45% of which are from 
  families specific to plants. Arabidopsis transcription factors that belong to families common 
  to all eukaryotes do not share significant similarity with those of the other kingdoms beyond the 
  conserved DNA binding domains, many of which have been arranged in combinations specific to each 
  lineage. The genome-wide comparison reveals the evolutionary generation of diversity in the 
  regulation of transcription.')]
```
Gaurav Sablok \
ORCID: https://orcid.org/0000-0002-4157-9405 \
WOS: https://www.webofscience.com/wos/author/record/C-5940-2014 \
RubyGems Published: https://rubygems.org/profiles/sablokgaurav \
Python Packages Published : https://pypi.org/user/sablokgaurav/
