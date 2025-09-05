# PJT 03 - 반응형 Profile 페이지 구현

## PJT 003 개요
Bootstrap & CSS를 활용하여 프로필 페이지 구현
<br/>
- HTML
- CSS
- Bootstrap5
- Visual Studio Code

## 구현 과정 및 학습 내용

### 1. 기본 정보 수정 페이지 구현
- 프로필 사진, 자기소개, 투자 성향을 좌측 레이아웃에 배치
- Bootstrap Grid 시스템(.row, .col-md-*)을 활용하여 반응형 구조 구현
- 회원 번호, ID, Email, Nickname, 나이, 자산, 연봉을 출력하는 폼 구성
- 중첩 딕셔너리 처리
#### 새로 배운 점 
  - border-end 등 Bootstrap 유틸리티 클래스로 빠르게 레이아웃 구성 가능
  - row 내부에는 반드시 col-*를 사용해야 media query가 정상 작동한다는 점을 알게 됨
#### 어려웠던 부분
- readonly와 disabled의 차이
  - readonly: 사용자가 내용을 변경할 수는 없지만, 값을 볼 수 있고, 폼 전송 시 함께 전송
  - disabled: 사용자가 볼 수는 있지만 상호작용 불가. 포커스도 받을 수 없음. 또한 폼 전송 시 제외
### 2. 내비게이션 바 구현
- 화면 상단에 페이지 로고를 표시
- 기본 정보 수정 페이지와 포트폴리오 수정 페이지로 이동 가능한 네비게이션 바 구현
#### 어려웠던 부분
- 네비게이션 바 안에서 요소 배치
  - d-block, w-100를 이용하여 가로에 꽉 차게 설정 가능
### 3. 포트폴리오 수정 페이지 구현
- 금융 포트폴리오 정보 출력
  - 회원 번호, ID, 저축 성향, 최애 은행
#### 어려웠던 부분
- input 태그의 disabled 속성: 입력하지 못하도록 비활성화
- div 태그안의 d-flex, justify-content-between: 요소를 양쪽 끝으로 밀어냄
#### 새로 배운 점
- 라디오 타입의 버튼 구현
```html
<input type="radio" class="btn-check border" name="options" id="option1" autocomplete="off">
<label class="btn border-info" for="option1">도전형</label>
```  
### 4. 반응형 레이아웃 구성
- Bootstrap Breakpoints를 이용하여 화면 크기에 따른 반응형 레이아웃 구성
### 5. 생성형 AI 활용
- 금융 어플리케이션의 회원 정보 페이지를 구현할건데 input 태그에 어떤 속성을 추가해야 더 가시성이 좋을까?
  - 박스를 클릭하면 테두리 색이 변경
  - 그림자 속성 적용
- 좀 더 전문성 있는 느낌을 주려면 어떤 속성을 적용하는게 좋을까?
  - 박스에 테두리 라운딩 처리

## 프로젝트 후기 및 발전 방향

### 배운 점
1. Bootstrap Grid System 이해
   - Breakpoints를 이용한 반응형 레이아웃 구성
     - container, row, col-sm-12 등

2. margin, padding 특성 이해
   - 마진 상쇄

3. block, inline 타입이 중첩됐을 때 적용되는 특성 파악
   - <div></div>의 자식 <a></a>가 있다면 부모 요소의 블록 타입 특성을 기대해도 자식의 인라인 특성 때문에 해당 블록이 화면의 가로 너비 전체를 차지하지 않음


### 향후 발전 방향
1. 기초 설계를 튼튼히 하고 작업을 시작하자
   
2. 협업 시 충분한 의사 소통 필요