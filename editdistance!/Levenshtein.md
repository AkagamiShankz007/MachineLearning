# Levenshtein's Distance! 
Levenshtein's distance or ***edit distance*** , is an algorithm that focuses on string conversion (from string a -> string b) using operations like edit, delete and converting. 


## <u>The Algorithm.</u>

Essentially it starts like your any other string matching algorithm , comparison , but the only catch here being you can modify a string B in order for it to exactly match a string A.. 

### <u>For Example!</u>

Assume u have two strings, 
1. String A - A B C D E F 
2. String B - A Z C E D

Visually we can see the difference between the two string , now in order to execute Levenshtein's Algorithm on them so that they begin to Match each other , we use the following operations as appropriately required. 

|   | NULL | A | B | C | D | E |F |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| A | 1 | 0 | 1 | 2 | 3 | 4 | 5 |
| Z | 2 | 1 | 1 | 2 | 3 | 4 | 5 |
| C | 3 | 2 | 2 | 1 | 2 | 3 | 4 |
| E | 4 | 3 | 3 | 2 | 2 | 2 | 3 |
| D | 5 | 4 | 4 | 3 | 2 | 3 | 3 |

Now , from the above table , we compare each of the letters A B C D E F to the string AZCED. 

So our step 1 would be comparing ```A``` from **AZCED** to each of **ABCDEF**

1. A -> ```A``` ===> Strings Match , hence 0 
2. A -> ```AB``` ===> Strings dont match , need to add 1 ```B``` , hence , 1 Operation(s)
3. A -> ```ABC``` ===> Strings dont match , need to add 2 ```BC``` , hence 2 operations...

The remaining steps would also take up linearly increasing operations as we are comparing only a single word ```A``` to characters in ```ABCDEF```

Now , lets take a bigger example. Say we are comparing ```AZCE``` with ```ABCDEF```

1. ```AZCE``` -> A ===> Strings dont match , need to edit ```ZCE``` hence it takes 3 Operations. 
2. ```AZCE``` -> AB ===> Strings dont match, need to edit ```ZCE``` . takes 3 again. 
3. ```AZCE``` -> ABC ===> Here , A and C is common for both strings , hence we only edit Z and E , 2 Operations. 
4. ```AZCE``` -> ABCD ===> Here . again AC common , need to edit BD for ZE which counts to 2 operations. 
5. ```AZCE``` -> ABCDE ===> AC common , need to edit BD to Z , thats totally 2 Operations (edit + delete)
6. ```AZCE``` -> ABCDEF ==> ACE common , need to do 3 operations , that would give you ```AZCE```


when i was small...i dint know how to download games...so i'd beg my dad...to get me game cd's....

each game cd costed like 99 and came with like 3-4 games... 

yesterday i was checking climber stand in amazon...and a game cd came into my recommended...it was 199 , anddd i can get it noww T-T

my mom wants foam and artificial plants now ...she'll stick the foam around the pillar and then insert artifical plants in them 