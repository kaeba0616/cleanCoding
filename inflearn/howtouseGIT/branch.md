## branch

![branch](./pictures/git-branches-merge.png)

- 브랜치란
  - 사용자가 독립적으로 작업을 진행할 수 있도록 돕는 작업 흐름

## work flow using branch

1. 각 개발자는 main branch에서 각자 자신이 작업할 new branch를 만든다.
2. 각 개발자는 본인이 만든 branch 위에서 작업한다.
3. 깃 호스팅 서버(github 등)를 쓰지 않은 경우 아래 흐름 따른다.(pull request 및 code review가 없다.)

   - 작업 완료후 작업한 브랜치를 main branch에 merge한다.
   - local repository의 main branch가 업데이트 되었으므로, remote repository에도 push하여 최신 내역을 공유한다.

4. 깃 호스팅 서버를 쓰는 경우 아래의 흐름을 따른다.
   - 작업 완료후 remote repository의 자신이 작업한 브랜치를 push한다.
   - remoote repository에서 main branch로 pull request를 한다.
   - review 및 합의가 된 이후에는 main branch로 merge한다.

## branch 명령어

- check local branchs

  ```
  git branch
  ```

- switch
  ```
  git switch -c feature
  ```
- merge

  - main branch에 feature들을 머지 시킬때 main branch로 이동하여 아래 명령어를 실행한다.

  ```
  git merge feature
  ```

  - 보통 code review를 하기 때문에 바로 머지는 잘 안한다.
    - github에서 pull request(merge request) 생성하고 reviewers를 지정한다.
    - write box에 변경된 사항들을 정리해서 작성한다.

- 커밋의 변경사항들 초기화, 커밋 삭제 (정확하진 않음)
  ```
  git reset --hard HEAD^
  ```
