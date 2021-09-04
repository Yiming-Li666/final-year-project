# Final-Year-Project
Doctors are overwhelmed by clerical work. A 2016 study estimates that doctors spend between 37% and 49% of their working hours on clerical tasks. All that paperwork contributes to the high level of burnout and depression in the profession, according to a 2019 study. The solution – voice assistant can serve as clinical stenographers that transcribe doctors’ observations and instructions and insert them into a patient’s electronic health record (EHR).

#### Task-specific project aims include [Research: 60%; Implementation: 40%]:
*  Develop a voice recognition by utilising deep learning to capture the doctors’ voice.  
* Build natural language task model that incorporate word embeddings, entity recognition and text classification for clinical text records.  
* Design a basic GUI application for demonstration purpose.  

## Requirements
* **SpeechRecognition**  
> pip3 install SpeechRecognition -i https://pypi.tuna.tsinghua.edu.cn/simple  
* **pyaudio**  
> brew install portaudio  
> pip3 install pyaudio  
* **noisereduce**
> pip3 install wavio  
> pip3 install wave  
> pip3 install noisereduce  
* **jieba nlp library**
> pip3 install jieba  
* **requests**
> pip3 install requests  
* **Pyqt5**
> pip3 install opencv-contrib-python-headless -i "https://pypi.doubanio.com/simple/"  
> pip3 install opencv-python-headless -i "https://pypi.doubanio.com/simple/"

## Relative Abbreviation
> **ADEs** - adverse drug events  
> **BPHSS** - Basic Public Health Service Specifications  
> **CCIS** - Critical Care Information System  
> **CDA** - Clinical Document Architecture  
> **EHR** - Electronic Health Records  
>> longitudinal health data on the population across care settings
>  
> **EMR** - Electronic Medical Records  
>> patient records for clinical purposes
>  
> **HIE** - Health Information Exchange  
> **HIMS** - Health Information Management System  
> **HIS** - Hospital Information System  
> **HIT** - Health Information Technology  
> **MDR** - Metadata Registries  
> **MEG** - Model of EHRs Grading  
> **MoH of China** - Ministry of Health of China  
> **NEHTA** - National E-Health Transition Authority, Australia  

## EHRs Security Standards in China
* ISO/TS 18308
> Structure necessities |&ensp; 34/50 &ensp;| (60.8%)  
> Process necessities &ensp;|&ensp; 22/24 &ensp;| (91.7%)  
> Others &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;|&ensp;  21/50 &ensp;| (42.0%)  
* ASTM E 1384
> Structure necessities |&ensp; 49/50 &ensp;| (98.0%)  
> Process necessities &ensp;|&ensp; 23/24 &ensp;| (95.8%)  
> Others &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;|&ensp;  39/40 &ensp;| (78.0%)  

## Data Standards
* NEHTA Clinical Data Standards  
* IT – Metadata Registries (MDR) – Part 3: Registry metamodel and basic attributes (ISO/IEC 11179-3:2003(E))  
* HL7 Clinical Document Architecture(CDA)  

## Construction of Personal Electronic Healthcare Records
* All medical institutions at any level must establish the medical record management system using a unique EMR identification (ID) number.  
* The medical record ID number should also be linked with the ID number of patients.  
* MoH instituted a Standards Bureau Office and series of standards in reference to architecture, regulations, and function profiles of EMRs.  
* Most of the health care s.ervice providers have set up its own EHRs system.  
* EHRs are connected to health insurance systems for settlement of claims with the special ID number for patients.  
* Resident Health Card connects the individual's EHR and EMR and provides a special connection for inter-institutional and trans-regional data sharing.  

## Benifits of EMRs System
1. improves patient care quality  
2. decreases medical errors  
3. controls and reduces medical expenditure   
4. saves in new EMR creation  
5. minimises full-time-equivalent employees  
6. saves adverse drug events(ADEs) and dose errors  
7. improves charge capture  
8. minimises billing errors  

## Use of Voice Technologies
1. documentation
2. commands
3. interactive response and navigation for patients

## NLP library
1. Spacy
2. CoreNLP
3. NLTK
> since version 3.2.3 has a new interface to Stanford CoreNLP using the StanfordCoreNLPServer. Among other places, see instructions on using the dependency parser and the code for this module, and if you poke around the documentation, you can find equivalent interfaces to other CoreNLP components; for example here is Stanford CoreNLP NER. Much of the work for this was done by Dmitrijs Milajevs.
4. stanfordcorenlp 
> by Lynten Guo. A Python wrapper to Stanford CoreNLP server, version 3.8.0. Also: PyPI page.
pycorenlp, A Python wrapper for Stanford CoreNLP by Smitha Milli that uses the new CoreNLP v3.6+ server. Available on PyPI.
5. corenlp-pywrap 
> by Sherin Thomas also uses the new CoreNLP v3.6+ server. Python 3.x (only). Also: PyPI page.
6. pynlp
> A (Pythonic) Python wrapper for Stanford CoreNLP by Sina. PyPI page.
7. stanfordnlp
8. jieba
> for chinese words split

## Reference
### NLP  
* [Compare Spacy, coreNLP and NLTK](https://blog.csdn.net/weixin_33278772/article/details/89135777)  
* [Use Stanford CoreNLP in Python](https://blog.csdn.net/qq_35203425/article/details/80451243)  
* [baidu NLP_Python_SDK](http://ai.baidu.com/ai-doc/NLP/tk6z52b9z)  
* [A collection of Chinese Word Segmentation Tools](https://blog.csdn.net/qq_33431368/article/details/92473779)
* [jieba - Chinese Word Segmentation Tools](https://github.com/fxsjy/jieba)

### Speach recognition  
* [Physician Dictation Audio Dataset](https://www.ezdi.com/open-datasets/)
* [Speech Recognition using baidu API](https://blog.csdn.net/weixin_40796925/article/details/98041155)  
* [Speech Recognition using google API](https://blog.csdn.net/dQCFKyQDXYm3F8rB0/article/details/79832700?utm_source=blogxgwz7)  
* [baidu Speech Recognition API instruction](https://ai.baidu.com/ai-doc/SPEECH/1k4o0bmc7)  

### EMR & EHR
* [EMR Information](https://baike.baidu.com/item/电子病历系统/8441290?fr=aladdin)
* [EHR Information](https://wenku.baidu.com/view/348d5a18a300a6c30c229fec.html)

### Noise reduce Reference
1. [Works, but get only noise](https://github.com/GedasFX/Audio-Noise-Reduction/blob/master/main.py)
2. [Formal documentation, but not working](https://pypi.org/project/noisereduce/)
3. [Online, like jupter. Seems to work, but it add a specific noise first and then remove it. There is a parameter 'noise_clip', he added this by himself, so that he can identify the noise_clip and directly remove it. Need VPN](https://colab.research.google.com/github/timsainb/noisereduce/blob/master/notebooks/1.0-test-noise-reduction.ipynb#scrollTo=GOxI8LTDBRNR)
4. [This is the same with 3, which has a better user experience](https://timsainburg.com/noise-reduction-python.html#:~:text=%20Noise%20reduction%20in%20python%20using%20¶%20,prototypical%20noise%20of%20the%20audio%20clip%20More%20)
5. [This one works, but get only noise. Need to include 'nextpow2', which cannot be install by pip. I added 'nextpow2.py' in ./google_voice_Demo](https://blog.csdn.net/iTaacy/article/details/60141849)
6. [Not working](https://blog.csdn.net/a1040193597/article/details/99598173?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param)

### Others
* [openpyxl - A Python library to read/write Excel 2010 xlsx/xlsm files](https://openpyxl.readthedocs.io/en/stable/)
* [Text similarity comparision - difflib & Levenshtein](https://blog.csdn.net/github_37443078/article/details/86552838)  
* [Text similarity comparision - fuzzywuzzy](https://blog.csdn.net/wumian0123/article/details/81435680)