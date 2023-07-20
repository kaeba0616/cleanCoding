## conflict 다루기 - 1,2

- Merge 과정에서 충돌이 났다면?

  - git merge [branch-name]
  - 충돌난 파일 열어보면 >>>>> or <<<<< or ====== 이 있다.

  - 위에 source , 아래는 target

  - 그것들을 없애고, 수정한 후에
  - git add .
  - git commit

    - fix 하고 되돌리고 싶을때

      - git reset --hard HEAD^

  - 충돌이 나는 경우

    - 같은 파일의 같은 라인을 수정할 때

  - merge conflict가 날때 되돌리고싶을때(수정전)

    - git merge --abort

- 하나의 브랜치를 함께 사용하다가 충돌이 나는 경우
  - git pull origin main --rebase
  - HEAD가 다른 두 개발자들이 함께 사용시에 해결법
