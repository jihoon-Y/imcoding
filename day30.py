# 클라이언트, 서버 구조 이해하기

# '서비스가 동작하는 원리'와 '그걸 구현하는 방법' 2가지만 알고 있으면
# 코딩을 통해 실제 서비스가 만들어지는 과정에 대한 설계를 할 수 있음

# 코딩으로 만들어낸 멋진 서비스들, 이 안에서는 사실 코드가 여러 조각으로 나누어져 있고
# 여러 조각들이 아주 정교하게 맞물려 동작하고 있다

# 대부분의 서비스들이 대동소이 하기 때문에 나눠지는 원리를 한 번 알고 나면 앞으로 많은 도움이 될 것이다

# 1. 동작원리
# 클라이언트(주문하는 손님)쪽 코드, 서버(제공해주는 역할)쪽 코드 이렇게 나뉜다


# -(웹 개발에서의)클라이언트 : 크롬, 사파리
# 브라우저가 우리에게 웹사이트를 보여주기 위해서는 html, css, jabascript code가 필요하다
# html : 이미지, 글자, 버튼 등이 어디에 들어갈 지 정해주는 역할
# css : html에 크기, 색깔, 테두리 선의 굵기 등의 스타일을 입혀주는 역할
# js : 클릭하거나 스크롤하거나 등의 유저 동작에 따라 사이트가 어떻게 반응할지 정해주는 역할

# 이 코드들이 내 컴퓨터에 있으면 바로 사이트를 띄울 수 있을텐데 다 갖고 있을 수는 없다
# 코드들은 어디서 오는 걸까? > 클라이언트와 서버를 이해하면 알 수 있다

# 웹사이트를 보여주기 위한 코드는 서버에서 온다
# -서버 : 또다른 개념의 컴퓨터
# 유튜브=구글이 유튜브를 지원하기 위해 항상 켜 놓는 서버 컴퓨터가 있는 셈
# 우리가 유튜브를 보고 싶을 땐 이 서버에 유튜브 사이트를 보여주세요 요청하는 것이다

# 인터넷에 특정 주소를 검색하면, DNS라는 인터넷 주소록 같은 곳에서 찾아보게 된다
# DNS에서는 우리가 입력한 주소가 어떤 숫자들을 가리키고 있는데, 그것이 바로 IP주소이다
# IP주소란 서버 컴퓨터의 위치를 나타내는 것인데, 각 서버 컴퓨터의 위치를 외울 수는 없으므로 DNS를 통하는 것이다.

# IP주소를 알아냈으면, 이 주소에 해당하는 서버 컴퓨터한테 "유튜브 사이트 보여주세요!"라고 요청할 수 있고
# 그렇게 이 사이트를 띄우기 위한 HTML, CSS, JS CODE를 서버->클라이언트를 통해 받는 것이다

# 마지막으로 이걸 브라우저가 해석해서 유저에게 보여주는 것이다

# 사이트 이용 중에 로딩 아이콘이 뜨면서 추가로 정보가 주어지는 경우가 있는데
# 이건 HTML, CSS, JS CODE가 아닌, 새로운 포스트 열 개에 대한 데이터만 달라고 요청한 것이다
# 사이트를 처음 들어갈 때만 요청하는 게 아니라, 쓰는 도중에도 계속 추가로 요청할 수 있다

# 이런 방대한 데이터를 서버는 어떻게 보관할까?
# 서버에는 데이터베이스(DB)라는 저장소가 있다

# 새 포스트를 올리면 클라이언트가 서버에게 이 포스트를 저장해달라고 요청하고
# 서버는 그 요청을 듣고 데이터베이스에 새로운 포스트를 저장한다

# 유저 모두가 공유하는 서버 컴퓨터에 저장되니까 나중에 다른 사람들이 사이트에 들어와도 같은 걸 볼 수 있는 것이다
# (깃헙의 깃과 푸싱이 이거에 해당하는걸까?)

# 서버는 단순히 데이터를 주고 저장하는 곳만이 아니라, 서비스 운영에 있어 여러 가지 일을 추가로 수행한다
# 지문인식 등 개개인의 컴퓨터가 하기엔 버거운 명령들을 서버가 전달받고 완료해서 돌려주기도 한다
# 또 클라이언트 요청 없이 서버가 스스로 하는 일도 있는데, 대표적인 예가 정기구독에 대한 자동결제이다
# 서버에서 스케줄에 맞게 작업을 예약해 둔 것이다
# 그래서 서버가 다운됐거나 점검 중일 때는 서비스 이용이 불가한 것이다


# 2. 동작 원리 및 구현 방법
# 멋지고 화려한 기능도 세부적으로 나눠보면 작고 간단한 개념들로 이루어져 있다
# 개발자들이 실제로 하는 일이, 이런 작은 단위의 논리를 세우고 하나로 이어지도록 합치는 것이다

# 반복문 : 음악-반복재생, 앨범과 곡 나열
# 조건문 : 회원가입-아이디 중복인지 확인하고 아닌 경우에, 비밀번호가 맞는 조건을 충족하는 경우에 가입 진행

# 하지만 모든 부분을 작은 단위로 나누기에는 효율적이지 않다
# 그래서 사람들이 가져다 쓸 수 있도록 누군가 미리 만들어 둔 코드들이 있다
# 라이브러리, 프레임워크가 이에 해당한다 = 남이 미리 써준 코드
# 우리는 이걸 가져와서 내 서비스에 맞게 조금만 변형해서 쓰면 되는 것이다
# 누가 이미 만들어 둔 회원 가입 라이브러리를 가져다 쓰면 몇 가지 설정만 해줘도 사이트에 쉽게 도입할 수 있는 것이다
# 회원가입 외에도 서비스에 흔히 들어가는 기능(상품 검색, 장바구니, 결제, 전화번호 인증)들은 대부분 가져다 쓸 수
# 있는 코드나 툴이 이미 만들어져 있을 것이다


# 웹 개발 분야 이해하기

# 프론트엔드 : 클라이언트 개발자, 사용자에게 보여지는 화면을 그려주는 것이다
# 라이브러리 : React, Angular, Vue 등 있는데, 가장 많이 쓰이는 기술은 react이다
# 프론트엔드 개발자 로드맵 : HTML > CSS > JavaScript > React

# 백엔드 : 서버 개발자, 뒤에 숨어있어 사용자에게 안 보이는 부분을 만드는 것이다

# API(Application Programming Interface) : 두 프로그램이 서로 소통할 수 있게 해주는 것
# 백엔드 개발자가 API를 만들면, 그때 프론트엔드-백엔드 소통이 가능해진다
# JAVA, Python, Kotlin, PHP, Ruby 중에 골라 쓰면 되고, 각 언어에 따라 대표적인 라이브러리나 프레임워크가 있다
# 요즘은 원래 프론트엔드 언어였던 Javascript도 Node.js라는 기술을 통해 백엔드에서 사용할 수 있게 됐다

# 데이터베이스도 선택지가 있는데, 크게는 SQL과 NoSQL로 분류된다
# SQL은 사용 규칙이 조금 더 엄격하고 역사가 깊기 때문에 안정적으로 개발할 수 있다는 장점이 있다
# NoSQL은 비교적 최근에 생긴 방식이라 유연하고 간편하게 사용할 수 있다는 장점이 있다

# 모바일 개발 분야 이해하기

# 모바일도 클라이언트와 서버로 나뉘는데, 서버 개발은 백엔드와 거의 동일하다
# 모바일에서의 클라이언트는 스마트폰 화면이 된다는 차이점이 있지만 크게 다른 것은 아니다
# 모바일 앱을 다운 받으면 '유저에게 보여지는 부분'에 대한 코드가 핸드폰에 설치되고
# 필요한 부분들에 대해서는 앱이 서버에 요청하게 된다

# 웹 클라이언트는 HTML, CSS, JS를 사용하지만 모바일은 안드로이드용과 애플용 두가지로 만들어야 해서 조금 다르다
# 안드로이드 개발은 Kotlin이라는 언어로, 앱스토어 개발은 Swift라는 언어로 하게 된다
# 이런 한계를 극복하기 위해 '크로스 플랫폼'이라는 모바일 개발 솔루션들이 나오기 시작했다
# 크로스 플랫폼으로 대표적으로는 React Native가 있는데 프론트엔드 웹 개발 기술인 React를 발전시켜서 만든 것이다
# 페이스북에서 React Native를 만들어내자, 구글에서도 Flutter라는 기술을 냈다
# Flutter는 구글에서 만든 Dart라는 언어를 써서 개발한다

# Swift, Kotlin : 모바일에 가장 최적화된 앱을 만들고 싶을 때, 시간과 인력이 충분할 때 사용
# 크로스 플랫폼 : 서비스가 복잡하지 않고 높은 성능이 필요하지 않을 때, 개발 비용이 적게 들어야 할 때 사용
# React Native : 자바스크립트와 리액트 등 필요로 하는 기술이 많음, 언젠가 제대로 배울 계획이라면 채택
# Flutter : Dart언어만 사용할 줄 알아도 됨, 필요한 것만 배워서 빠르게 모바일 개발을 하고 싶다면 채택


# 그외 다양한 분야의 개발 이해하기

# 게임

# 컴퓨터 게임, 모바일 게임, 콘솔 게임 형태에 따라 개발 방식이 많이 다르다
# 가장 많이 쓰이는 기술로는 Unity와 Unreal 엔진이 있다
# Unity : C#
# Unreal : C++
# Unreal이 조금 더 결과물의 완성도를 높일 수 있지만 더 어려운 기술을 요구한다
# 그리고 엄청나게 큰 차이가 없기 때문에 비교적 접근성이 높은 Unity가 시장에서 더 많이 사용된다
# Unity를 쓰면 게임에 원하는 물체들을 드래그해서 넣을 수 있고
# 이 물체들이 어떤 식으로 동작할 지에 대해서는 C# 언어를 통해 코딩으로 구현하는 것이다

# 블록체인

# 비트코인, 이더리움, 솔라나 등등 탈중앙화된 형태의 시스템도 클라이언트 쪽은 기존과 동일하다
# 사실상 데이터가 관리되는 방식, 즉 백엔드가 탈중앙화된 형태일 뿐이다
# DApp(Decentralized App) : 블록체인 엔지니어는 블록체인 자체를 만드는 코어 엔지니어도 있겠지만
# 대체로 블록체인 위에 올라가는 APP을 만드는 엔지니어들이다
# 블록체인에 대한 이해가 필요하고, 어떤 블록체인이냐에 따라 개발에 사용되는 기술이 좀 다르다
# 현재 가장 큰 플레이어는 이더리움이라는 체인이고, 이더리움 DApp를 만들기 위해선 Solidity라는 언어를 알아야 한다

# 임베디드 시스템

# 코딩하면 컴퓨터, 스마트폰을 떠올리는데 사실 세탁기, 청소기 등 하드웨어에도 모두 코딩이 쓰였다
# 이렇게 하드웨어를 동작하게 하는 걸 임베디드 시스템(Embedded System)이라고 한다
# 이런 기계들에는 아무래도 조금 더 작고 성능이 안좋은 컴퓨터가 들어가기 때문에
# 세밀한 자원 관리가 가능한 C 같은 프로그래밍 언어들을 쓴다
# C는 Python이나 Java에 비해 코딩하기엔 까다로운데, 자원을 효율적으로 관리하는 데에는 뛰어나 쓰인다

# 사물인터넷

# 우리 일상에 있는 다양한 기계들이 서로 소통하면서 데이터를 공유하는 사물인터넷이라는 기술이 있다
# 이걸 사용하려면 결국 각 기계에 대한 코딩을 해야하기 때문에 여기서도 임베디드 시스템이 필요하다

# 시스템 프로그래밍

# 윈도우, 맥, 안드로이드, ios 같은 운영체제처럼 눈에 보이지 않는 내부 프로그램을 만드는 기술

# 언어 > Python, JavaScript
# 프레임워크 > Django, Node.js, Express.js
# 데이터 베이스 > SQL, mongoDB