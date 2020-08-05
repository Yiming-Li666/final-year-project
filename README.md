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
> NEHTA Clinical Data Standards  
> IT – Metadata Registries (MDR) – Part 3: Registry metamodel and basic attributes (ISO/IEC 11179-3:2003(E))  
> HL7 Clinical Document Architecture(CDA)  

## Construction of Personal Electronic Healthcare Records
> All medical institutions at any level must establish the medical record management system using a unique EMR identification (ID) number.  
> The medical record ID number should also be linked with the ID number of patients.  
> MoH instituted a Standards Bureau Office and series of standards in reference to architecture, regulations, and function profiles of EMRs.  
> Most of the health care s.ervice providers have set up its own EHRs system.  
> EHRs are connected to health insurance systems for settlement of claims with the special ID number for patients.  
> Resident Health Card connects the individual's EHR and EMR and provides a special connection for inter-institutional and trans-regional data sharing.  

## Benifits of EMRs System
1. improves patient care quality  
2. decreases medical errors  
3. controls and reduces medical expenditure   
4. saves in new EMR creation  
5. minimises full-time-equivalent employees  
6. saves adverse drug events(ADEs) and dose errors  
7. improves charge capture  
8. minimises billing errors  

## Reference
* [Compare Spacy, coreNLP and NLTK](https://blog.csdn.net/weixin_33278772/article/details/89135777)  
* [Use Stanford CoreNLP in Python](https://blog.csdn.net/qq_35203425/article/details/80451243)  
* [Automatic Speech Recognition using baidu API](https://blog.csdn.net/weixin_40796925/article/details/98041155)
* [baidu NLP_Python_SDK](http://ai.baidu.com/ai-doc/NLP/tk6z52b9z)
* [baidu Speech Recognition API instruction](https://ai.baidu.com/ai-doc/SPEECH/1k4o0bmc7)