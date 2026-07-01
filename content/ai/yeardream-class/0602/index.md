---
title: "0602 수업 정리"
date: 2026-06-02
description: "이어드림 스쿨 0602 수업 내용을 정리한 글입니다."
categories: ["수업 내용 정리"]
tags: ["이어드림", "수업정리"]
draft: false
---

# 0602 수업 정리

MY구글드라이브 : https://drive.google.com/drive/u/0/folders/1iEo6RXGKwC1nWZL5XYSHGAPKYOuMjbua

---

강의주제: 2주차-01-파이썬중급문법-2

날짜: 2026년 6월 2일

구글드라이브: https://drive.google.com/drive/folders/1GBSrhypSx_qwdLV6yLlsj5IsoszYMZyr?usp=sharing

상태: 완료

전화번호: 01072072163

게시-URL: https://torch-law-f0b.notion.site/260602-370d0b4d457380009458f2026e40daa6?source=copy_link

# UV 관련 명령어

```jsx
uv cache clean
uv sync
uv run python check_env.py
uv run jupyter lab
```

# Git 관련 명령어

- git push 할 때 쓰는 명령어

```jsx
git clone https:...
git add .
git commit -m "update"
git push
```

- git 로그인 할 때 쓰는 명령어

```jsx
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

# Python 수업

- 3교시

```jsx
import random

class TeamMember:
    """
    IT 회사 팀원을 표현하는 클래스
    
    속성:
        name (str): 팀원 이름
        role (str): 직책 (예: 시니어 개발자, 주니어 기획자 등)
        salary (int): 연봉 (만원 단위)
    """
    
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary
        self.projects = []  # 현재 참여 중인 프로젝트 목록

    # 행동 정의
    def introduce(self):
        """자기소개 메서드"""
        print(f"안녕하세요! 저는 {self.role} {self.name}입니다.")

    def join_project(self, project_name):
        """프로젝트 참여 하는 행동"""
        self.projects.append(project_name)
        print(f"🏃‍♂️ [{self.name}]님이 '{project_name}' 프로젝트에 새롭게 투입되었습니다!")

    def negotiate_salary(self, desired_salary):
        """연봉 협상 행동"""
        print(f"💼 [{self.name}]님이 연봉 협상을 시도합니다... (희망 연봉: {desired_salary}만원)")
        
        # 간단한 재미를 위해 70% 확률로 협상 성공, 30% 확률로 동결하는 로직을 넣어봤어요!
        if random.random() > 0.3:
            self.salary = desired_salary
            print(f"  -> 🎉 협상 성공! 연봉이 {self.salary}만원으로 인상되었습니다.")
        else:
            print(f"  -> 🥲 협상 결렬... 올해 연봉은 {self.salary}만원으로 동결입니다.")

    def say_goodbye(self):
        """작별인사 행동 (퇴사)"""
        print(f"👋 [{self.name}] : '안녕히 계세요 여러분! 전 이 세상의 모든 굴레와 속박을 벗어 던지고 제 행복을 찾아 떠납니다!'")
        self.projects.clear() # 퇴사하니까 진행 중인 프로젝트도 모두 비워줍니다.

    def make_toast(self):
        """술자리 건배사 행동"""
        print(f"🍻 [{self.name}]님이 잔을 번쩍 듭니다!")
        print(f"   '우리 팀의 무궁한 발전과 성공적인 프로젝트 마무리를... 위하여!!!'")
```

```jsx
# 1. 새로운 팀원 입사
dev_lee = TeamMember("이코딩", "주니어 개발자", 4000)
dev_lee.introduce()

# 2. 프로젝트 참여
dev_lee.join_project("사내 메신저 앱 개발")

# 3. 회식 자리에서 건배사
dev_lee.make_toast()

# 4. 1년 뒤, 연봉 협상
dev_lee.negotiate_salary(5000)

# 5. 퇴사 및 작별인사
dev_lee.say_goodbye()
```

# 4교시

```jsx
class TeamMember:
    # - 클래스 변수: 모든 팀원이 같은 값을 공유 - 
    company_name = "앨리스"  # 회사 이름은 모두 동일
    total_members = 0         # 전체 팀원 수 카운터

    def __init__(self, name, role, salary):
        # - 인스턴스 변수 : 각 팀원마다 다른 값 - 
        self.name = name
        self.role = role
        self.salary = salary

        # 새로운 팀원이 생성될 때마다 클래스 변수 업데이트
        TeamMember.total_members += 1
        
    def introduce(self):
        # 클래스 변수는 self.company_name 또는 TeamMember.company_name 으로 접근
        print(f"[{self.company_name}] {self.role} {self.name} (연봉: {self.salary}만원)")

alice = TeamMember(name = "Alice", role = "시니어 개발자", salary=6000)
bob = TeamMember(name = "Bob", role = "주니어 기획자", salary=3800)
```

## 6. str, repr

```jsx
class TeamMember:
    company_name = "TechCorp"
    total_members = 0
    
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary
        TeamMember.total_members += 1

    # - 클래스 메서드 : cls = 클래스 자체를 받음
    @classmethod
    def get_total_members(cls):
        """현재까지 생성된 팀원 수 반환"""
        return cls.total_members

    @classmethod
    def from_string(cls, member_string):
        """
        '이름-직책-연봉' 형식의 문자열로 팀원을 생성하는 대체 생성자
        예) "Alice-시니어 개발자-6000"
        """
        name, role, salary = member_string.split("-")
        return cls(name, role, int(salary))   # cls() = TeamMember()

    def __str__(self):
        return f"{self.role} {self.name}"

    def __repr__(self):
        return f"TeamMember(name='{self.name}', role='{self.role}', salary={self.salary})"
```

# 8. 상속

```jsx
# ────────────────────────────────────────────
# 부모 클래스(Base Class): Department
# 모든 팀이 공통으로 가지는 속성과 행동
# ────────────────────────────────────────────
class Department:
    """
    IT 회사 부서(팀)를 표현하는 기본 클래스
    
    속성:
        team_name (str): 팀 이름
        members (list): 팀원 목록
        budget (int): 팀 예산 (만원)
    """
    
    def __init__(self, team_name, budget):
        self.team_name = team_name
        self.budget = budget
        self.members = []         # 팀원 목록 (TeamMember 인스턴스들)
    
    def add_member(self, member):
        """팀원을 팀에 추가"""
        self.members.append(member)
        print(f"[{self.team_name}] {member.name}님이 합류했습니다.")
    
    def remove_member(self, name):
        """이름으로 팀원을 제거"""
        for member in self.members:
            if member.name == name:
                self.members.remove(member)
                print(f"[{self.team_name}] {name}님이 퇴팀했습니다.")
                return
        print(f"'{name}'님을 찾을 수 없습니다.")
    
    def show_members(self):
        """팀 구성원 목록 출력"""
        print(f"\n=== {self.team_name} 구성원 ({len(self.members)}명) ===")
        if not self.members:
            print("  (팀원 없음)")
        for i, member in enumerate(self.members, 1):
            print(f"  {i}. {member.role}: {member.name} (연봉 {member.salary}만원)")
    
    def get_total_salary(self):
        """팀 전체 연봉 합계 반환"""
        return sum(m.salary for m in self.members)
    
    def team_meeting(self):
        """팀 회의 (자식 클래스에서 재정의 가능)"""
        print(f"[{self.team_name}] 정기 팀 회의를 시작합니다.")
    
    def __str__(self):
        return f"{self.team_name} (팀원 {len(self.members)}명, 예산 {self.budget}만원)"

# ────────────────────────────────────────────
# 자식 클래스 1: 개발팀
# ────────────────────────────────────────────
class DevTeam(Department):
    """
    개발팀 클래스 - Department를 상속
    
    추가 속성:
        tech_stack (list): 사용 기술 스택
    """
    
    def __init__(self, budget, tech_stack):
        # super().__init__()으로 부모 클래스의 __init__ 호출
        super().__init__("개발팀", budget)
        self.tech_stack = tech_stack     # 개발팀만 가지는 추가 속성
    
    def code_review(self):
        """개발팀 전용 메서드: 코드 리뷰 진행"""
        print(f"[{self.team_name}] 코드 리뷰를 시작합니다. 참여자: {', '.join(m.name for m in self.members)}")
    
    def show_tech_stack(self):
        """사용 기술 스택 출력"""
        print(f"[{self.team_name}] 기술 스택: {', '.join(self.tech_stack)}")
    
    # 부모 메서드 오버라이딩(Override): 개발팀만의 회의 방식
    def team_meeting(self):
        print(f"[{self.team_name}] 스프린트 계획 회의를 시작합니다. (기술 스택: {', '.join(self.tech_stack)})")

# ────────────────────────────────────────────
# 자식 클래스 2: 기획팀
# ────────────────────────────────────────────
class PlanningTeam(Department):
    """
    기획팀 클래스 - Department를 상속
    
    추가 속성:
        current_plan (str): 현재 기획 중인 서비스명
    """
    
    def __init__(self, budget):
        super().__init__("기획팀", budget)
        self.current_plan = None
    
    def start_planning(self, service_name):
        """새 서비스 기획 시작"""
        self.current_plan = service_name
        print(f"[{self.team_name}] '{service_name}' 서비스 기획을 시작합니다.")
    
    def team_meeting(self):
        plan_info = f"(현재 기획: {self.current_plan})" if self.current_plan else ""
        print(f"[{self.team_name}] 기획 검토 회의를 시작합니다. {plan_info}")

# ────────────────────────────────────────────
# 자식 클래스 3: 영업팀
# ────────────────────────────────────────────
class SalesTeam(Department):
    """
    영업팀 클래스 - Department를 상속
    
    추가 속성:
        monthly_target (int): 월 매출 목표 (만원)
        monthly_achievement (int): 월 매출 달성액 (만원)
    """
    
    def __init__(self, budget, monthly_target):
        super().__init__("영업팀", budget)
        self.monthly_target = monthly_target
        self.monthly_achievement = 0
    
    def close_deal(self, amount):
        """계약 성사 시 매출 기록"""
        self.monthly_achievement += amount
        rate = (self.monthly_achievement / self.monthly_target) * 100
        print(f"[{self.team_name}] 계약 성사! +{amount}만원 (이번 달 달성률: {rate:.1f}%)")
    
    def team_meeting(self):
        rate = (self.monthly_achievement / self.monthly_target) * 100
        print(f"[{self.team_name}] 영업 현황 회의 (목표: {self.monthly_target}만원, 달성: {self.monthly_achievement}만원, {rate:.1f}%)")

# ────────────────────────────────────────────
# 자식 클래스 4: 분석팀
# ────────────────────────────────────────────
class AnalyticsTeam(Department):
    """
    분석팀 클래스 - Department를 상속
    
    추가 속성:
        tools (list): 사용 분석 도구
        reports (list): 완료된 분석 보고서 목록
    """
    
    def __init__(self, budget, tools):
        super().__init__("분석팀", budget)
        self.tools = tools
        self.reports = []
    
    def publish_report(self, report_name):
        """분석 보고서 발행"""
        self.reports.append(report_name)
        print(f"[{self.team_name}] 보고서 발행: '{report_name}'")
    
    def team_meeting(self):
        print(f"[{self.team_name}] 데이터 리뷰 회의 (사용 도구: {', '.join(self.tools)}, 발행 보고서: {len(self.reports)}건)")

print("클래스 정의 완료!")
```

```jsx
# ── Step 1: 팀원(TeamMember) 인스턴스 생성 ──
print("=" * 50)
print("Step 1. 팀원 채용")
print("=" * 50)

# 개발팀 팀원
alice  = TeamMember("Alice",  "시니어 백엔드 개발자", 6500)
derek  = TeamMember("Derek",  "프론트엔드 개발자",   4800)
eve    = TeamMember("Eve",    "주니어 백엔드 개발자", 3600)

# 기획팀 팀원
bob    = TeamMember("Bob",    "시니어 기획자",       5200)
fiona  = TeamMember("Fiona",  "UX 디자이너",         4300)

# 영업팀 팀원
carol  = TeamMember("Carol",  "영업 팀장",           5800)
george = TeamMember("George", "영업 담당자",          3900)

# 분석팀 팀원
helen  = TeamMember("Helen",  "데이터 사이언티스트", 5500)
ivan   = TeamMember("Ivan",   "데이터 분석가",        4200)
```

```jsx
# ── Step 2: 팀(Department) 인스턴스 생성 ──
print("=" * 50)
print("Step 2. 팀(부서) 구성")
print("=" * 50)

dev_team       = DevTeam(budget=50000, tech_stack=["Python", "React", "PostgreSQL", "Docker"])
planning_team  = PlanningTeam(budget=20000)
sales_team     = SalesTeam(budget=30000, monthly_target=100000)
analytics_team = AnalyticsTeam(budget=25000, tools=["Python", "Tableau", "BigQuery"])

```

---------------------------------
# 0602 수업 정리

- [☀️ 오전 수업 내용 정리 - 보기 / 다운로드](files/260602_오전수업.pdf)
- [🌙 오후 수업 내용 정리 - 보기 / 다운로드](files/260602_오후수업.pdf)

## 수업 내용 필기 첨부 파일

- [0602필기 다운로드(아직 없음)](files/0602_필기.txt)