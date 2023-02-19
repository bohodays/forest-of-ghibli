# 지브리의 숲

<br>

## 0. 프로젝트 개요

- 프로젝트명 : 지브리의 숲 (forest of ghibli)
- 프로젝트 컨셉 : 지브리 영화 커뮤니티 웹사이트
- 개발 기간 : 22.11.08(화) ~ 22.11.25 (금)
- 사용 기술스택 : Django, HTML, CSS, JavaScript

- 개발 일지 (노션링크) : https://cactus-silkworm-e8c.notion.site/1770dbf90db745099305cfb6c4db645e

- 팀원 정보 :

<table>
  <tr>
    <td align="center"><a href="https://github.com/bohodays"><img src="https://avatars.githubusercontent.com/u/109454527?v=4?s=100" width="100px;" alt=""/><br /><sub><b>박중원 bohodays<br /></a>Front & Back</b></sub><br /></td>    
    <td align="center"><a href="https://github.com/Dohyun-Kimm"><img src="https://avatars.githubusercontent.com/u/109256734?v=4?s=100" width="100px;" alt=""/><br /><sub><b>김도현 Dohyun-Kimm<br /></a>Front & Back</b></sub><br /></td>        
  </tr>
</table><br/>

<br>

<br>



## 1. 목표 서비스 구현 및 실제 구현 정도

| <center>목표</center>                                        | <center>실제 구현</center>                                   |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| <center>Account</center>                                     | <center>100%</center>                                        |
| 1. 유저 회원가입 기능<br />2. 유저 로그인 기능<br />3. 유저 로그아웃 기능<br />4. 유저 비밀번호 변경 기능<br />5. 유저 프로필 수정 기능<br />6. 유저의 내 정보 보기 기능<br />7. 회원탈퇴 기능<br />8. 북마크 기능 | 1. 유저 회원가입 기능<br />2. 유저 로그인 기능<br />3. 유저 로그아웃 기능<br />4. 유저 비밀번호 변경 기능<br />5. 유저 프로필 수정 기능<br />6. 유저의 내 정보 보기 기능<br />7. 회원탈퇴 기능<br />8. 북마크 기능 |
| <center>Movie</center>                                       | <center>92%</center>                                         |
| 1. FILMS 페이지<br />2. 영화 상세 페이지<br />3. DIRECTORS 페이지<br />4. 영화 감독 상세 페이지<br />5. GBTI 페이지(설문-결과)<br />6. QUIZ 페이지(풀이-결과)<br />7. 지브리 영화 검색 기능<br />8. 지브리 영화 캐릭터 인기투표 페이지<br />9. 영화 리뷰 생성 기능<br />10. 영화 리뷰 삭제 기능<br />11. 영화 리뷰 수정 기능<br />12. 영화 리뷰 좋아요 기능<br />13. 영화 리뷰 삭제 기능 | 1. FILMS 페이지<br />2. 영화 상세 페이지<br />3. DIRECTORS 페이지<br />4. 영화 감독 상세 페이지<br />5. GBTI 페이지(설문-결과)<br />6. QUIZ 페이지(풀이-결과)<br />7. 지브리 영화 검색 기능<br />8. 영화 리뷰 생성 기능<br />9. 영화 리뷰 삭제 기능<br />10. 영화 리뷰 수정 기능<br />11. 영화 리뷰 좋아요 기능<br />12. 영화 리뷰 삭제 기능 |
| <center>responsive web</center>                              | <center>80%</center>                                         |
| 1. 반응형 웹사이트 구현                                      | 1. 부분적으로 반응형 웹사이트 구현                           |



<br>

<br>



## 2.  데이터베이스 모델링 (ERD)

![img](https://cactus-silkworm-e8c.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fad809454-4855-4a72-b875-6d9b2441eeae%2FUntitled.png?table=block&id=9c95f5d3-ba55-4303-a286-d38b5a9dd046&spaceId=dd881eeb-b329-4edc-bb7c-14a91e45e834&width=2000&userId=&cache=v2)



<br>

<br>



## 3. Wireframe & Design

`피그마`

https://www.figma.com/file/vXuBc6w0viB4nAlZr0jyGU/%EC%A7%80%EB%B8%8C%EB%A6%AC%EC%9D%98-%EC%88%B2?node-id=0%3A1&t=3xdfvMdmsV6lsOCu-0

![화면 캡처 2023-02-19 235209](https://user-images.githubusercontent.com/109454527/219955815-1d425eb0-f800-423c-93c8-7876981e6470.jpg)



<br>

<br>



## 4. 서비스 기능에 대한 설명

#### 1) 인트로 페이지

![ezgif com-gif-maker (25)](https://user-images.githubusercontent.com/109454527/204095305-58755e4c-b041-4dcc-b6ee-12d18ac155cb.gif)

- 인트로 페이지에서는 웹사이트의 이름과 함께 컨셉에 대해 간단히 소개했습니다.
- 화면을 클릭하거나 아무키를 입력하게 되면 메인 페이지로 이동하게 됩니다.

<br>

#### 2) Account 페이지
![ezgif com-gif-maker (26)](https://user-images.githubusercontent.com/109454527/204095692-bf2f9eae-cba9-49ce-a9cd-28c98d44d946.gif)

- 회원가입시 기존에 있는 닉네임이나 아이디 입력, 빈칸으로 회원가입을 시도하면 경고 메시지로 알려주었습니다.
- 로그인, 프로필 수정, 비밀번호 변경 기능을 구현하였으며, 회원가입 탈퇴는 Modal을 통해 유저가 재확인할 수 있도록 알려주었습니다.

<br>

#### 3) FILMS 페이지
![ezgif com-gif-maker (27)](https://user-images.githubusercontent.com/109454527/204096072-bd201d0e-7f51-4f20-917b-bad8f0a45dee.gif)

- FILMS 페이지는 지브리 영화를 시간순서대로 나열하였고, 최신순 버튼을 통해 최신순으로 정렬할 수 있도록 만들었습니다.
- 영화 상세 페이지에서는 영화에 대한 상세한 정보를 확인할 수 있으며, 유튜브 api를 통해 예고편을 연결하였고, 북마크 기능을 구현했습니다.

<br>

#### 4) 리뷰 기능
![ezgif com-gif-maker (28)](https://user-images.githubusercontent.com/109454527/204096238-89a8d086-7fe4-4315-8822-60cb807f8dba.gif)

- 영화에 대한 리뷰 생성은 비동기 방식으로 구현했으며, 리뷰에 대한 좋아요 기능도 비동기 방식으로 구현했습니다.
- 리뷰는 500자 제한이 있으며 우측하단에 유저가 현재 쓴 글자수를 보여주었고, 유저가 등록한 리뷰가 100자 이상이 되면 자동으로 요약화되며 요약화된 글을 클릭하면 전문화가 됩니다.
- 리뷰에 대한 삭제 기능도 비동기 방식으로 구현했습니다.

<br>

#### 5) DIRECTORS 페이지
![ezgif com-gif-maker (29)](https://user-images.githubusercontent.com/109454527/204120061-4eb04243-568c-44b5-b3b0-cd177eb9b3fc.gif)

- 지브리 영화 감독들을 소개하는 페이지입니다. 감독의 상세 페이지에서는 감독의 명언이나 감독이 연출한 영화의 명대사를 보여주었고, 하단에는 연출한 영화들을 나열했습니다.

<br>

#### 6) 검색 기능
![ezgif com-gif-maker (30)](https://user-images.githubusercontent.com/109454527/204120330-5a735a5a-d913-485f-a9b6-c829f67ea35c.gif)

- Navbar의 검색 기능을 통해 지브리 영화를 검색할 수 있습니다. 유저가 2글자 이상 일치하는 지브리 영화를 검색하면 하단에 추천 검색어가 나오고, 그 상태에서 'Enter'를 누르거나 추천 검색어를 누르면 그 영화의 상세 페이지로 이동합니다.
- 지브리 영화가 아닌 영화를 검색하면 Modal을 통해 알려주었고, FILMS 페이지로 이동하는 버튼을 만들어서 유저가 검색하고 싶은 영화를 살펴볼 수 있도록 만들었습니다.

<br>

#### 7) GBTI 페이지
![ezgif com-gif-maker (31)](https://user-images.githubusercontent.com/109454527/204120505-ad21629d-341d-4db4-a660-6059ade2c2a3.gif)

- GBTI는 Ghibli와 MBTI의 합성어로 간단한 설문을 통해 유저의 MBTI를 구하고, 해당 MBTI에 대한 간단한 설명과 유저의 MBTI와 일치하는 지브리 캐릭터를 소개합니다.
- 하단에는 해당 지브리 캐릭터가 출연하는 영화도 함께 소개해주었고, 클릭시 해당 영화의 상세 페이지로 이동합니다.

<br>

#### 8) QUIZ 페이지
![ezgif com-gif-maker (32)](https://user-images.githubusercontent.com/109454527/204120760-82ba5eab-3f98-474b-b769-ce17ffb9ee2d.gif)

- 지브리 영화와 관련된 8단계의 퀴즈 풀이 서비스입니다.
- 맞힌 문제 수에 따라 4단계(지브리 새싹, 지브리 매니아, 지브리 고수, 지브리 박사)로 등급을 구분하였습니다.

<br>

#### 9) 반응형 웹사이트
![ezgif com-gif-maker (24)](https://user-images.githubusercontent.com/109454527/204120823-e35a4dd3-7af6-4b22-962a-faf04daf29ab.gif)

- 부분적으로 반응형 웹사이트로 제작하여 휴대폰에서도 접속이 가능합니다.

<br>
<br>

## 5. 배포 서버 URL
https://forestofghibli.com/movies/intro/
- 2022.11.24 aws(Cloud9, Instance, EC2)를 통해 배포했습니다.
- 2022.11.27 배포 중단되었습니다.

<br>
<br>


## 6. 후기

#### 박중원
최종 프로젝트를 하며 아침마다 도현이 형과 회의하고, 업무를 분담하고, Git을 통해 서로의 코드를 merge하고 conflict을 해결하는 과정이
모두 처음이어서 새롭고 신기했습니다. 그리고 현업에서도 업무 형태가 비슷하지 않을까 라는 생각이 들었습니다.<br />
 프로젝트는 제 자신의 부족한 부분을 되돌아볼 수 있는 좋은 경험이었습니다. 코드를 작성하고 문제를 맞닥뜨리며 능력의 한계를 느끼게 되었고,
처음 계획했던 목표를 계속 수정하며 시간의 한계를 느꼈습니다. 그리고 제가 작성한 코드가 올바른 코드인지에 대한 의문도 많이 가지게 되었습니다.
이러한 부분들을 통해 어떤 부분을 집중해서 공부해야될지 알 수 있게 되었기 때문에 더욱 발전할 수 있는 발판이 된 것 같습니다. 프로젝트를 준비했던 시간이
정말 빠르게 지나간 것 같고, 특히 마지막 배포 단계에서 하루를 모두 투자해도 안돼서 큰 좌절을 했었지만 최종 제출 전날 배포를 성공적으로 진행해서 정말 기뻤습니다.

#### 김도현
 프로젝트를 진행하면서, 협업을 어떻게 하면 잘 할 수 있을지 고민을 많이 했습니다. 개발 초기 단계에서부터 프로젝트를 완성하기까지 중원이와 같은 페이지를 보고 있다는 느낌이 들면 이상적일 것이라고 생각했습니다. 중원이와 저 둘다 이런 생각을 했기 때문에 자연스럽게 매일 아침 구현을 시작하기전 아이디어 회의를 하는 시간을 가졌습니다. 혼자 생각하는 것보다 둘이 얘기 하는 과정에서 더 나은 방향이 나왔기 때문에 회의 하는 시간을 아깝게 여기지 않았습니다.<br />이런 팀 문화 덕분에 개인의 능력으로는 어려웠을 일을 해냈다고 생각합니다. 
 1학기 때 배운 내용을 소화하기엔 시간이 부족 했던것 같습니다. 그래도 프로젝트를 하면서 장고 프레임워크와 자바 스크립트를 공부할 수 있어서 의미 있는 시간이었습니다.
뷰를 배웠지만 익숙하지 않아서 적용하지 않았는데, 뷰를 쓸 줄 알았더라면 더 편하게 개발 했을 것 같다는 생각도 들었습니다. 장고를 배울 땐 몰랐던 프레임 워크의 장점을 알게 되었습니다.
일찍 프로젝트를 시작 한 덕분에 배포를 해볼 수 있었던 것은 이번 프로젝트의 가장 큰 수확 이었습니다. 아무것도 아는게 없어서 가이드라인만 따라가면서 해봤지만, static 파일들을 불러오지 못했습니다. 시도한지 이틀 째에 배포에 성공했을 때 진짜 프로젝트를 완성한 기분이 들어서 뿌듯 했습니다.


