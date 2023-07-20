## stash 변경사항을 커밋하기 보단 임시저장하고 싶어요

- git stash

  - 임시 수정 내용을 임시 저장하는 명령어이다.

  - git stash list

    - stash stack에 저장된 내용을 확인한다.

  - git stash pop [번호]

    - stash stack에서 빼서 적용한다.

  - git stash apply

    - stash stack에서 빼지 않고 적용한다.

  - git stash clear

  - git stash drop stash@{0}
