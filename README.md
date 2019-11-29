# FINAL PROJECT



## 목차

0. 기본 사항
1. 구현 과정 
   1. Day 1
   2. Day 2
   3. Day 3
   4. Day 4
   5. Day 5
2. 데이터베이스 모델링 (ERD)
3. 핵심 기능
4. 배포 서버 URL 
5. 후기



## 00_기본 사항 

1. 개발 아키텍처

   C. Django REST API 서버(djangorestframework) + VueJS (Node, SFC)



2. 팀원 정보

   - 팀명: `haaagisooya`

   - 팀원: 3반 정병학, 홍수경



3. 업무 분담 

   * 정병학 

     * 데이터 수집 
     * Django Movie App 모델링 
     * Vue Login, Signup, Logout, Userlist, Userfollow
     * 추천 알고리즘 구현

   * 홍수경

     * 데이터 수집 
     * Django Accounts App 모델링 
     * Vue MoiveList, Movie genre Select, Movie Like
     * 웹 페이지 구성 및 디자인 (CSS, Bootstrap  등)

     

## 01_구현 과정

### 00. Trello 사용

![image-20191129090548053](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20191129090548053.png)

프로젝트 일정과 진행 사항을 관리하기 위해 Trello 사용 



### 01. Day 1 (2019.11.24)

1. 프로젝트 구상 및 기획 
2. 데이터 수집
   * 영화진흥위원회 API 를 통해 박스 오피스 순위를 바탕으로 중복 없이영화 제목, 영어 제목, 장르 등 데이터 수집
     * 장르별 영화 리스트를 제공하기 위해 최대 세가지의 장르 데이터 수집 
   * 영화진흥위원회 API 포스터 url, 영화 상세 설명, 관객 평점 을 제공하지 않아 Naver API 사용하여 데이터 수집 
     * 영화상세 설명: 검색 API 를 통해 제공하지 않기 때문에 link 를 통해 크롤링 
   * 영화 진흥위원회와 Naver 의 API 를 사용하여 3개의 CSV 파일로 데이터 수집 후 pandas 모듈을 이용하여 merge



### 02. Day 2 (2019.11.25)

1. CSV 파일을 json 파일로 변환 

2. Django 를 통해 Back-End 설정

   * Accounts App, Movie App 구성 
     * 데이터를 Vue.js 로 연결하기 위해 Serializer 설정 

3.  Vue.js 프로젝트 생성 

   

### 03. Day 3 (2019.11.26)

1. Vuex 를 활용하여 Signup, Login, Logout 구현 

   1. Signup

      - vuex에 userinput 인자를 생성하고, UsersignupForm 을 통해 userinput에 데이터를

        받고, axios 요청을 통해 userinput을 django로 넘겨 db에 저장한다.

        signup이후에 dispatch 함수를 통해 login 함수를 호출하여, 로그인 까지 바로 되게 구현

   2. Login

      - credential을 store에서 선언하고, username과 password를 넣어준다. axios 요청을 통해서

        credential을 넘겨주면, jwt토큰을 발급해준다.

   3.  Logout

      - session strage에서 jwt 토큰을 제거해줌으로써 로그아웃 구현

   

2. 모든 영화와 장르별 영화 보여주기 

   

### 04. Day 4 (2019.11.27)

1. MovieDetail 구현
   * 새로운 싱글 페이지로 연동하기 위해 router를 시도 
   * movie.id 를 props 와 emit 과정에서 문제가 지속적으로 발생
   * 이전의 프로젝트 중 실현한 Modal 을 통해 영화 상세정보를 제공 

2. 영화 좋아요 

3. user 팔로우 

   

### 05. Day 5 (2019.11.28)

1. 영화 추천 알고리즘 
2. Vue 기능 구현 및 CSS 수정 
3. 영화 리뷰 작성
4. 서버배포
   1. gitignore 관리 
   2.  Heroku 를 통해 백엔드인 Djago 서버 연결 
   3. Firebase 를 통해 프론트엔드인 Vue.js 서버 연결 후 배포
5. README 작성
   * ERD 시각화 
   * 발표자료 준비 





## 02_데이터베이스 모델링 (ERD)

![image-20191129090607066](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20191129090607066.png)

## 03_핵심 기능

1. 장르에 따른 영화 분류 

   * 드라마, 액션, 스릴러, 멜로, 애니메이션 등 11개 카테고리에 따른 지능형 영화 추천

   * 영화장르를 선택하게 되면 무비 전체리스트에서 장르 1, 장르 2, 장르 3을 돌면서 사용자가

     선택한 영화 장르와 같은 영화를 필터해서 사용자의 화면에 출력한다.

   



2. 영화 좋아요와 팔로우 기반으로 추천 알고리즘 

   - 사용자가 팔로우 한 사람이 좋아요한 영화를 바탕으로 영화 추천 알고리즘 구현

   - 사용자가 로그인을 하여, 추천 영화 버튼을 누르게 되면,  해당 사용자의 User 테이블에서

     그 사용자가 follow 한 사람의 리스트를 불러온다. 그 팔로우 리스트에 있는 사람들의 Movie 

     테이블을 순차대로 읽어  그 사람이 좋아요한 무비 목록을 새로운 테이블에 넣는다.

     팔로우한 모든 사람들의 영화를 중복없이 등록하고 화면에 출력한다.



3. user 팔로우 

   - 사용자가 여러 사용자의 리스트를 볼 수 있으며, 리뷰남긴 것을 보고 그 사용자를 팔로우

     할 수 있음



4. 영화 좋아요 
   - 해당 영화의 리뷰, 평점 뿐만 아니라 좋아요를 눌러 관심 영화 등록 가능



## 04_배포 서버 URL 

배포 서버 URL = `https://haaagisooya.firebaseapp.com/`



```bash
$ npm run build
$ firebase deploy --only hosting
```



## 05_후기

 이전의 프로젝트오 달리 웹 서버 배포를 위해 기획, 데이터 수집 등 모든 영역을 팀원과 함께 프로젝트를 진행하여 소프트웨어 개발를 아주 조금 간접적으로 경험할 수 있었습니다. 이번 프로젝트의 결과물은 부족한 부분이 많지만 Vue 를 통해 프런트엔드를 다뤄서 Vue 를 학습하며 어느정도 사용할 수 있게 된것으로 만족했습니다. 한가지 가장 크게 아쉬운 부분이 있다면 프론트엔드를 vue 를 통해 진행했기 때문에 컴포넌트를 프랍하는 과정의 문제인지 css 를 할 수록 계속 에러가 나서 디자인을 원하는 데로 진행하지 못한 부분이 아쉬웠습니다.

