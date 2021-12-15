'''
Filename: e:\GitHub_clones\Apella-plus-thesis\scraper_py\scriptTest_file.py
Path: e:\GitHub_clones\Apella-plus-thesis\scraper_py
Created Date: Friday, December 10th 2021, 12:39:16 am
Author: nikifori

Copyright (c) 2021 Your Company
'''

import pandas as pd
import json
from semantic_scholar_scraper import *

# correct main authors list - fix unscraped authors
def correct_authors(main_authors_list: list, authors2add: list):
    cc=0
    for unlist_author in authors2add:
        for counter, author in enumerate(main_authors_list):
            if unlist_author["name"]==author["name"]:
                cc+=1
                print(cc)
                main_authors_list[counter] = unlist_author
    
    # return main_authors_list

# check unscraped authors
def check_unscraped_authors(authors_list: list):
    cc = 0
    unscraped_authors = []   
    for author in authors_list:
        if "Publications" not in author:
            unscraped_authors.append(author)
            print(author["name"])
            cc += 1
            print(cc)
    print(cc)
    return unscraped_authors

if __name__ == '__main__':
    # save dictionary as json file
    # json_file = json.dumps(authors_out_of_GS, indent=4)
    # with open(fr'..\json_files\csd_out_with_abstract\csd_out_authors_out_of_GS.json', 'w', encoding='utf-8') as f:
    #     f.write(json_file)
    
    csd_out_specter = open_json("csd_out_with_abstract\csd_out_specter_with_410_authors.json")
    csd_out_with_abstracts_30_missing_with_410_authors = open_json("csd_out_with_abstract\csd_out_with_abstracts_30_missing_with_410_authors.json")
    # csd_out_with_abstracts_30_missing = open_json("csd_out_with_abstract\csd_out_with_abstracts_30_missing.json")
    # save2json(json_fi=csd_out_specter, path2save="csd_out_with_abstract\csd_out_specter_with_410_authors.json")
    
    unscraped_authors = check_unscraped_authors(csd_out_specter)
    unscraped_authors = check_unscraped_authors(csd_out_with_abstracts_30_missing_with_410_authors)
    # correct_authors(csd_out_specter, can_not_fetch_complete)
    
    df = pd.read_csv(r'..\csv_files\csd_data_out_processed_ground_truth.csv')
    
    # add 2 authors that didnt exist in main json file without specter embeddings
    # temp_list = []
    # for author in csd_out_with_abstracts_30_missing:
    #     temp_list.append(author.get("name"))
    
    # temp_df = pd.DataFrame(temp_list, columns=["name"])
    
    # matched = (temp_df["name"]==df["name"])
    
    # for i in df["name"]:
    #     counter = 0
    #     for k in temp_df["name"]:
    #         if k==i:
    #             counter=1
    #     if counter==0:
    #         print(i)      
    # save2json(csd_out_with_abstracts_30_missing, "csd_out_with_abstract\csd_out_with_abstracts_30_missing2.json")  
    #---------------------------------------------------------------------------------------------------------------
    # csd_out_specter.append(csd_out_with_abstracts_30_missing[-2])
    
    # csd_out_researchgate_only_titles = open_json("csd_out_with_abstract/csd_out_researchgate_only_titles.json")
    # correct_authors(csd_out_with_abstracts_30_missing_with_410_authors, csd_out_researchgate_only_titles)
    # save2json(csd_out_with_abstracts_30_missing_with_410_authors, path2save="csd_out_with_abstract\csd_out_completed_missing_2.json")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
