Feature: Share a Feeling in the facebook

         As a user, I want to share my feeling about an item in facebook.


         Scenario: Share feeling
         Given that I have a feeling for an item
         When I share it in facebook
         Then my feeling is posted


         Scenario: Share feeling 
         Given that I have a feeling for an item 
         And I am not logged-in in facebook
         When I share it in facebook
         Then I can see the log-in page in facebook

         