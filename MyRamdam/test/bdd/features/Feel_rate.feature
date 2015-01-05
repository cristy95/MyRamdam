Feature: Feel Rate of an item

        As a user, I want to see the rate for an item

        Scenario: Feel rate
        Given that an item has a feeling "happy"
        When the user wants to see the rating
        Then the program will view the rating

        Scenario: feel rate without added feeling/s
        Given that an item has no feeling "happy"
        When the user wants to see the rating
        Then the program will alert the user that it has no rating yet
