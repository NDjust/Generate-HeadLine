# Headline Generator (KPMG)
[![license](https://img.shields.io/badge/License-AGPL-red)](https://github.com/NDjust/Generate-HeadLine/blob/master/LICENSE)
[![code](https://img.shields.io/badge/Code-Python3.7-blue)](https://docs.python.org/3/license.html)
[![member](https://img.shields.io/badge/Data-news-blueviolet)](https://news.chosun.com/ranking/list.html)

> Text-mining을 통해 Content에 대한 Headline을 추천해주는 프로젝트

## 📖 Introduction  
글을 작성하는 사람은 Headline을 만들 때, 다른 사람의 이목을 끄는 Headline을 선정하거나  
정보 전달이 명확한 Headline을 선정하는 등 글의 취지에 맞게 Headline을 선정하게 됩니다.  
  
'첫 문장은 제목이다'라는 말처럼 Headline을 잘 만드는 것이 중요해지고 있습니다.  
  
우리는 Headline을 작성하는 사람들의 부담을 덜어주고자 해당 프로젝트를 진행하게 되었습니다.  
  
## Participation Member
- 홍나단 : 010-6681-8139  
- 박성아 : 010-5619-9295  
- 박규훤 : 010-6473-4049  
- 한예찬 : 010-9042-1834  

## Role
- Data Engineering : 홍나단, 박규훤  
- Data Analysis : 박성아, 한예찬  
- Modeling : All  

## 📂 Directory structure (예시)
``` 
  |-Data           
  |  |-Data.zip                              #데이터 파일
  |  |-Data_Crawling.ipynb                   #데이터 크롤링 코드
  |  |-stopword.txt                          #한국어 불용어 사전
  |
  |-Data Preprocessing    
  |  |-NounExtraction.ipynb                  #명사를 추출하는 코드
  |  |-TextRank.ipynb                        #TextRank 코드     
  |
  |-Data Analysis   
  |  |-Similarity.ipynb                      #TextRank 알고리즘을 적용한 코드
  |
  |-README.md                                #이 문서
```

## 💻 System requirements







