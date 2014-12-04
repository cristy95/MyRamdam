Feature: Express Feeling towards an item

        As a user, I want to choose a particular feeling
        so that I can express my feelings
        on a certain data item.

Scenario: Express feeling
        Given the user has identification and the item has id
        And the various feelings are shown
        When the user chooses a feeling
        Then the feeling is recorded
        And the data item is updated with the feeling

Scenario: Express feeling but session has expired
        Given the user has identification and the item has id
        And the various feelings are shown
        But the current session of the user already expired
        When the user chooses a feeling
        Then the system will ask for a password
        And the user will enter his password
        And the feeling is recorded
        And the data item is updated with the feeling
