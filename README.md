# Timetable Generator


Timetable Generator to generate a timetable that meets the given constraints and produces the best solution.

# Background

- Hods face difficulty in arranging classes for staff in a department. This Automatic Timetable generator will schedule classes that convenience their staff without conflicts and no 3 continuous classes.

# Goals

This will produce a time-table that solves the given constraints:

- **HARD CONSTRAINTS**
    - No conflicting hours for staff around different class
    - No 3 continuous hours for a staff
    - Labs must be in [2,1] for UG and [2,2,1] for PG.
- **SOFT CONSTRAINTS**
    - Labs can be taken by two staff.

# Proposed Solution

Program a Genetic Algorithm to solve and get the best outcome that passes all constraints

### Risks

- Need to be careful in the input of the subjects and staffs details