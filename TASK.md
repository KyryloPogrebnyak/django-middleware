# Task

## Create The Following pages:

1. Add: 

-   To add a new word
-   Consist of Two textfields with one Button (Submit/Send).
-   on pages, and create a new view in `views.py`

2. Search

1.  Contains a form with one textfield
2.  Button to search

3. Create a new Middleware `CheckWordEntry`
    - if length of submitted word less than 2, show error (Think about to create an Error page in `pages`)

## Task 
1. Create another route (`word/all`) and use the same main template, show all words in a `table` (english | German|).
2. Implement Search (GET) Request. The Response should be same main template, with the word in both languages.   