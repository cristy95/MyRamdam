Feature: Express Feeling towards an item

        As a user, I want to choose a particular feeling
        so that I can express my feelings
        on a certain data item.

Scenario: Express feeling
        Given the user has identification and the item has id
        And the following feelings are shown:
                |feeling        |
                |happy          |
                |sad            |
                |angry          |
                |surprised      |
        When the user chooses "happy"
        Then the feeling "happy" is recorded
        And the data item is updated with the feeling

Scenario: Express feeling but session has expired
        Given the user has identification and the item has id
        And the following feelings are shown:
                |feeling        |
                |happy          |
                |sad            |
                |angry          |
                |surprised      |
        But the current session of the user already expired
        When the user chooses "sad"
        Then the system will ask for a password
        And the user will enter his password
        And the feeling "sad" is recorded
        And the data item is updated with the feeling
