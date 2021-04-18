# placebook-server
초기 세팅 시 발생한 에러
- 버전에러 : 가상환경을 사용하지 않으므로, python3.8, pip3 명령어 사용권장(맥 기본 버전이 2.대기 때문)


DB생성
- SQLite 를 데이터베이스로 사용하지 않는 경우, USER, PASSWORD, HOST 같은 추가 설정이 반드시 필요합니다

순서
- 앱 생성
- 프로젝트 폴더 내 settings.py에 installed apps에 생성된 앱 추가

명령어
- (models.py 에서) 모델을 변경합니다.
- python manage.py makemigrations을 통해 이 변경사항에 대한 마이그레이션을 만드세요.
- python manage.py migrate 명령을 통해 변경사항을 데이터베이스에 적용하세요.

commit test