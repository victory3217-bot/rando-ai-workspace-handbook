# AI Workspace Handbook / AI 워크스페이스 구축 핸드북

> **상태: 공개된 초안 (v0.0.4).** 한국어 **필수 과정 CH01~CH14의 본문 초안**이 있으며 모두 `Draft`다. 저자 승인과 실제 학습자 시험은 아직 없다. 선택·심화 OP01~OP03은 `content-manifest.json`에 등록만 되어 있다(`Planned`). 영어 본문은 없다. 사이트: https://victory3217-bot.github.io/rando-ai-workspace-handbook/

프로그래밍 경험이 없는 일반 실무자가 자신의 컴퓨터, 클라우드 저장소, AI 도구, 업무문서를 연결해 **개인 AI 업무환경**을 만들고 실제 업무 하나를 끝내도록 돕는 실습형 핸드북이다. 성공 기준은 AI 도구의 기능을 많이 아는 것이 아니라, 자신의 업무에 쓸 수 있는 환경을 만들고 업무 하나를 완수하는 것이다.

*A public draft of a hands-on handbook for non-programmers. The 14 core Korean chapters exist as drafts that have not been approved by the author or tested with learners; the three optional chapters are only registered as Planned. There is no English edition yet.*

## 저작권과 이용 조건 / Copyright and terms of use

- 이 저장소의 교재, 실습자료, 강사용 안내서, 사이트 코드와 그 밖의 모든 내용의 저작권은 저자(Magis Global)에게 있다. **별도의 오픈소스 라이선스를 부여하지 않는다.**
- 개인의 학습과 교육 참고를 위해 읽고 웹사이트에서 사용하는 것은 환영한다. 그 밖의 복제, 수정, 재배포, 번역, 상업적 이용(강의·교재·상품에 쓰는 것 포함)은 사전에 저자의 허락을 받아야 한다.
- 내용은 **저자 승인 전의 초안**이며, 제품 기능과 정책은 바뀔 수 있다. 각 장에 적힌 출처와 확인일을 기준으로 직접 다시 확인하고, 조직의 정보보안 규정이 우선한다. 법률·보안 자문이 아니다.
- 모든 예시(회사, 인물, 파일, 회의 메모, AI 결과물)는 교육용 가상 자료이며 실제와 무관하다.

*No open-source license is granted. All rights are reserved by the author (Magis Global). Reading and using the site for personal study is welcome; copying, modifying, redistributing, translating, or commercial use requires the author's prior permission. This is an unreviewed draft, not legal or security advice, and all examples are fictional.*

## 공개 정책

교안(CH01~CH14), 실습자료와 워크북, **강사용 해설과 정답**, 워크숍 운영자료, 용어집, 사이트 코드, 저자 검토기록을 이 저장소에 모두 공개한다. 실제 개인정보·고객정보·비밀번호·API 키·허가되지 않은 타인의 비공개 자료는 어디에도 넣지 않으며 모든 예시는 가상이다. 웹사이트에서는 학습자가 실습 전에 정답을 먼저 보지 않도록 강사용 안내서를 별도 메뉴(기본 접힘)와 안내 페이지 뒤에 두고 검색에서 제외한다. 저자 승인 전의 초안이다. 공개 절차는 `review/LAUNCH_PLAN_PUBLIC.md`를 본다.

## 구성

- **현재 핸드북의 기본 범위는 필수 14장**(`AW-CH01`~`AW-CH14`)이다. 1차 교육대상은 비개발자 일반 실무자다.
- **선택·심화 3장**(`AW-OP01`~`AW-OP03`)은 삭제하지 않고 `Planned`로만 유지한다. Git·GitHub, Claude Code, 하네스 엔지니어링은 *향후 별도 교육과정*으로 분리해 개발하는 방향이며, 현재 프로젝트 범위에서 집필을 보류한다.
- 한국어를 먼저 쓰고 검토한다. 영어는 한국어 장이 `Reviewed`가 된 뒤 시작한다.
- 모든 장은 같은 아홉 단계를 따른다: 학습목표 → 핵심 개념 → 업무 적용 사례 → 준비물 → 단계별 실습 → 결과 검증 → 오류 해결 → 완료 체크리스트 → 참고자료.

| ID | 제목 | 상태 |
|---|---|---|
| AW-CH01 | AI 워크스페이스란 무엇인가 | Draft (본문 초안, 저자 승인 전) |
| AW-CH02 | AI 워크스페이스의 구성요소와 전체 구조 | Draft (본문 초안, 저자 승인 전) |
| AW-CH03 | AI에 입력할 수 있는 정보와 정보보안 | Draft (본문 초안, 저자 승인 전) |
| AW-CH04 | PC·파일·폴더 관리 | Draft (본문 초안, 저자 승인 전) |
| AW-CH05 | 클라우드 저장소와 업무자료 연결 | Draft (본문 초안, 저자 승인 전) |
| AW-CH06 | ChatGPT 작업환경 구축 | Draft (본문 초안, 저자 승인 전) |
| AW-CH07 | Claude 작업환경 구축 | Draft (본문 초안, 저자 승인 전) |
| AW-CH08 | 개인 지식베이스 구축 | Draft (본문 초안, 저자 승인 전) |
| AW-CH09 | 문서작성과 자료분석 실습 | Draft (본문 초안, 저자 승인 전) |
| AW-CH10 | 프롬프트를 업무 지침서로 표준화 | Draft (본문 초안, 저자 승인 전) |
| AW-CH11 | 반복 업무와 AI Workflow 설계 | Draft (본문 초안, 저자 승인 전) |
| AW-CH12 | 결과 검증과 오류 해결 | Draft (본문 초안, 저자 승인 전) |
| AW-CH13 | 백업·버전 관리 기초 | Draft (본문 초안, 저자 승인 전) |
| AW-CH14 | 나만의 AI 워크스페이스 완성 | Draft (본문 초안, 저자 승인 전) |
| AW-OP01 | Git과 GitHub 기초 | Planned |
| AW-OP02 | Claude Desktop과 AI 코딩 도구 | Planned |
| AW-OP03 | AI 하네스 엔지니어링 입문 | Planned |

`Draft`는 본문 초안이 있으나 저자 승인과 학습자 시험 전이라는 뜻이고(`last_reviewed`는 비어 있음), `Planned`는 "등록만 했고 파일이 없다"는 뜻이다. 어떤 페이지도 생성되지 않는다. (정확한 상태는 `content-manifest.json`이 기준이며 이 표는 사람이 읽기 위한 사본이다.)

## 폴더 구조

```
content-manifest.json   장별 상태 (chapter_id, title, language, status, last_reviewed)
VERSION  CHANGELOG.md  glossary.md  source-map.md
ko/chapters/            한국어 장 (CH01.md ...)  ← 기준 원본
en/                     영어판. 지금은 README만 있고 장 파일이 없다
assets/templates/       장별 표준 템플릿 (한국어·영어)
workshop/               6시간 워크숍 실습자료(가상 자료, 참가자 워크북, 강사용 안내서와 정답). 사이트의 실습자료·강사용 메뉴로 게시됨
review/                 저자 검토 자료(장마다 한 쪽)와 통합 검토·워크숍·런칭 계획. 저장소에는 공개되며 사이트에는 게시되지 않음
tools/content_audit.py  구조 감사 도구 (읽기 전용)
site/                   Astro + Starlight 사이트 (생성 계층)
```

`site/src/content/docs/`는 빌드할 때마다 `ko/`, `en/`에서 다시 만들어지는 **생성물**이며 git에서 제외된다. 고치려면 항상 `ko/` 또는 `en/` 원본을 고친다. 동기화 스크립트는 원본을 읽기만 하고, 지우는 것은 생성 폴더뿐이다.

## 규칙

1. **장 ID**는 언어와 무관하게 고정한다 (`AW-CH01`...). 파일 첫 줄에 `<!-- chapter_id: AW-CHxx -->`를 넣고, 매니페스트·파일 이름과 일치해야 한다.
2. **미완성 장을 완성품처럼 보이지 않게 한다.** `Planned`는 페이지가 없고, `Draft`는 사이트에서 "초안" 표시와 안내 배너가 붙는다.
3. **영어 페이지는 영어 장이 `Reviewed` 또는 `Published`일 때만** 만들어진다. 영어 장이 하나도 해당하지 않으면 Starlight에 영어 언어를 아예 등록하지 않으므로 `/en/` 경로가 생기지 않는다. 영어 장이 하나라도 생기면 영어를 Starlight의 *기본 언어*로 바꾼다(아래 "영어 점진 공개" 참고). 영어 장은 한국어 장이 먼저 `Reviewed` 이상이어야 하며, 없으면 `npm run build`가 멈춘다.
4. **하네스 사례**는 공개가 확인된 저장소만 쓰고, 저장소 이름·파일 경로·확인한 내용·진행 상태·확인일을 모두 적는다. 비공개 저장소, 실제 고객자료, 미공개 교육자료는 쓰지 않는다. 기록은 `source-map.md`에 둔다.
5. **다른 장으로 가는 `.md` 상대 링크는 쓰지 않는다.** 사이트에서 깨진다. 장 ID(`AW-CH02`)만 적는다.
6. 도구 화면·요금·계정 조건처럼 바뀌는 내용은 공식 문서를 근거로 쓰고 각 장의 참고자료 표에 확인일을 적는다. 확인하지 못한 것은 〔확인 필요〕로 남긴다.
7. 연습에는 가상 자료만 쓴다. 개인정보, 회사 기밀, API 키는 예시에도 넣지 않는다.

## 사용법

필요한 것: Node.js 22.23.4 이상, Python 3 (감사 도구).

```bash
cd site
npm ci
npm run build        # 동기화 후 site/dist 생성
npm run dev          # 로컬 미리보기
```

```bash
python tools/content_audit.py                  # 원본 구조 감사
python tools/content_audit.py --dist site/dist # 빌드 결과까지 감사 (빌드 후)
```

감사는 읽기 전용이다. 실행하지 못한 검사는 `SKIP`으로 표시되며 PASS로 세지 않는다.

## 기술 버전 선택과 근거

선택: **Astro 7.4.2 + Starlight 0.42.7** (`site/package.json`에 정확한 버전으로 고정, `package-lock.json` 포함). 2026-10-26 기준이며 npm 레지스트리 정보와 이 컴퓨터(Windows 11, Node 24.19.0, npm 11.17.0)에서의 실제 설치·빌드로 확인했다.

| 비교 항목 | 기존 조합 재사용 (Astro 5.18.2 + Starlight 0.30.6, pricing-handbook과 같음) | 최신 조합 (Astro 7.4.2 + Starlight 0.42.7) — **선택** |
|---|---|---|
| 설치 후 `npm audit` (운영 의존성) | 16건 (critical 1, high 3, moderate 9, low 3). 해결은 메이저 업그레이드로만 가능하다고 나옴 | **0건** |
| 이 프로젝트 빌드 | 성공 | 성공 (설정 한 곳 수정 필요, 아래) |
| Astro 요구 Node | 18.20.8 / 20.3 이상 / 22 이상 | 22.23.4 이상 |
| Starlight ↔ Astro | Starlight 0.30.6은 Astro ^5 | Starlight 0.42.7은 Astro ^7.2.10 |
| 코드 변경 | 없음 | 사이드바 그룹 형식 1곳 (`autogenerate`를 `items` 안으로). 이 형식은 Starlight 0.39.0에서 바뀌었다 |
| 장점 | 형제 핸드북과 동일해 동기화 스크립트·설정을 그대로 재사용 | 알려진 보안 경고 없음, 최신 버전에서 시작해 나중의 대규모 업그레이드를 피함 |
| 위험 | 알려진 보안 경고(정적 사이트라 서버 기능을 쓰지 않아 영향은 제한적일 것으로 보이나 **개별 평가는 하지 않았다**). 오래된 메이저에 머무름 | Starlight가 1.0 이전이라 마이너 버전 사이에도 설정이 바뀔 수 있음. Node 22.23.4 이상이 필요. 형제 저장소와 버전이 다름 |
| GitHub Pages | 정적 출력이라 가능 | 정적 출력이라 가능. 배포 워크플로의 Node를 22.23.4 이상(또는 24)으로 맞춰야 함 |

선택 이유: 요구사항이 "안정성과 구현 복잡도 우선"이었다. 최신 조합은 보안 경고가 없고 필요한 코드 변경이 한 곳뿐이어서, 알려진 경고를 안고 시작할 이유가 없다고 판단했다.

**확인하지 않은 것**
- GitHub Pages에 실제로 배포해 보지 않았다. 배포 워크플로(`.github/workflows`)는 만들지 않았다.
- Phase 2B와 2C에서 내장 브라우저로 375·768·1440px 화면을 확인했다(가로 넘침, 사이드바·메뉴, 이전/다음, 코드블록 복사 버튼, 검색, 한국어 줄바꿈). 실제 스마트폰, Safari·Firefox 등 다른 브라우저, 인쇄 화면은 확인하지 않았다.
- **코드블록 복사 버튼:** 버튼이 복사하는 문자열(`data-code`)이 화면에 보이는 양식과 CH01~CH03의 모든 코드블록에서 일치함은 확인했다. 그러나 내장 브라우저에서는 일반 텍스트 영역에서도 복사·붙여넣기가 동작하지 않아(대조 실험) **실제 클립보드 복사는 확인하지 못했다**. Phase 2B 보고서에 "복사 완료!"를 확인했다고 쓴 것은 버튼의 라벨 속성을 읽은 것이었고 성공 표시가 아니었다. 일반 브라우저에서 사람이 한 번 눌러 보아야 한다.
- 기존 조합의 보안 경고가 이 정적 사이트에 실제로 악용될 수 있는지는 평가하지 않았다.
- 빌드 경고 `The collection "i18n" does not exist or is empty`는 Phase 2B에서 원인을 확인하고 없앴다. Starlight(`dist/utils/translations.js`)가 빌드할 때 선택 컬렉션 `i18n`(`src/content/i18n/<언어>.json`, 사용자 지정 화면 문구)을 읽는데 이 저장소에 없어서 났다. `content.config.ts`에 컬렉션을 선언하고 빈 `ko.json`을 두었다. 화면 문구는 바뀌지 않는다.
- 빌드 경고 `Entry docs → 404 was not found`는 남아 있다. 원인은 확인했다. Starlight의 404 경로(`utils/routing/data.js`)가 `getEntry("docs", "404")`로 직접 만든 404 문서를 찾고, 없으면 내장 기본 404 페이지로 대체한다. 그래서 `dist/404.html`은 정상 생성된다. 404 문서를 생성해 보았더니 대신 `Could not render /404 ... conflicts with higher priority route` 경고가 나와서 되돌렸다. 경고 하나를 다른 경고로 바꾸는 것뿐이라 그대로 둔다.
- **영어 점진 공개(Phase 2D에서 해결책을 시험함, 실제 영어 본문으로는 시험하지 않음):** 아래 "영어 점진 공개" 절 참고.
- 기존 조합(Astro 5)을 설치했을 때는 npm이 `esbuild`, `sharp`의 설치 스크립트가 허용 목록에 없다고 경고했다. 최종 선택한 조합을 설치할 때는 이 경고가 나오지 않았고 빌드도 성공했다.

## 영어 점진 공개

**문제:** Starlight는 기본 언어의 모든 문서에 대해 다른 언어 주소에 **기본 언어 본문을 그대로 보여 주는 대체 페이지**를 자동으로 만든다(`utils/routing/index.js`). 한국어를 기본 언어로 두고 영어 장을 하나만 공개하면, 번역하지 않은 장의 `/en/` 주소에 한국어 본문이 나온다(임시 복사본에서 확인). `draft: true`로는 막을 수 없다(draft 문서는 목록에서 빠져서 대체 페이지가 그대로 생긴다).

**적용한 방법(임시 복사본에서 시험한 뒤 적용):** 한국어는 항상 영어보다 많거나 같다(영어 장은 한국어 `Reviewed` 이후에만 가능, 감사 도구와 동기화 스크립트가 강제). 그러므로 영어 장이 하나라도 공개될 때 **영어를 Starlight 기본 언어로** 둔다. 대체 페이지는 "기본 언어 → 다른 언어" 방향으로만 만들어지므로, 한국어에는 영어가 없어도 대체 페이지가 생기지 않는다.

| 조건 | 구현 |
|---|---|
| 번역하지 않은 장은 영어 주소에 나타나지 않음 | 영어를 기본 언어로 설정(`site/astro.config.mjs`). 해당 주소는 404 |
| 번역된 장은 영어로 표시 | `Reviewed`/`Published` 영어 장만 `site/scripts/sync-content.mjs`가 페이지로 생성 |
| 영어 목차에는 공개된 장만 | 영어 페이지의 사이드바에서 빈 묶음(Part)을 제거(`site/src/route-data.ts`) |
| 언어 전환은 존재하는 페이지로만 | 언어 선택기를 교체(`site/src/components/LanguageSelect.astro`). 같은 장이 없으면 그 언어의 첫 페이지로 이동 |
| 검색에 미공개 영어 내용 없음 | 대체 페이지가 없으므로 검색 색인에도 없음. 언어별 검색이 분리됨 |
| `hreflang`·사이트맵에 없는 페이지 없음 | `route-data.ts`가 없는 페이지의 `hreflang`을 제거. 사이트맵은 실제 생성 페이지만 포함 |
| 한국어 페이지는 기존과 동일 | 영어가 없는 현재 상태에서 커밋 `dff817e`의 빌드와 모든 페이지를 비교해 동일함을 확인 |

**시험 결과(임시 복사본, 영어 1장 → 2장 공개):** `/en/`에 목차와 공개된 장만 생성, 번역하지 않은 장은 404, 영어 페이지에 한국어 본문 없음, 영어 검색에서 한국어 검색어는 결과 없음(반대도 마찬가지), 한국어 장의 언어 선택기는 같은 영어 장이 없을 때 영어 첫 페이지로 이동. 감사 도구(`--dist`)의 관련 검사는 이 구성에서 통과하고, 대체 장치를 빼면 실패하는 것을 확인했다.

**알려진 한계**
- 시험에 쓴 영어 본문은 한 줄짜리 테스트 문서였다. 실제 번역 본문으로는 시험하지 않았다.
- 영어를 기본 언어로 두면 사이트 전체의 404 페이지가 영어로 표시된다(한국어 방문자도). 이 페이지를 한국어·영어 겸용으로 바꾸려는 시도는 `Could not render /404 ...` 경고를 만들어 하지 않았다.
- `LanguageSelect.astro`는 Starlight 0.42.x의 원본 컴포넌트를 복사해 고친 것이다. Starlight를 올릴 때 원본과 비교해야 한다.
- 이 구성은 *영어와 한국어 두 언어*만을 전제로 한다. 세 번째 언어를 추가할 때는 다시 설계해야 한다.

## 앞으로 할 일

- (완료) 일반 페이지의 `noindex`를 제거했다. 강사용 안내서 두 페이지는 따로 `noindex`를 유지한다.
- 영어 장은 한국어 `Reviewed` 이후에 시작한다.
- Magis Global 핸드북 목록 연결은 아직 하지 않았다(최소 변경안은 `review/LAUNCH_PLAN_PUBLIC.md`).
