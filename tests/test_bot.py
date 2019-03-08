from unittest import mock, TestCase

from slackbot.bot import Bot
from slackbot import messages


class TestBot(TestCase):

    @mock.patch('slackbot.rdw.RdwOnlineClient')
    @mock.patch('slackbot.owners.CarOwners')
    def test_slack_command_car(self, mock_car_owners, mock_rdw_client):
        bot = Bot()
        bot.car_owners = mock_car_owners
        bot.rdw_client = mock_rdw_client

        r = bot.command_car('@user1', 'help')
        assert r == messages.command_car_usage

        r = bot.command_car('@user1', '')
        assert r == messages.command_car_usage

    @mock.patch('slackbot.rdw.RdwOnlineClient')
    @mock.patch('slackbot.owners.CarOwners')
    def test_slack_command_car_lookup(self, mock_car_owners, mock_rdw_client):
        mock_car_owners.lookup.return_value = None
        mock_rdw_client.get_rdw_details.return_value = None

        bot = Bot()
        bot.car_owners = mock_car_owners
        bot.rdw_client = mock_rdw_client

        r = bot.command_car('@user1', '12-AAA-4')
        mock_car_owners.lookup.assert_called_with('12AAA4')
        assert r == messages.lookup_no_details_found

        r = bot.command_car('@user1', 'tag 1234')
        assert r == messages.command_invalid_licence_plate('1234')

        # Invalid..
        r = bot.command_car('@user1', 'tag $$-^^^-4')
        assert r == messages.command_invalid_licence_plate('$$-^^^-4')

        # Happy Flow
        r = bot.command_car('@user1', 'tag 12-AAA-4')
        assert r == 'Added 12AAA4 to @user1'
        mock_car_owners.tag.assert_called_with('12AAA4', slackid='@user1')

    @mock.patch('slackbot.rdw.RdwOnlineClient')
    @mock.patch('slackbot.owners.CarOwners')
    def test_slack_command_car_tagging(self, mock_car_owners, mock_rdw_client):
        bot = Bot()
        bot.car_owners = mock_car_owners
        bot.rdw_client = mock_rdw_client

        r = bot.command_car('@user1', 'tag')
        assert r == messages.command_tag_usage

        r = bot.command_car('@user1', 'tag 12-AAA-4 more-arguments')
        assert r == messages.command_invalid_owner('more-arguments')

        r = bot.command_car('@user1', 'tag 1234')
        assert r == messages.command_invalid_licence_plate('1234')

        # Invalid..
        r = bot.command_car('@user1', 'tag $$-^^^-4')
        assert r == messages.command_invalid_licence_plate('$$-^^^-4')

        # Happy Flow
        r = bot.command_car('user1', 'tag 12-AAA-4')
        assert r == 'Added 12AAA4 to user1'
        mock_car_owners.tag.assert_called_with('12AAA4', slackid='user1')

        r = bot.command_car('@user1', 'tag 12-AAA-4 @harry')
        assert r == 'Added 12AAA4 to @harry'
        mock_car_owners.tag.assert_called_with('12AAA4', slackid='@harry')

        r = bot.command_car('@user1', 'tag 12-AAA-4 "Grote beer"')
        assert r == 'Added 12AAA4 to "Grote beer"'
        mock_car_owners.tag.assert_called_with('12AAA4', name='Grote beer')

