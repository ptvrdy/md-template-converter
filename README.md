# README for CSV to Markdown README Template Converter  

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)  

National Transportation Library (NTL). Bureau of Transportation Statistics (BTS), U.S. Department of Transportation (USDOT). [ROR ID: https://ror.org/00snbrd52](https://ror.org/00snbrd52)    
2024-07-26  

## Links to Software  
Program Archive Link: <https://github.com/tvrdy-ctr/md-template-converter>   

## Table of Contents  
A. [General Information](#a-general-information)  
B. [Sharing/Access & Policies Information](#b-sharingaccess-and-policies-information)  
C. [Data and Related Files Overview](#c-data-and-related-files-overview)  
D. [Update Log](#f-update-log)  

**Title of Dataset:**  CSV to Markdown README Template Converter  

**Description of the Program:** This program converts each row of a CSV file into a separate markdown README file. Any markdown template can be used and created for this program. But for this program to work, the replacement values in the markdown file must match the CSV headers. For example, to replace the value if "`Insert Geographic Location Here`" in the markdown template, the CSV must also have the header "`Insert Geographic Location Here`" exactly the same. Templates can be modified and adjusted for different use cases. It may be best to initially work in an XLSX spreadsheet to capture all information needed for the README and adjust with Macros and formulas before converting to CSV for this program. This will also work well if you have this metadata already in a CSV or XLSX file, but you use a macro to transform the headings to the values that match the README file. Because this program is so simple, the possibilities are endless! 

*Note: This program does not delete any blank fields or add additional fields. If you do not wish to use certain values or wish to add more, adjust the template. If values are left blank, ensure you delete the unnecessary fields from the README before publication and use.*

**Program Archive Link:** <https://github.com/tvrdy-ctr/md-template-converter>  

**Authorship Information:**  

>  *Principle Author Contact Information*  
>  Name: Joseph Lambeth  
>  Email: josephwlambeth@gmail.com  

>  *Supporting Author Contact Information*  
>  Name: Peyton Tvrdy ([0000-0002-9720-4725](https://orcid.org/0000-0002-9720-4725))   
>  Institution: National Transportation Library [(ROR ID: https://ror.org/00snbrd52](https://ror.org/00snbrd52))     
>  Email: peyton.tvrdy123@gmail.com   


## B. Sharing/Access and Policies Information  

**Recommended citation for the data:**  

>  Lambeth, Joseph and Peyton Tvrdy (2024). *CSV to Markdown README Template Converter*. <https://github.com/tvrdy-ctr/md-template-converter>  

**Licenses/restrictions placed on the data:** 
 [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg  

License file and display taken from "cc-licenses" by santisoler: <https://github.com/santisoler/cc-licenses?tab=readme-ov-file>  

 
## C. Data and Related Files Overview  

File List for CSV to markdown README Template Converter  

>  1. Filename: README.md  
>  Short Description:  The README file you are reading now. Contains project and copyright information.   

>  2. Filename: CSV_Template_Blank.csv  
>  Short Description:  This is the blank version of the CSV template with all of the correct headers for the README template README_Template.md. This file can be copied and adjusted to fit your README needs.  

>  3. Filename: CSV_Template_Example.csv  
>  Short Description:  This is the CSV file that contains the header row for README_Template.md but contains dummy data in rows 2 and 3. This file is used mostly for testing but can also be used to better demonstrate what information should be added to your README template.    

>  4. Filename: markdown-templater.py  
>  Short Description:  This is the main python file for this project. It contains all of the project's code.   

>  5. Filename: README_Template.md  
>  Short Description:  This is the README Template file. This file can be copied and adjusted to fit your README needs.   


**Instrument or software-specific information needed for this project:** This project was created using VS Code. Editing READMEs with the ["Markdwon Preview Enhanced"](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced) extension is highly recommended. CSVs were created using Excel but may also be opened/edited in Notepad++.   

## D. Update Log  

This README.md file was originally created on 2024-07-26 by Peyton Tvrdy ([0000-0002-9720-4725](https://orcid.org/0000-0002-9720-4725)), Data Management and Data Curation Fellow, National Transportation Library <peyton.tvrdy.ctr@dot.gov>  
 
2024-07-26: Original file created  
