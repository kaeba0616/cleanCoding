## squash & rebase merge 브랜치를 머지할 때 머지커밋을 남기기 싫을 때

![branch-merge](./pictures/branchMerge.png)

- default Merge

  - fast forward merge : HEAD위치만 바꿔준다.

    - 한쪽의 branch만 변경되었을 때
    - 별도의 커밋을 만들지 않고, HEAD위치만 바꿔준다.
    - 변경된 branch의 HEAD로 main HEAD를 옮긴다.

  - 두 branch 둘다 변경 되었을 때
    - 새로운 커밋을 만들어서 머지한다.
    - 합쳐지기 때문

- Squash Merge

  - 여러개의 commit들을 한번에 묶어서 머지한후 하나의 커밋으로 만듦!

  - git merge [branchName] --squash
  - git commit -m "commit message"

- Rebase Merge

  - 다른 머지들과 다르게 main에서 하지않고 feature branch에서 rebase를 시킨다.

    - git switch [branch-name]
    - git rebase main

    - 그리고 rebase한후에 fast-forward를 하기 위해서 main에서 feature로 merge시킨다.
      - git merge [branch-name]

- **TIP**

  - 개발 팀에서 브랜치 관리 전략에 따라 각기 다른 머지를 사용합니다. 따라서 상황에 맞는 최적의 머지 방식을 사용하면 된다.

  - 대표적인 Remote repository(github, bitbucket)들은 브랜치 간 병합을 하기 전 코드를 리뷰할 수 있는 PR(pull request) 환경을 제공합니다. 이때 squash, rebase merge 방식을 모두 지원함.
