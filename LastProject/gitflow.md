```bach
A>>
touch .gitignore 

# gitignore.io 들어가서 등록하기 

git init 

# 함부로 commit 하면 안되고 브랜치는 머징하는 곳이다. 처음 init 할 때만 commit 하고 나머지는 머징한다. 

git add .
git commit -m 'init'
git remote add origin 주소 
git remote -v
git push origin master # -u 안하는게 나으다 

 
B>>
$ git clone https://github.com/eduyu/gitflow_practice.git

ls -a # 숨김 파일들까지 보여준다. 

A>>
git branch dev/startproject  # 브랜치를 만든다. 

git branch # 확인 

git checkout dev/startproject  # 스위칭이 일어난다. 그러면 여기서 작업을 하는 것

(작작작업업업이 끝나면 )

git add . # 마스터가 아닌 브랜티 만든 곳에서!! 

git status  # 심심할때 마다 보는 것이 좋으다. commit 은 초록색 파일만 일어난다. 

git commit -m '이름 '

git  checkout master  # 브랜치에서 했던 작업들이 날라가있다. | 그냥 확인할라고 

git checkout dev/startproject

git push origin dev/startproject

compare & 어쩌구 버튼 클릭 

git checkout master

# 홈페이지에서 작업한 후 

AB>> 
git pull origin master 

# 만들면서 스위치 하기 
$ git checkout -b dev/board




```







