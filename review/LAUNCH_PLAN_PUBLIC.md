# 단일 공개 저장소 런칭 계획

작성 2026-10-26. 공개 정책: 교안, 실습자료, 워크북, 강사용 해설·정답, 워크숍 운영자료, 용어집, 사이트 코드, 공개해도 문제가 없는 저자 검토기록을 **하나의 저장소 `rando-ai-workspace-handbook`**로 공개한다. 이 문서는 점검 결과와 계획이며, 이번 단계에서 **GitHub 저장소 생성, push, Pages 배포, 홈페이지 수정은 하지 않았다.** 14개 장은 모두 `Draft`, `last_reviewed`는 비어 있다(저자 승인과 학습자 시험 없음).

## 1. 단일 공개 저장소 사용 가능 여부

**가능하다. 현재 Git 이력(커밋 2개)을 그대로 공개해도 중대한 위험은 발견되지 않았다.** 이력을 다시 쓰거나 별도 저장소를 만들 필요가 없다. 다만 아래 "저자 판단 사항(B)"을 정한 뒤 공개한다.

- 작업 트리와 전체 이력의 비밀·인증정보 검사: 발견 없음(gitleaks, 이력 패치 텍스트 직접 검색 포함).
- GitHub Pages는 Free 계정에서 공개 저장소로 쓸 수 있다(GitHub 문서, 2026-10-26 확인). 공개 저장소이므로 요금제와 무관하게 가능하다.
- 기존 핸드북 두 곳과 같은 방식(공개 저장소 + Pages 워크플로)이며 홈페이지 포털의 구조("각 핸드북은 자기 공개 저장소와 Pages가 원본")와 맞는다.

## 2. 점검 결과: 세 가지로 구분

### A. 반드시 제거해야 하는 민감정보 — **없음**

| 점검 | 결과 |
|---|---|
| 비밀번호·API 키·토큰·개인 키·`.env` | 작업 트리와 이력 모두 없음(패턴 검색: `password`, `api key`, `token`, `gho_`, `ghp_`, `sk-`, `BEGIN … KEY`, Vercel `prj_`/`team_` ID) |
| 개인정보·고객정보 | 없음. 모든 인물·회사는 가상. 연락처는 자리 표시용 `010-0000-0000`과 `example@example.com`뿐 |
| 로컬 PC 경로·계정 | 저장소 파일에 없음(이 점검 중 `review/LAUNCH_PLAN_L1.md`에 있던 로컬 경로는 문서를 대체하며 제거함) |
| 추적 파일 | 이력에 있는 파일은 31개의 문서·소스 파일뿐이며 이진 파일, 설정 비밀 파일 없음 |

### B. 저자가 공개 여부를 판단할 내부 작업정보

| # | 위치 | 내용 | 위험 | 해결안 |
|---|---|---|---|---|
| B1 | `source-map.md`, `tools/content_audit.py`(이력의 2개 커밋에도 있음) | 비공개 저장소 **2개의 이름**(`rando-client-discovery-app`, `rando-client-discovery-training`)과 "사례로 쓸 수 없음" 표기 | 비밀은 아니다. 이름만으로 접근할 수 없지만 비공개 저장소의 *존재*가 드러난다. 정책상 "이름이 비공개라는 이유만으로 숨기지는 않음" | **(권장) 그대로 공개**하거나, 감추려면 현재 파일에서 이름을 일반 표현("비공개 저장소")으로 바꾸고 이력의 2개 커밋은 그대로 둔다(이력에 남음) → 완전히 감추려면 이력 재작성 또는 새 저장소가 필요하므로 **이번에 하지 않고 저자 결정 사항으로 보고** |
| B2 | 커밋 메타데이터 | 작성자 `Kwangdong Min <victory3217@gmail.com>` | 같은 주소가 이미 공개된 다른 저장소(pricing-handbook 등)의 커밋에 있다. 새로운 노출 아님 | 그대로 공개(또는 앞으로 noreply 주소 사용) |
| B3 | `ko/chapters/CH01.md` 9절, `source-map.md`, `review/CH01.md` | "핸드북 기획 문서(내부 자료)"를 출처로 언급 | 독자가 확인할 수 없는 내부 문서를 가리킴. 민감하지 않음 | 그대로 공개(출처가 내부 문서라고 밝힌 것이 정직한 표기). 저자가 문구를 바꿀 수 있음 |
| B4 | `review/` 전체(저자 검토자료, 통합 검토·워크숍 계획) | 저자 의사결정 항목, 미검증 사항, "법무 검토 없었음" 같은 솔직한 한계 | 민감정보는 아님. 다만 *저자가 아직 검토하지 않은 작성자(AI) 의견*이 공개 저장소에 그대로 보임 | 공개해도 문제 없음. 정책상 공개 대상. 저자가 원하면 일부만 공개 |
| B5 | `review/LAUNCH_PLAN_PUBLIC.md`(이 문서) | 내부 운영 계획(공개 절차, 복구 절차) | 접근 경로를 유추하게 하는 정보는 넣지 않았다(저장소 이름·호스팅 방식·로컬 경로 생략) | 공개 가능. 불안하면 공개 후 삭제 |
| B6 | `CHANGELOG.md`, `README.md` | 개발 과정 기록("작성자(AI)", Phase 이름) | 민감하지 않음 | 공개 전 README만 공개용으로 다듬기(권장) |
| B7 | `workshop/instructor-guide.md` | 정답과 해설 | 정책상 공개. 학습자가 먼저 볼 수 있음 | 사이트에서 메뉴·검색에서 분리(4절). 저장소(GitHub)에서는 파일이 그대로 보임 → 완전히 숨길 수 없음을 인정 |
| B8 | `LICENSE` 없음 | 공개하면 법적으로 "모든 권리 보유"가 기본 | 재사용 허용 여부가 불명확 | (결정됨) 오픈소스 라이선스를 부여하지 않고 README에 저작권·이용 조건 안내(Phase L3) |
| B9 | 사이트 `noindex` | (결정됨) 일반 페이지의 noindex는 공개 시점에 제거, 강사용 안내서 두 페이지는 noindex 유지 | — | 반영 완료(Phase L3) |

### C. 문제없이 공개 가능한 교육자료

`ko/chapters/CH01~CH14.md`, `workshop/` 5개 파일(가상 자료, 정답·해설 포함), `glossary.md`, 장별 9절의 공식 출처와 확인일, 사이트 코드(`site/`), `content-manifest.json`, `assets/templates/`, `en/README.md`, `VERSION`. 가상 자료 안전성은 감사 도구의 개인정보 패턴 검사(장 본문)와 `workshop/`의 직접 검색(이메일·실제 전화번호·계좌·키 형태 없음)으로 확인했다. 외부 공식 문서는 요약·재서술이며 원문을 길게 옮기지 않았다.

## 3. 공개 전 반드시 해결할 위험

1. **B1~B9의 저자 결정**(특히 B1 비공개 저장소 이름, B8 라이선스, B9 noindex).
2. **저장소에서의 정답 노출은 막을 수 없다.** 정책상 공개이므로 GitHub 저장소의 `workshop/instructor-guide.md`는 누구나 열 수 있다. 사이트에서의 분리(4절)는 *실수로 먼저 보는 일*을 줄일 뿐이다. 또한 CH03·CH06·CH09·CH12 본문 6절에 저자 해설이 이미 들어 있다.
3. **`git add`는 마지막에 한 번, 목록을 확인하고 한다.** 현재 미추적 파일은 모두 공개 대상이지만, 공개 직전에 `git status`로 의도하지 않은 파일(임시 파일, 로컬 도구 폴더)이 없는지 확인한다(`.gitignore`에 `.claude/`, `.vscode/`는 추가함).
4. 공개 직전 gitleaks를 **다시** 실행한다(그 사이 수정이 있었다면).
5. 공개용 `README.md`를 정리한다(현재는 개발 메모 중심, 최소 수정 제안은 7절).

## 4. 교육자료 웹사이트 구성안 (이미 로컬에 구현, 커밋 전)

기존 Astro/Starlight를 유지하고 새 프레임워크·CMS를 도입하지 않았다. 동기화 스크립트가 `workshop/*.md`와 `glossary.md`를 한국어 페이지로 복사한다(본문은 바꾸지 않음).

| 메뉴(왼쪽 사이드바) | 내용 | 기본 상태 |
|---|---|---|
| Part 1~4 | CH01~CH14 (기존) | 펼침 |
| **실습자료(참가자용)** | 실습자료 안내, 참가자 워크북, 가상 회의자료, 가상 AI 결과물, 워크스페이스 양식 | 펼침 |
| **참고자료** | 용어집 | 펼침 |
| **강사용 안내서(정답·해설 포함)** | 열기 전 안내(문 역할의 페이지) → 강사용 안내서 | **접힘** |

**정답 노출을 줄이는 장치:** ① 강사용 자료는 별도 묶음이며 기본으로 접혀 있다. ② 실습자료 메뉴에는 정답이 없고 "정답은 강사용 안내서에 있다"고 안내한다. ③ 강사용 두 페이지는 **검색 색인에서 제외**(`pagefind: false`; 검색으로 "3,650" 같은 정답 값을 찾으면 CH09 본문만 나오고 강사용 안내서는 나오지 않음을 확인)하고 `noindex` 메타가 있다. ④ 강사용 페이지 상단에 "정답이 들어 있으니 실습을 마친 뒤에" 배너. ⑤ 시작 페이지에는 별도 소제목 "강사용(정답·해설 포함)"으로 링크를 분리했다.

**변경한 파일(로컬, 커밋 전):**
- `site/handbook.config.mjs`: `EXTRA_GROUPS`, `EXTRA_PAGES`(어떤 파일을 어느 메뉴에 둘지) 추가
- `site/scripts/sync-content.mjs`: 위 목록을 복사하고 안내·문 페이지와 시작 페이지 링크를 생성, 프론트매터에 배열 값 지원
- `site/astro.config.mjs`: 사이드바에 세 묶음 추가(강사용은 접힘)
- `site/public/favicon.svg`(파비콘 404 해소), `.github/workflows/deploy.yml`(Pages 배포), `.gitignore`(로컬 도구 폴더)
- `workshop/instructor-guide.md`, `workshop/sample-ai-output.md`: "강사 전용·배포하지 않음" 문구를 공개 정책에 맞게 수정(내용·정답은 그대로)
- 시작 페이지 문구: 선택·심화 3과정은 "향후 별도 과정 예정"으로 표시. 영어 미작성 장과 OP01~OP03은 `Planned` 유지(페이지 없음)

**검증:** 빌드 25페이지(기존 17 + 실습자료 5 + 용어집 1 + 강사용 2), 콘텐츠 감사 PASS 48 / FAIL 0, 내부 링크 715개 중 깨진 것 0(파비콘 포함), 검색·모바일(375px, 가로 넘침 없음) 확인.

## 5. 홈페이지 연결에 필요한 최소 변경(이번 단계에서는 수정하지 않음)

포털(`/ko/handbooks/`, `/en/handbooks/`)은 `src/content/handbooks.ts`의 배열을 `HandbookCard`로 그리며 교재 본문은 호스팅하지 않고 공개 Pages 주소로 링크만 건다.

1. **`handbooks.ts`에 항목 추가:** 슬러그 `ai-workspace`, 제목 "AI 워크스페이스 구축 핸드북", `chapters: 14`, `languages: ['ko']`, `repoUrl: https://github.com/victory3217-bot/rando-ai-workspace-handbook`, `pagesUrl: https://victory3217-bot.github.io/rando-ai-workspace-handbook/`, `koUrl: …/ko/`(영어 주소 없음). 초안 표기(버전, 설명의 "(초안)")는 저자 결정.
2. **`HandbookCard.astro`를 한국어 전용 교재를 처리하도록 최소 수정(필수):** 현재 카드는 태그를 항상 "Korean / English"로 쓰고 영어 버튼을 `enUrl`이 없어도 그리므로 깨진 링크가 생긴다. 태그는 `languages` 값으로, 영어 버튼은 `enUrl`이 있을 때만, GitHub 버튼은 `repoUrl`이 있을 때만 그린다. `Worksheets`/`Examples` 태그는 0이면 숨기거나 값을 정의한다.
3. `/en/handbooks/`에도 같은 카드가 나오므로 "한국어 전용" 안내를 정한다.
4. 순서: 독립 사이트 공개와 URL 확인 → 포털 변경 브랜치 → 로컬 빌드 → 미리보기 → 별도 승인 후 배포. 홈페이지 저장소의 기존 미커밋 변경(소개 영상 관련)과 섞지 않는다.

## 6. GitHub Pages 실제 공개에 필요한 최소 실행 단계(별도 승인 후)

| # | 작업 | 확인 |
|---|---|---|
| 0 | 저자 결정: B1, B8(라이선스), B9(noindex), README 공개용 정리 | 결정 기록 |
| 1 | 사이트·감사 재확인: `cd site && npm ci && npm run build`, `python -I tools/content_audit.py --dist site/dist` | PASS 48, 25페이지 |
| 2 | gitleaks 재실행(작업 트리와 이력) | 발견 없음 |
| 3 | `git status`로 커밋 대상 목록을 눈으로 확인(미추적: `ko/chapters/CH04~14`, `review/`, `workshop/`, `.github/`, `site/public/` 등 모두 공개 대상) | 의도하지 않은 파일 없음 |
| 4 | `git add`(위 목록)와 커밋. 권장 분리: ① 원고(`ko/`, `content-manifest.json`, `glossary.md`, `source-map.md`) ② 실습자료(`workshop/`) ③ 검토·계획 문서(`review/`, `CHANGELOG.md`, `README.md`) ④ 사이트·배포(`site/`, `.github/`, `.gitignore`, `tools/`). 이전 이력(커밋 2개)은 그대로 유지 | `git log`에 새 커밋 |
| 5 | 저장소 생성(공개): `gh repo create victory3217-bot/rando-ai-workspace-handbook --public --source . --remote origin --description "AI Workspace Handbook (Korean draft)"` | 저장소 URL |
| 6 | `git push -u origin main` | 원격 파일 목록이 로컬과 같음 |
| 7 | Pages 설정: Settings → Pages → Source "GitHub Actions"(또는 `gh api -X POST repos/victory3217-bot/rando-ai-workspace-handbook/pages -f build_type=workflow`) 후 `gh workflow run deploy.yml` | Actions 성공 |
| 8 | **공개 확인:** `https://victory3217-bot.github.io/rando-ai-workspace-handbook/ko/` 200, 14장·실습자료·용어집·강사용 페이지 200, 사이드바(강사용 접힘), 검색(강사용이 결과에 없음), 모바일, 배너의 홈페이지 링크, `view-source`의 noindex(B9 결정과 일치), 404, 외부 출처 링크 | 점검표 기록 |
| 9 | 포털 변경(5절) → 미리보기 확인 → 별도 승인 후 배포 | 카드에서 독립 사이트로 이동 |

**문제가 생기면:** Pages 빌드 실패는 Actions 로그를 보고 수정 후 다시 push(공개된 사이트가 없으므로 영향 없음). 잘못된 파일이 올라갔다면 먼저 노출 내용과 비밀 여부를 확인하고, 비밀이면 **폐기·재발급이 먼저**, 저장소를 비공개 전환하거나 삭제하고 정리해 다시 만든다(이력 재작성보다 새 저장소가 확실하며 포크·캐시 가능성을 가정). 사이트만 내리려면 `gh api -X DELETE repos/victory3217-bot/rando-ai-workspace-handbook/pages`. 포털 쪽은 변경 커밋을 되돌리거나 이전 배포로 되돌린다.

## 7. 공개용 README 최소 수정 제안

현재 README는 개발 메모(Phase 표기, `review/`·`tools/` 설명, 영어 점진 공개 기술 설명)가 많다. 공개 전에 다음만 고치면 충분하다: 첫머리 상태 문구(필수 14장 초안, 저자 승인 전, 공개 사이트 주소), 폴더 구조에 `workshop/` 추가, 공개 정책 한 단락(정답·해설 포함 공개, 가상 자료만 사용), 라이선스 문구. 기술 규칙 절은 유지.
