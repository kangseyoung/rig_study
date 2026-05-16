# rig_study

Maya 리깅 자동화와 Python 스크립팅을 공부하며 정리한 저장소입니다. 공개된 코드에는 transform 계층을 기반으로 joint를 생성하거나, mesh 위치를 수집하고, Maya로 데이터를 전달하는 실험용 스크립트가 포함되어 있습니다.

## 주요 내용

- `rig_script_test/rig_test.py`: transform 계층을 순회하며 joint 생성과 skin bind 흐름을 실험한 스크립트
- `rig_script_test/get_joint_position.py`: joint 또는 오브젝트 위치 정보 수집 관련 스크립트
- `rig_script_test/mesh_finder.py`: mesh 탐색 및 매칭 실험
- `rig_script_test/send_to_maya.py`: Maya 환경으로 데이터를 전달하기 위한 테스트 코드
- `rig_script_test/깃헙분석.md`: 리깅 스크립트 분석 기록

## AI 활용 방식

이 프로젝트에서는 Maya 리깅 구조를 이해하고 Python 자동화 방향을 정리하는 과정에서 AI를 보조 도구로 활용했습니다. 직접 테스트할 리깅 흐름과 스크립트 목표를 정한 뒤, AI를 통해 계층 구조 처리 방식, 반복 코드 작성, 예외 상황 정리, 문서화 초안을 보완했습니다.

주로 다음 작업에 활용했습니다.

- transform, mesh, joint 계층을 어떤 순서로 탐색할지 아이디어 정리
- joint 생성, bounding box 기반 위치 계산, skin bind 흐름의 반복 코드 작성 보조
- Maya `cmds` 사용 중 발생할 수 있는 오류 로그 분석과 디버깅 방향 탐색
- 리깅 자동화 스크립트의 함수 분리와 리팩토링 방향 검토
- 테스트할 장면 구성과 검증 체크리스트 작성

최종 코드는 Maya 리깅 학습 목적과 실제 테스트 흐름에 맞게 직접 검토하고 수정했습니다.
