# 1. 현재 위치 확인 

## 현재 디렉터리 확인
- 현재 내가 어느 위치에 있는지 절대 경로로 출력

```bash
pwd
/c/Users/중진공57/Desktop/test
```

## 바탕화면으로 이동 
- `cd` 명령어로 원하는 디렉터리로 이동

```bash
$ cd ~/Desktop
```

## 현재 위치의 파일 폴더 목록 보기 
- 현재 디렉터리 안의 파일과 폴더를 나열

```bash
$ ls
```

- 숨김 파일 포함, 상세 정보까지 보기
```bash
$ ls -al
```

# 2. 폴더(디렉터리) 만들기 및 이동
## test 폴더 안에서 새로운 폴더 만들기
- `mkdir`로 새로운 폴더 생성
```bash
mkdir linux_practice
```

- 중첩 폴더를 한번에 만들기 (`-p` 옵션)
```bash 
mkdir -p linux_practice/src/utils
```

## 만든 폴더로 이동

```bash
cd linux_practice
```

## 상위 폴더로 이동하기
```bash
cd ..
```

---

# 3. 파일 만들기 및 내용 확인
## 빈 파일 만들기 (touch)
- `touch`로 빈 파일 생성
```bash
cd ~개인경로/linux_practice
touch hello.txt
```

- `>`는 덮어쓰기, `>>`는 내용 추가 
    + 가급적이면 `>`는 사용 금지
```bash
echo "Hello, Linux!" > hello.txt
echo "두 번째 줄 추가" >> hello.txt
```

## 파일 내용 확인 
- 파일 전체 내용을 터미널에 출력 
```bash
cat hello.txt
```

## vi 편집기 익히기
- 기본문법
- vi 편집기 : 개발자 필수 / 분석가 옵션 / 기획자, 공부하지 마세요!
    + 개발자의 경우 : 앞으로 markdown 작업할 때, vi 편집기로 하는 것 추천

| 키 | 동작 |
|---|---|
| `i` | 삽입 모드 진입 (현재 커서 앞) |
| `ESC` | 일반 모드로 복귀 |
| `:w` | 저장 |
| `:q` | 종료 |
| `:wq` | 저장 후 종료 |
| `:q!` | 저장 없이 강제 종료 |