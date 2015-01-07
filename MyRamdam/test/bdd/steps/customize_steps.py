from lettuce import *
from nose.tools import assert_equal, assert_in
from newfeel import *

@step(u'Given I add feeling "([^"]*)"')
def given_i_add_feeling_group1(step, group1):
    assert True

@step(u'And I choose "([^"]*)" as the feeling it is leaning towards')
def and_i_choose_group1_as_the_feeling_it_is_leaning_towards(step, group1):
    newfeel = NewFeel("incomplete", "sad")
    assert_equal(newfeel.addFeel(newfeel), "Ok")

@step(u'When I click the submit/post button')
def when_i_click_the_submit_post_button(step):
    assert True

@step(u'Then I could see post "([^"]*)"')
def then_i_could_see_post_group1(step, group1):
    assert False

@step(u'And I do not choose a feeling it is leaning towards')
def and_i_do_not_choose_a_feeling_it_is_leaning_towards(step):
    assert False

@step(u'Then the submit/post button is disabled')
def then_the_submit_post_button_is_disabled(step):
    assert True

@step(u'And my session has already expired')
def and_my_session_has_already_expired(step):
    assert False

@step(u'Then I could see alert "([^"]*)"')
def then_i_could_see_alert_group1(step, group1):
    assert False

@step(u'And I would have to verify back my identity')
def and_i_would_have_to_verify_back_my_identity(step):
    assert False
