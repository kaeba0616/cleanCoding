## 작업 공간 정리

```
git add : workspace -> index
git commit : index -> local repository
git push : loal repository -> remote repository
git pull, fetch : remote repository -> local repository
```

- add

  ```
  git add a /git add . / git add -A
  ```

- commit
  ```
  git commit -m "~~text~~"
  ```
- push
  ```
  git push origin main
  ```
- check log

  - local repository에 기록된 커밋 로그들은 git log로 확인가능

  ```
  git log
  ```

  - git log를 하고 q를 이용해서 나올 수 있다.
    - I don't know how to say it like demon (linux), service(window).

- check status
  ```
  git status
  ```
- connect remote repository
  ```
  git remote add origin https://github.com/kaeba0616/cleanCoding.git
  git branch -M main
  git push -u origin main
  ```
