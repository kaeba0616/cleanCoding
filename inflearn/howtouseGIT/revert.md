## revert 이전 커밋의 변경사항을 되돌리고 싶을때

- 중간에 있는 커밋의 변경사항만 되돌릴 때

- git revert [커밋명]

  - hotfix의 경우

- **TIP**
  - 이전 커밋을 되돌려야 하는 상황일 때 rebase --interaction를 사용하여 커밋내역을 조작할 수 있다.
    - rebase 는 remote repository에 push를 할때 forece push를 해야되고, 안전하지 않을 수 있어서
  - revert를 선호한다.
