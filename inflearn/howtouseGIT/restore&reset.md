## restore & reset 변경사항, 커밋을 초기화하고싶다.

- git reset

  - 특정커밋 시점으로 돌아갈때, 해당 커밋 이후 만들어진 모든 작업들에 대한 처리방법에 따라 명령어가 다르다.

  - git reset --hard [commitID]

    - 해당 커밋 이후의 모든 작업들을 삭제하고 해당 커밋으로 돌아간다.

  - git reset --mixed [commitID]

    - Default값이라 git reset [commitID]라 해도 된다.

    - 해당 커밋 이후의 모든 작업들을 삭제하고 해당 커밋으로 돌아간다.

    - 삭제된 작업들은 workspace에 남아있다.
      - 변경사항들이 commit되지 않은 상태로 남아있음.

  - git reset --soft [commitID]

    - 변경사항을 삭제하고 해당커밋으로 돌아간다.

    - 삭제되는 작업들은 index(stage)에 남는다.

- git restore

  - 특정 파일의 변경사항을 제거하고 HEAD기준으로 되돌리고 싶을때 사용

    - workspace에 있는 변경 사항을 되돌릴때: git restore {파일경로}

    - modified상태인 파일의 변경사항을 HEAD의 상태로 변경한다.

    ```
    # 아직 stage(index)에 올라가지 않은 README.md 파일을 되돌릴 때
    git restore README.md
    ```

    - TIP

      - git restore는 git reset --hard HEAD와 비슷한 결과를 가져온다.

      - 다만 restore는 새파일의 변경사항을 되돌리지 않지만, reset은 새파일의 변경사항도 되돌린다.
        - modifed상태인 파일에서의 변경사항만 되돌린다.
