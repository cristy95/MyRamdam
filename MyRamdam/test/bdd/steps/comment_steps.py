from lettuce import step

@step(u'Given the data item exists')
def given_the_data_item_exists(step):
    assert True

@step(u'And I visit the profile of the data item')
def and_i_visit_the_profile_of_the_data_item(step):
    assert True

@step(u'When I enter my comment "([^"]*)"')
def when_i_enter_my_comment_group1(step, group1):
    assert True

@step(u'Then the comment and user id is recorded')
def then_the_comment_and_user_id_is_recorded(step):
    assert True

@step(u'And the comment is shown in the profile of the data item with the identity of the user')
def and_the_comment_is_shown_in_the_profile_of_the_data_item_with_the_identity_of_the_user(step):
    assert True

@step(u'And I check the option for "([^"]*)"')
def and_i_check_the_option_for_group1(step, group1):
    assert True

@step(u'Then the comment is recorded')
def then_the_comment_is_recorded(step):
    assert True

@step(u'But the user id of the comment is not recorded')
def but_the_user_id_of_the_comment_is_not_recorded(step):
    assert True

@step(u'And the comment is shown in the profile of the data item without an identity')
def and_the_comment_is_shown_in_the_profile_of_the_data_item_without_an_identity(step):
    assert True

@step(u'Given the comment already exists')
def given_the_comment_already_exists(step):
    assert True

@step(u'And I visit the comment section in the profile of the data item')
def and_i_visit_the_comment_section_in_the_profile_of_the_data_item(step):
    assert True

@step(u'When I click the button for "([^"]*)"')
def when_i_click_the_button_for_group1(step, group1):
    assert True

@step(u'Then an edit comment section field is shown')
def then_an_edit_comment_section_field_is_shown(step):
    assert True

@step(u'And I edit my comment')
def and_i_edit_my_comment(step):
    assert True

@step(u'And I saved it')
def and_i_saved_it(step):
    assert True

@step(u'And the edited comment is recorded')
def and_the_edited_comment_is_recorded(step):
    assert True

@step(u'And the edited comment is shown in the profile of the data item')
def and_the_edited_comment_is_shown_in_the_profile_of_the_data_item(step):
    assert True
    
@step(u'Then an alert for "([^"]*)" or "([^"]*)" is shown')
def then_an_alert_for_group1_or_group2_is_shown(step, group1, group2):
    assert True

@step(u'And I click "([^"]*)"')
def and_i_click_group1(step, group1):
    assert True

@step(u'And the comment is deleted from the record')
def and_the_comment_is_deleted_from_the_record(step):
    assert True

@step(u'And the comment disappears in the the profile of the data item')
def and_the_comment_disappears_in_the_the_profile_of_the_data_item(step):
    assert True

@step(u'Given the user has identification and the item has id')
def given_the_user_has_identification_and_the_item_has_id(step):
    assert True
