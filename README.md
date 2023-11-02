# 쇼핑 웹 데이터를 활용한 웹 사이트 개발<br/>(Django를 활용한 데이터 스크래핑 웹앱 구현)
*※ 기존에 수행한 https://github.com/choiwanmin/web_scraper2 프로젝트를 정비 및 정리*

## 목차
* [프로젝트 소개](#프로젝트-소개)
* [기술 스택 & 개발 환경](#기술-스택--개발-환경)
* [구현 기능](#구현-기능)
* [배운 점 & 아쉬운 점](#배운-점--아쉬운-점)
## 프로젝트 소개
> ### 프로젝트 개요/동기
* 개발 기간 : 2022.12.08 ~ 2022.12.09 (2 일간)
* 개발 구성원 : BE/FE 2명 (같은 개발 내용을 각자 진행하며 모든 영역에 대하여 의논하여 진행)
* 프로젝트 목표 : 수업을 통해 배운 `Django`와 관련 기술의 복습 및 활용도 향상
* 개인 목표 : 백엔드 프로그래밍 활용 역량 강화를 목표
> ### 작업 내용
* 웹 스크래핑 기술 활용을 위한 주제(사이트) 선정
* 데이터 모델 정의
* `Django` 프로젝트 기본 환경 구성
* 쇼핑 데이터 웹 스크래핑을 위한 `scraper` 구현
* `URLConf`, `Template`, `Views` 정의
* `Bootstrap` 적용
> ### 웹 스크래핑 앱 구성도
![부트캠프_프로젝트1_앱_구성도_231031](https://github.com/choiwanmin/web_scraper2_review/assets/111493653/1c49752f-04a8-4efe-abf3-a0e051a5a099)
> ### 앱 데이터 모델
* 데이터 수집 사이트 : "https://www.10x10.co.kr/shoppingtoday/shoppingchance_saleitem.asp?sflag=sc&disp=&srm=be
* 데이터 수집 정보 : 이미지_url, 상품_url, 가격, 상품명, 할인율, 댓글개수, 좋아요개수

    |수집정보|데이터 속성|필요한 django 메서드|
    |--|:--:|--|
    |이미지_url(`image_link`)|텍스트|CharField(max_length=200)|
    |상품_url(`link`)|텍스트|CharField(max_length=200)|
    |가격(`price`)|숫자|IntegerField()|
    |상품명(`tile`)|텍스트|CharField(max_length=200)|
    |할인율(`dc_rate`)|숫자|IntegerField()|
    |댓글개수(`reply_cnt`)|숫자|IntegerField()|
    |좋아요개수(`like_cnt`)|숫자|IntegerField()|
> ### 클라이언트 화면 UI
*※ 2023/11/02 15:24 기준 웹 스크래핑 데이터*
|Home 화면|
|:--:|
|![부트캠프_프로젝트1_home_1](https://github.com/choiwanmin/web_scraper2_review/assets/111493653/33d39a3b-bd1f-489c-ac9e-f97c019f60f8)|
|**Dashboard 화면**|
|![부트캠프_프로젝트1_dashboard_1](https://github.com/choiwanmin/web_scraper2_review/assets/111493653/ef51131e-6535-4253-88d0-78c5a2b17874)|
## 기술 스택 & 개발 환경
> ### 기술 스택
|기술 스택|사용 버전|
|:---|:---|
|`python`|`3.8.10`|
|`django`|`4.1.3`|
|`requests`|`2.28.1`|
|`django_extensions`|`3.2.1`|
|`beautifulsoup4`|`4.11.1`|

<br/>

> ### 개발 환경

|개발 환경|사용 프로그램|
|:---|:---|
|CLI|`Cmder`|
|EDITOR|`Visual Studio Code`|
|OS|`Window`|
|SCM|`Git`|
|DBMS|`SQLite`|
## 구현 기능
* 텐텐사이트에서 할인특가 상품 중 일부 상품에 대한 간단한 정보 제공
* 대시보드를 통하여 웹 스크래핑 데이터 중 댓글개수 TOP10에 대한 그래프 제공
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