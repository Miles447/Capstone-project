# Capstone-project
# Farm Management Project 

A Django project to manage farm animals and their produce.

---

## Phase 1: Initial Setup 
- Created Django project `Farm_project`.
- Added `farm` app.
- Configured project-level and app-level URLs.
- Verified homepage loads correctly.# looked as i expected
- 
## Phase 2: Models and Migrations

- Added `Animal` model with fields: name, species, age, date_added.
- Added `Produce` model with fields: animal (FK), produce_type, quantity, date_collected.
- Registered both models in the Django admin.
- Ran initial migrations for `farm` app.
