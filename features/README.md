# Features

## Steps

In the steps folder you will find python code which translates the natural language feature files into executing code.

## Feature Files

The feature files are Gherkin files and they are written in natural language to test the beahviour of the software.

## Running the Feature files

To run the Feature files (BDD tests) run the following command:

    behave

Expected output:

    Feature: Lesson 0 # features/Lesson_0_dot_test.feature:1
      Testing the Lesson 0 (tutorial) functions as expected
      Scenario: Completing Lesson 0                  # features/Lesson_0_dot_test.feature:4
        Given an interaction module has been created # features/steps/interaction_steps.py:4
        Given an interaction module has been created # features/steps/interaction_steps.py:4 0.539s
        When Lesson 0 completed correctly            # features/steps/lesson_steps.py:70 10.090s
        Then The lesson is completed succesfully     # features/steps/lesson_steps.py:138 0.000s
    
    Feature: Lesson 1 # features/Lesson_1_A_to_C.feature:1
      Testing the Lesson 1 (A-C) functions as expected
      Scenario: Completing Lesson 1                  # features/Lesson_1_A_to_C.feature:4
        Given an interaction module has been created # features/steps/interaction_steps.py:4
        Given an interaction module has been created # features/steps/interaction_steps.py:4 0.116s
        When An A-C lesson is completed correctly    # features/steps/lesson_steps.py:110 5.561s
        Then The lesson is completed succesfully     # features/steps/lesson_steps.py:138 0.000s
    
    Feature: Lesson 2 # features/Lesson_2_A_to_J.feature:1
      Testing the Lesson 2 (A-J) functions as expected
      Scenario: Completing Lesson 2                  # features/Lesson_2_A_to_J.feature:4
        Given an interaction module has been created # features/steps/interaction_steps.py:4
        Given an interaction module has been created # features/steps/interaction_steps.py:4 0.116s
        When An A-J lesson is completed correctly    # features/steps/lesson_steps.py:13 16.009s
        Then The lesson is completed succesfully     # features/steps/lesson_steps.py:138 0.000s
    
    Feature: Quiz 2 # features/Quiz_2_A_to_J.feature:1
      Testing Quiz 2 (A-J) functions as expected
      Scenario: Completing Quiz 2                         # features/Quiz_2_A_to_J.feature:4
        Given an interaction module has been created      # features/steps/interaction_steps.py:4
        Given an interaction module has been created      # features/steps/interaction_steps.py:4 0.117s
        When An a quiz on letters is completed flawlessly # features/steps/quiz_steps.py:4 11.303s
        Then The quiz is completed succesfully            # features/steps/quiz_steps.py:26 0.000s
    
    4 features passed, 0 failed, 0 skipped
    4 scenarios passed, 0 failed, 0 skipped
    12 steps passed, 0 failed, 0 skipped, 0 undefined
    Took 0m43.852s

Please note:

- If any of the feature files have failed then the system is not operating as expected, so something has gone wrong.