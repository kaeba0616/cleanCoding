## amend commit & rebase 이전에 쌓인 커밋들을 변경하고 싶을 때

- amend commit

  - 현재 작업 중인 커밋(HEAD) 간단하게 수정할때
  - 메시지, 변경사항

    - git commit --amend

      - --amend : 현재 커밋(HEAD) 위에 변경사항을 덮어씌울 때 사용하는 옵셥, 커밋한 후에 추가적인 변경사항이 생겼거나 커밋 메시지를 변경하고 싶을 때 많이 사용

    - --no-edit : 커밋 메시지의 수정이 필요 없을 때

- rebase

  - 아래에 있는 커밋들 중 일부를 수정하거나 변경할 때

    - git rebase --interactive 를 사용

      - git rebase -i shortcut으로 많이 사용

      - pick : 별다른 변경 사항없이 그냥 커밋으로 두겠다.
      - edit : 해당 커밋 내용을 변경할 것이며 커밋 메시지도 변경 할 수 있게 하겠다.
      - reword : 해당 커밋의 메시지도 변경할 수 있게 하겠다.
      - drop : 해당 커밋을 제거하겠다.

      - i를 눌러서 수정가능

- TIP
  - git revert는 대상 커밋을 되돌리는 새로운 커밋을 만드는 기능이며, 커밋 자체를 변경하지는 못한다.
