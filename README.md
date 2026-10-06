# Agile CI/CD practice

## Student details
Student identifier: [complete with an approved identifier]
Group: [complete]

## Sprint goal
Deliver a Sprint Dashboard that accurately displays completed story points and can be updated through an automated, tested release process.

## Product backlog
| ID | Story | Acceptance criteria |
|---|---|---|
| US-01 | As a team member, I want to see the sprint goal. | Published page displays Sprint Dashboard and the sprint goal. |
| US-02 | As a Scrum Master, I want accurate completed points. | Only Done items count; sample result is 5. |
| US-03 | As a developer, I want automated checks. | PR checks run and failed tests prevent deployment. |
| US-04 | As a stakeholder, I want to identify the sprint. | Page displays Sprint 1; an automated test checks it. |

## Definition of Done
- Acceptance criteria satisfied.
- Automated tests pass.
- Change reviewed and merged into main.
- Deployment succeeds and published page is checked.
- Evidence is recorded.

## Local commands optional
Run from this directory with Python 3.12:
```
python -m unittest discover -v
python build.py
python -m http.server 8000 --directory dist
```
Open http://localhost:8000 and press Ctrl+C to stop the server.

## Pipeline
Pull requests test and build. Pushes to main test, build and deploy to GitHub Pages. Manual runs test and build only. Configure Settings > Pages > Source > GitHub Actions before committing the workflow.

## Links
Website: [complete]
Feature PR: [complete]
Defect experiment PR: [complete]
Recovery PR: [complete]

## Review and retrospective
Record review decisions, observed limitations and improvements here or in your report.
