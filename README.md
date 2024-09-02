# 쇼핑 웹 데이터를 활용한 웹 사이트 개발<br/>(Django를 활용한 데이터 스크래핑 웹앱 구현)
*※ 기존에 수행한 https://github.com/choiwanmin/web_scraper2 프로젝트를 정비 및 정리*

## 목차
* [프로젝트 소개](#프로젝트-소개)
* [기술 스택](#기술-스택)
* [구현 기능](#구현-기능)
* [앱 데이터 모델](#앱-데이터-모델)
* [작업 내용](#작업-내용)
* [웹 스크래핑 앱 구성도](#웹-스크래핑-앱-구성도)
* [클라이언트 화면 UI](#클라이언트-화면-UI)
* [배운 점 & 아쉬운 점](#배운-점--아쉬운-점)
* [기타](#기타)

## 프로젝트 소개
> ### 프로젝트 개요
* 수업을 통해 학습한 python 기반의 Django를 활용한 웹 스크랩핑이 적용된 웹 사이트 구현을 목표로 해당 프로젝트를 수행
* 개발 기간 : 2022.12.08 ~ 2022.12.09 (2 일간)
* 개발 구성원 : 2명(BE/FE) (같은 개발 내용을 각자 진행하며 모든 영역에 대하여 의논하여 진행) 
> ### 프로젝트 목표
* 팀 목표 : 수업을 통해 배운 `Django`와 관련 기술의 복습 및 활용도 향상
* 개인 목표 : 백엔드 프로그래밍 활용 역량 강화를 목표

## 기술 스택
    |구분|사용 기술|
    |:---|:---|
    |Front-End|`HTML`, `Javascript`, `Bootstrap`|
    |Back-End|`python(3.8.10)`, `django(4.1.3)`, `beautifulsoup4(4.11.1)`|
    |DBMS|`SQLite`|
    |Server|`AWS EC2(Ubuntu)`|
    |IDE|`VS code`, `Vim`, `DBeaver`, `cmder`|
    |SCM|`Git & Github`|
    |Etc.|`Slack`|

## 구현 기능
* 텐텐사이트에서 할인특가 상품 중 일부 상품에 대한 간단한 정보 제공
* 대시보드를 통하여 웹 스크래핑 데이터 중 댓글개수 TOP10에 대한 그래프 제공

## 앱 데이터 모델
* 데이터 수집 사이트 : "https://www.10x10.co.kr/shoppingtoday/shoppingchance_saleitem.asp?sflag=sc&disp=&srm=be
* 데이터 수집 정보 : 이미지_url, 상품_url, 가격, 상품명, 할인율, 댓글개수, 좋아요개수

    |수집정보|데이터 속성|필요한 django 메서드|
    |--|:--:|--|
    |이미지_url(`image_link`)|텍스트|CharField(max_length=200)|
    |상품_url(`link`)|텍스트|CharField(max_length=200)|
    |가격(`price`)|숫자|IntegerField()|
    |상품명(`title`)|텍스트|CharField(max_length=200)|
    |할인율(`dc_rate`)|숫자|IntegerField()|
    |댓글개수(`reply_cnt`)|숫자|IntegerField()|
    |좋아요개수(`like_cnt`)|숫자|IntegerField()|

## 작업 내용
* 웹 스크래핑 기술 활용을 위한 주제(사이트) 선정
* 데이터 모델 정의
* `Django` 프로젝트 기본 환경 구성
* 쇼핑 데이터 웹 스크래핑을 위한 `scraper` 구현
* `URLConf`, `Template`, `Views` 정의
* `Bootstrap` 적용

## 웹 스크래핑 앱 구성도

    |![부트캠프_프로젝트1_앱_구성도_231031](https://github.com/choiwanmin/web_scraper2_review/assets/111493653/1c49752f-04a8-4efe-abf3-a0e051a5a099)|
    |:--:|

## 클라이언트 화면 UI
*※ 2023/11/02 기준 데이터 UI*
    |Home 화면|Dashboard 화면|
    |:--:|:--:|
    |![부트캠프_프로젝트1_home_1](https://github.com/choiwanmin/web_scraper2_review/assets/111493653/33d39a3b-bd1f-489c-ac9e-f97c019f60f8)|![부트캠프_프로젝트1_dashboard_1](https://github.com/choiwanmin/web_scraper2_review/assets/111493653/ef51131e-6535-4253-88d0-78c5a2b17874)|

## 배운 점 & 아쉬운 점
> ### 배운 점
* 수업을 통해 배운 `Django`를 활용한 웹앱 사이트 구현 및 복습
* `Django`를 활용한 일련의 개발 과정
> ### 아쉬운 점
* 데이터 모델 하나만 생성한 점
* 구현 기능을 더 추가하지 못한 점
* `Git`과 `Github`를 활용하지 못한 점
* 배포까지 진행하지 못한 점
* 제한된 기간에 완성도를 높이지 못한 점

## 기타
> ### 프로젝트 구조
```
    📦web_scraper2_pjt
     ┣ 📂venv_webscraper2pjt
     ┃ ┣ 📂Include
     ┃ ┣ 📂Lib
     ┃ ┃ ┗ 📂site-packages
     ┃ ┣ 📂Scripts
     ┣ 📂web_scraper2_review
     ┃ ┣ 📂.git
     ┃ ┣ 📂scripts
     ┃ ┃ ┗ 📜scraper_minipjt.py
     ┃ ┣ 📂static
     ┃ ┃ ┣ 📂image
     ┃ ┃ ┗ 📂js
     ┃ ┣ 📂templates
     ┃ ┃ ┣ 📜base.html
     ┃ ┃ ┣ 📜footer.html
     ┃ ┃ ┗ 📜navbar.html
     ┃ ┣ 📂tenten
     ┃ ┃ ┣ 📂migrations
     ┃ ┃ ┃ ┗ 📜__init__.py
     ┃ ┃ ┣ 📂templates
     ┃ ┃ ┃ ┣ 📜dashboard.html
     ┃ ┃ ┃ ┗ 📜index.html
     ┃ ┃ ┣ 📜admin.py
     ┃ ┃ ┣ 📜apps.py
     ┃ ┃ ┣ 📜forms.py
     ┃ ┃ ┣ 📜models.py
     ┃ ┃ ┣ 📜tests.py
     ┃ ┃ ┣ 📜views.py
     ┃ ┃ ┗ 📜__init__.py
     ┃ ┣ 📂web_scraper2
     ┃ ┃ ┣ 📜asgi.py
     ┃ ┃ ┣ 📜settings.py
     ┃ ┃ ┣ 📜urls.py
     ┃ ┃ ┣ 📜wsgi.py
     ┃ ┃ ┗ 📜__init__.py
     ┃ ┣ 📜.gitignore
     ┃ ┣ 📜db.sqlite3
     ┃ ┣ 📜manage.py
     ┃ ┣ 📜README.md
     ┃ ┗ 📜req.txt
```
