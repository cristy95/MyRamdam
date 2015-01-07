# -*- coding: utf-8 -*-
from lettuce import step
from nose.tools import *
#from feelings import Feeling

#FEELING = Feeling()

@step(u'Given the user has identification and item has id')
def given_the_user_has_identification_and_item_has_id(step):
    assert True


@step(u'And the following feelings are shown')
def and_the_following_feelings_are_shown(step):
	assert True


@step(u'When the user chooses "([^"]*)"')
def when_the_user_chooses_feeling(step, feeling1):
    assert True


@step(u'Then the feeling "([^"]*)" is recorded')
def then_the_feeling_group1_is_recorded(step, feeling1):
    user_id = "007"
    item_id = "008"

    assert_equal(manager1.add_user_feeling(user_id, 001, item_id), 'OK')
	assert_equal(manager1.add_rate_count(item_id, 001), 'OK')
	assert_equal(manager1.add_daily_log(001), 'OK')


@step(u'And the data item is updated with the feeling')
def and_the_data_item_is_updated_with_the_feeling(step):
    assert True


@step(u'But the current session of the user already expired')
def but_the_current_session_of_the_user_already_expired(step):
    assert True

@step(u'Then the system will ask for a password')
def then_the_system_will_ask_for_a_password(step):
    assert True


@step(u'And the user will enter his password')
def and_the_user_will_enter_his_password(step):
    assert True


@step(u'And the feeling is recorded')
def and_the_feeling_is_recorded(step):
    user_id = "007"
    item_id = "008"

    assert_equal(manager1.add_user_feeling(user_id, 001, item_id), 'OK')
	assert_equal(manager1.add_rate_count(item_id, 001), 'OK')
	assert_equal(manager1.add_daily_log(001), 'OK')
