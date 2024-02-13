[![LinkedIn][linkedin-shield]][linkedin-url]
      
# Python-Words-In-Pyramid
    
The initial code will decode() text from a .txt file, and arrange the number-word pairs in numerical order in the shape of a right-triangle.
        
The next file will continue the process and return a string of the last words on each row.
    
### coding_qual_input.txt
This a sample text tile that is filled with an unorganized set of words. There are 300 words in total. Note that there are no line breaks, extra spaces, or empty lines in this text file. The code will not work if this file is not formatic to match this structure. 
     
#### Sample text from text file
     
```bash
195 land
91 sun
266 too
120 huge
3 dont
140 such
69 noun
227 student
```
    
    
### DisplayWordsInPyramid.py
     
This code does the following steps:
     
1. Imports text fie in read only
2. Each file is split into number and word.
a. Number is assigned Key, note this is by default since Number are in the Key position. 
b. Word is assigned Value, note this is by default since Word are in the Value position. 
3. Value for "i" set to 1. "i" represents the column position in the pyramid.
4. Value for "k" set to 2. "k"  represents the row position in the pyramid.
5. When "i" = "k", a line break is insert on the console to display the next value as a start to a new row. 
6. Then this displays the resulting pyramid on the console
    
#### Sample display
       
```bash
 down
 each dont
 experiment seat nine
 prove ready stead lot
 kind skill power third work
 with hole suit major fire silver
```
   
   
### DisplayLastWordInPyramid.py
     
This code does the following steps:
    
1. Imports text fie in read only
2. Each file is split into number and word.
a. Number is assigned Key, note this is by default since Number are in the Key position. 
b. Word is assigned Value, note this is by default since Word are in the Value position. 
3. Then this displays the values in order that "i" = "key". 

#### Sample display
  
```bash
 down dont nine lot work silver
```







[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/justin-bucsa