# HESPI : A PIPELINE TO DETECT INFORMATION ON HERBARIUM 

#### _This write-up is based off a oxford publish research paper on <u>```Hespi : a pipeline for automatically detecting information from herbarium specimen sheets```</u> , published by Robert Turnbull , Emily Fitzgerald , Karen M.Thompson and Joanne L. Birch_
----


### <u>Problems faced with Herbarium Specimens.</u>
There are over thousands of Herbaria globally . Where each contain like over 400 million physical specimens with valuable biological data. 

Digitizing these information has been happening over the past decade and is still in the process. 

One of the major issues in this field comes from Manual transcription of specimen labels , where the extraction rate of these specimens have been remained flat for over a long period of time. 

So in brief , researchers needed something , a tool which would help them to immediately extract informaton from such labels , fast and efficiently while also delivering the information to researchers accurately. 

**_This brought in the need for automation of these specimen labels and hence the birth of ```HESPI```_** 

----
### What is "hespi"?
- **_Hespi_** Stands for Herbarium specimen sheet pipeline. Hespi uses advanced computer vision techniques to extract data applicable for a range of research purposes. 

- Hespi combines multiple methods to automate specimen data extraction such as:
    1. **_Component detection:_** Deep-learning models detect various parts of specimen sheets. 
    2. **_Field Detection_** : identifies fields within primary specimen labels. 
    3. **_Text recognition_** : Uses 
        - OCR (Optical Character Recognition) for printed / typed text. 
        - HTR (Handwritten text recognition) for handwritten labels. 
        - Multimodal LLM's for parsing unstructured text and formatting data.






