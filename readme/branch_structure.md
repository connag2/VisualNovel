# 비주얼노벨 분기 구조 안내

이 패키지는 Chapter 1~4 기준으로 공통 루트, 캐릭터 루트, 파멸 분기, 트루 루트, 최종 선택 엔딩을
분리해서 관리하기 위한 기본 골격이다.

## 핵심 구조
- Chapter 1: 공통 우정 축적 / 관계 형성
- Chapter 2: 축제 시작 / 얇은 불안 20% / 분기 플래그 누적 시작
- Chapter 3: 본격 균열 / 파멸 분기 가속 / 루트 잠금 해제 조건 형성
- Chapter 4: 루트 확정 / 파멸 / 트루 진입 / 최종 선택

## 기본 원칙
- 최신 실제 스크립트를 기준으로만 이어 붙인다.
- 공통 챕터와 엔딩 챕터를 섞지 않는다.
- 한 파일 안에서 너무 많은 분기를 처리하지 않는다.
- 공통 상태값은 `system/route_flags.rpy`에서 관리한다.
- 엔딩 판정은 `system/route_checks.rpy`에서 모아 처리한다.
- 캐릭터 개별 서사는 `routes/`와 `endings/`에서 분리한다.
- 배드 엔딩은 `bad/` 폴더에서 계층적으로 나눈다.

## 추천 흐름
1. `script.rpy`에서 chapter 1 진행
2. `chapter2_main.rpy`에서 chapter 2 진행
3. `chapter3_main.rpy`에서 chapter 3 진행
4. `chapter4_main.rpy`에서 chapter 4 진행
5. 조건에 따라 `bad/*`, `true/true_route.rpy`, `endings/*`로 이동

## 주의
- 내용/대사/흐름을 바꾸지 않는 수정 작업과,
  신규 분기 구조 설계를 같은 파일에서 동시에 하지 않는다.
- Save 호환이 민감하면 기존 chapter 본편 뒤에 jump만 추가하는 쪽이 안전하다.
