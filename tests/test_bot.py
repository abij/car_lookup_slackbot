from unittest import mock, TestCase

from slackbot.bot import Bot
from slackbot import messages


class TestBot(TestCase):

    @mock.patch('slackbot.rdw.RdwOnlineClient')
    @mock.patch('slackbot.owners.CarOwners')
    def test_slack_command_my_car_usage(self, mock_car_owners, mock_rdw_client):
        bot = Bot()
        bot.car_owners = mock_car_owners
        bot.rdw_client = mock_rdw_client

        r = bot.command_my_car('user1', 'help')
        assert r == messages.command_usage

        r = bot.command_my_car('user1', '')
        assert r == messages.command_invalid_usage(1)

    @mock.patch('slackbot.rdw.RdwOnlineClient')
    @mock.patch('slackbot.owners.CarOwners')
    def test_slack_command_my_car_tag(self, mock_car_owners, mock_rdw_client):
        bot = Bot()
        bot.car_owners = mock_car_owners
        bot.rdw_client = mock_rdw_client

        r = bot.command_my_car('user1', 'tag')
        assert r == messages.command_invalid_usage(1)

        r = bot.command_my_car('user1', 'tag 12-AAA-4 more-arguments')
        assert r == messages.command_invalid_usage(3)

        r = bot.command_my_car('user1', 'tag 1234')
        assert r == messages.command_invalid_licence_plate('1234')

        # Invalid..
        r = bot.command_my_car('user1', 'tag $$-^^^-4')
        assert r == messages.command_invalid_licence_plate('$$-^^^-4')

        # Happy Flow
        r = bot.command_my_car('user1', 'tag 12-AAA-4')
        assert r == 'Added 12AAA4 to your slack handle'
        mock_car_owners.tag.assert_called_with('user1', '12AAA4', name='')

