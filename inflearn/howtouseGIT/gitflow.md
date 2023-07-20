## 전략적으로 Git 사용하기 - gitflow

![gitflow](./pictures/gitflow.png)

- **TIP**

  - 대표적인 브랜치 전략으로 Gitflow 이외에도 Github flow, Gitlab flow 등이 있다.

  - branch의 naming convention은 gitflow에서 권장하는 방식이다.

    - default merge사용
    - master

      - 최종

    - develop

      - feature들이 merge되는 곳

    - feature

      - 기능들

    - release

      - 배포를 위한 브랜치
      - 배포를 위한 최종적인 테스트를 진행한다.
      - release하고나면 develop과 main에 sync를 맞춤.

    - hotfix

      - 배포 후 발생하는 버그들을 수정하는 브랜치
      - main과 develop에 sync를 맞춤.

    - 장점
      - 브랜치별로 명확하게 나눴기 때문에 브랜치별로 담당 팀을 명확하게 나눌 수 있다.

    - 단점
      - branch가 많아지고 commit 내역많아진다.
        - 명확한 life cycle를 가지는 것은 아니다.
            - aglie(life cycle가 고정되지 않고, 만들어지자 마자 바로바로 적용), waterfall(life cycle이 고정적인것)
## branch flow

1. main branch에서 develop branch를 만든다.
   - main과 develop branch는 항상 sync를 맞춘다.
     - hotfix, release branch를 만들고 나서는 main과 develop에 sync를 맞춘다.
2. 필요한 기능 사항들을 정의하고, 개발자들 별로 어떤 기능 개발을 담당할지 정한다.

3. 기능 사항 별로 각 개발자는 develop branch에서 feature branch를 만들어 작업한다.
   - 실제로 feature/create-user, feature/delete-user 등 한번에 개발할 단위로 브랜치를 만든다.
   - 한 사람이 여러 브랜치를 담당할 수 있다.
   - 반대로 한 브랜치를 담당할 수 있습니다.
4. feature branch에서 작업 완료 후 remote repository에서 push하여 팀원들에게 리뷰를 받는다.

5. 리뷰가 완료된 feature branch는 develop branch로 merge한다.

6. 정의했던 기능 사항들을 모두 개발하면 develop branch에서 release branch를 만든다.

7. 이 release branch위에서 통합 테스트를진행한다.

   - 보통 회사에서 QA팀이 있으면 QA팀이 이런 테스트를 한다.
   - 통합 테스트 중 발견된 버그는 release branch 위에서 수정하고 커밋한다.

8. 통합 테스트를 마치면 main branch와 develop branch를 머지한다.

9. 마지막으로 main branch의 최종 commit에 lag를 달아 project version을 명시한 후 배포한다. (1.1, 1.2)
   - git tag [tag-name]
   - version (tag) 기록하는 방식인 Semantic Versioning 등과 같은 패턴을 사용
     - https://semver.org/
10. 이후에 최종 배포된 project에 심각한 버그를 발견하면 main 브랜치에서 hotfix브랜치를 만들어서 버그 수정작업을 한다.

11. 버그 수정 작업 완료 후에는 main branch와 develop branch에 merge.

12. 버그 수정이 완료된 main branch의 project의 최종 커밋에 다시 tag를 달아 project version을 명시한다.


## reference
- gitflow 실습
    - https://www.youtube.com/watch?v=EzcF6RX8RrQ
 