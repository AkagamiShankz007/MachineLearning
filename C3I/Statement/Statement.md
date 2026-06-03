# MuseuSCAT challenge! 

## **_Task:_** 
- To develop a machine learning model that can read specimen labels from history collection , and then proceed to extract two key pieces of information ```The WHEN``` and  ```the WHERE``` about a given specimen. ```SCAT``` in the title essentially stands for ```Specimen Collected Automated Transcription.``` 

## **_References_** : 
Yonatan Geifman and Ran El-Yaniv. 2017. Selective classification for deep neural networks. In Proceedings of the 31st International Conference on Neural Information Processing Systems (NIPS'17). Curran Associates Inc., Red Hook, NY, USA, 4885–4894.



## **_Problem Statement in brief!_** : 
Natural museums , where one would find such specimens , each of the specimens , has a label attached with them , either a tiny slip or paper work or embeddings beside it by whomever collected it . 

These tables usually record important information like 
-  _28th August 1881 , near Madurai , Tamil Nadu , India , elevation(6 , 200ft)__
- _JUne 3rd , 1923 - Kovalam , Kerala , India._

These labels only provide very restricted information about a given specimen. They barely tell you how the given artifact was collected and nothing on or about it. They being handwritten , makes it even more imposssible to even find a accurate specimen description with millions of collectors scattered across the world with different typing formats , handwriting , and short forms.. etc 

## **_Problem Statement Proposed Solution_** : 
- A physical specimen with the appropriate label is first scanned 
- The scanned label is then fed into the machine learning model which then reads the text from the image. 
- The NLP extraction phase , where the date and locality are parsed from it. 
- Structured record , where the Date , GPS , notes etc about a specimen is verified. 
- collection DB , then added and queried into the database. 