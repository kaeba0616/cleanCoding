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
