# Capstone-project
# Farm Management Project 

A Django project to manage farm animals and their produce.

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

# Phase 3:  CRUD views and templates for Animal and Produce models

- Implemented class-based views for Animal and Produce (List, Detail, Create, Update, Delete)
- Added farm/urls.py with routes for animals and produce
- Created templates for Animal (list, detail, form, confirm_delete)
- Created templates for Produce (list, detail, form, confirm_delete)
- Linked CRUD functionality to models with proper fields
