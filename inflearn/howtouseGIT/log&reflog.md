## [log & reflog] 이전 commit 내역들과 변경사항을 확인하고 싶어요.

- TIP

  - HEAD는 커밋 내역에서 현재 커밋(보통 가장 최신 커밋)을 가리키는 simbolic link(pointer)입니다. 보통 명령어에 커밋ID 대신 HEAD pointer를 많이 활용한다.

  - HEAD의 이전 커밋들을 확인하고 싶을 땐 HEAD^ 혹은 HEAD~ 으로 포인팅이 가능함.

  - 만약 HEAD로부터 3개 전의 commit에 접근하고 싶다면 HEAD^^^ 혹은 HEAD~3으로 표현가능.

- log

  - git log --help

    - 도움말

  - git log
    - 자세하게 나옴
  - git log --oneline

    - 간략하게 commitID와 commit message만 나옴

  - git log -n [숫자]

    - 최근 n개의 commit log만 보여줌

  - git log --oneline --decorate --graph

    - 커밋이 어떤 브랜치로부터 머지가 됬는지 확인가능

  - git show [HEAD^/~1]

    - 변경사항들 확인가능

  - git reflog

    - git reflog show HEAD를 축약한 것
    - HEAD의 이동경로를 확인가능
    - 모든 변경사항 reset과 같은 명령어들은 reflog에 기록됨

    - (HEAD -> {branch name})는 HEAD가 어떤 브랜치를 가리키고 있는지를 나타낸다.
    - HEAD@{n}은 가장 최근의 HEAD의 참조가 변경된 작업으로 부터 몇번쨰 전의 작업인지 알려줌
