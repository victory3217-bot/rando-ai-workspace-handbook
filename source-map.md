# Source Map / 출처 관리

장마다 무엇을 근거로 썼는지 기록한다. 외부 리서치로 채우지 않고, 직접 읽어서 확인한 것만 적는다. 확인하지 못한 것은 "미확인"으로 남긴다.

## 장별 근거 (작성된 장만)

| 장 | 상태 | 핵심 근거 | 하네스 사례 |
|---|---|---|---|
| AW-CH01 | Draft (본문 초안, 검토 전) | 세 개념의 작업 정의: 핸드북 기획 문서(내부 자료, 공개 문헌 검토 전). 사례 인물·회사는 교육용 가상 설정 | 없음 |
| AW-CH02 | Draft (본문 초안, 검토 전) | 다섯 구성요소 분류는 저자의 교육용 설계. 공식 문서 인용 없음 | rando-promotion-harness |
| AW-CH03 | Draft (본문 초안, 검토 전) | 공식 출처 S1~S5(아래). 정보 등급 A/B/C는 저자의 교육용 설계이며 법적 분류가 아님 | rando-client-discovery-harness |

나머지 장(AW-CH04~CH14, AW-OP01~OP03)은 아직 쓰지 않았다. 장을 쓸 때 이 표에 행을 추가한다.

## 공식 출처 (AW-CH03에서 사용, 확인일 2026-10-26)

브라우저로 해당 페이지를 직접 열어 본문을 읽고 확인했다. 정책과 화면은 바뀔 수 있으므로 장을 사용하기 전에 다시 확인한다.

| 번호 | 출처 | URL | 문서에 표시된 날짜 | 이 책에서 쓴 내용 |
|---|---|---|---|---|
| S1 | OpenAI 도움말: How your data is used to improve model performance | https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance | "Updated: 6일 전"(상대 표기) | 개인용 학습 설정과 opt-out 방법, 피드백 예외, 임시 채팅, 업무용 기본값 |
| S2 | OpenAI 도움말: Data controls in ChatGPT | https://help.openai.com/en/articles/7730893-data-controls-in-chatgpt | "Updated: 13분 전"(상대 표기) | 개인 계정 기본값, 학습 설정과 삭제의 관계, 임시 채팅 30일, 관리형 워크스페이스 |
| S3 | Anthropic Privacy Center: Is my data used for model training? (consumer) | https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training | March 17, 2026 | 학습에 쓰이는 조건, 시크릿 대화, 피드백 5년 |
| S4 | Anthropic Privacy Center: How long do you store my data? (consumer) | https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data | July 2, 2026 | 삭제 후 30일, 허용 시 최대 5년, 위반 표시 시 최대 2년 |
| S5 | Anthropic Privacy Center: Is my data used for model training? (commercial) | https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training | August 19, 2026 | 업무용 상품의 기본값과 피드백 예외 |

**읽지 않은 것 (책에서 추정하지 않음):** Claude 개인용 `Model Improvement`의 기본값, ChatGPT Business·Enterprise·Edu와 Claude for Work의 대화 보관 기간과 관리자 설정, 요금제별·지역별 세부 차이, 두 회사의 정식 개인정보처리방침과 이용약관 본문.

**읽기 방법에 대한 메모:** S1·S2·S3·S4·S5 모두 브라우저로 본문을 직접 읽었다. 처음에 자동 요약 도구로 가져왔을 때 문서 표시 날짜가 하루씩 다르게 나왔으므로(S3 3월 16일 → 실제 3월 17일 등) 날짜는 브라우저에서 읽은 값을 쓴다.

## 하네스 사례 기록

사례는 아래 다섯 항목을 모두 적는다. 저장소 공개 여부는 `gh repo view`로 확인했다(확인일 2026-10-26).

| 사례가 쓰인 곳 | 저장소 | 공개 여부 | 파일 경로 | 확인한 내용 | 진행 상태 | 확인일 |
|---|---|---|---|---|---|---|
| AW-CH02 | rando-promotion-harness | PUBLIC | `README.md`, `core/PLAYBOOK.md`, `agents/promotion-agent.md`, `knowledge/personal-profile.md`, `skills/` | 공통 규칙을 `core/PLAYBOOK.md` 한 곳에 두고, 실행 절차(`agents/`)·채널별 가이드(`skills/`)·운영자 선호(`knowledge/`)를 나눔. `CLAUDE.md`와 `AGENTS.md`는 같은 규칙을 읽는 얇은 진입점. 옛 교육자료는 `legacy/`에 보존하고 실제 작업 흐름에서는 쓰지 않음. 최종 확인과 게시 결정은 사용자 몫 | 공개 저장소. 커밋 `3725763`(2026-09-06)이 원격 최신 커밋과 동일함을 `git ls-remote`로 확인. 로컬 사본에는 원격에 없는 `output/` 폴더가 있었으나 근거로 쓰지 않음 | 2026-10-26 |
| AW-CH03 | rando-client-discovery-harness | PUBLIC | `docs/privacy.md`(0절), `HARNESS.md`(9절), `README.md` | 원본을 서버에 영구 저장하지 않는 것이 기본값(`EPHEMERAL`). 저장하지 않는 것과 전송하지 않는 것은 다르며 추출된 텍스트는 설정한 LLM 제공자에게 전송됨. 실제 고객 정보·개인정보·API 키·비공개 제안서를 공개 저장소에 올리지 않고 예제는 가상 정보만 쓴다는 규칙 | 공개 저장소, 버전 0.7.0-alpha.1(9단계 중 7단계), 마지막 push 2026-09-22 | 2026-10-26 |

## 사례로 쓸 수 있는 저장소 (공개 확인: 2026-10-26)

`pricing-harness`(로컬 폴더명 `pricing-harness-public`), `rando-promotion-harness`, `oda-project-reviewer`, `rando-client-discovery-harness`, `business-planning-handbook`, `pricing-handbook`.

## 사례로 쓸 수 없는 저장소

| 저장소 | 이유 |
|---|---|
| rando-client-discovery-app | 비공개(PRIVATE) |
| rando-client-discovery-training | 비공개(PRIVATE) |

이 두 이름은 장 본문에 나타나지 않아야 하며 `tools/content_audit.py`가 검사한다. 실제 고객자료와 미공개 교육자료도 사례로 쓰지 않는다.

## 공개 허용 목록이 낡았는지 확인하는 방법

저장소 공개 여부는 바뀔 수 있다. 사례를 새로 쓰거나 공개 배포 전에는 다음으로 다시 확인하고, `tools/content_audit.py`의 `PUBLIC_REPOS`와 이 문서의 확인일을 갱신한다.

```bash
gh repo view victory3217-bot/<저장소 이름> --json visibility
```
