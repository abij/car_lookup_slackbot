from unittest import mock, IsolatedAsyncioTestCase

from slackbot.bot import Bot
from slackbot import messages


class TestBot(IsolatedAsyncioTestCase):

    @mock.patch('slackbot.rdw.RdwOnlineClient')
    @mock.patch('slackbot.owners.CarOwners')
    async def test_slack_command_car_help(self, mock_car_owners, mock_rdw_client):
        bot = Bot()
        bot.car_owners = mock_car_owners
        bot.rdw_client = mock_rdw_client

        assert await bot.command_car('@user1', 'help') == messages.command_car_usage
        assert await bot.command_car('@user1', '') == messages.command_car_usage

    @mock.patch('slackbot.finnik.FinnikOnlineClient')
    @mock.patch('slackbot.rdw.RdwOnlineClient')
    @mock.patch('slackbot.owners.CarOwners')
    async def test_slack_command_car_lookup(self, mock_car_owners, mock_rdw_client, mock_finnik):
        mock_car_owners.lookup = mock.AsyncMock(return_value=None)
        mock_rdw_client.get_rdw_details = mock.AsyncMock(return_value=None)
        mock_finnik.get_car_details = mock.AsyncMock(return_value=None)

        bot = Bot()
        bot.car_owners = mock_car_owners
        bot.rdw_client = mock_rdw_client
        bot.finnik_client = mock_finnik

        r = await bot.command_car('@user1', '12-AAA-4')
        mock_car_owners.lookup.assert_called_with('12AAA4')
        mock_rdw_client.get_rdw_details.assert_called_with('12AAA4')
        mock_finnik.get_car_details.assert_called_with('12AAA4')
        assert r == messages.lookup_no_details_found('12AAA4')

        assert await bot.command_car('@user1', 'tag 1234') == messages.command_invalid_licence_plate('1234')
        assert await bot.command_car('@user1', 'tag $$-^^^-4') == messages.command_invalid_licence_plate('$$-^^^-4')

        r = await bot.command_car('user1', 'tag 12-AAA-4')
        assert r == 'Added 12AAA4 to <@user1>'
        mock_car_owners.tag.assert_called_with('12AAA4', slackid='user1')

    @mock.patch('slackbot.finnik.FinnikOnlineClient')
    @mock.patch('slackbot.rdw.RdwOnlineClient')
    @mock.patch('slackbot.owners.CarOwners')
    async def test_slack_command_car_tagging(self, mock_car_owners, mock_rdw_client, mock_finnik):
        bot = Bot()
        bot.car_owners = mock_car_owners
        bot.rdw_client = mock_rdw_client
        bot.finnik_client = mock_finnik

        assert await bot.command_car('@user1', 'tag') == messages.command_tag_usage
        assert await bot.command_car('@user1', 'tag 12-AAA-4 more-arguments') == messages.command_invalid_owner('more-arguments')
        assert await bot.command_car('@user1', 'tag 1234') == messages.command_invalid_licence_plate('1234')
        assert await bot.command_car('@user1', 'tag $$-^^^-4') == messages.command_invalid_licence_plate('$$-^^^-4')

        r = await bot.command_car('user1', 'tag 12-AAA-4')
        assert r == 'Added 12AAA4 to <@user1>'
        mock_car_owners.tag.assert_called_with('12AAA4', slackid='user1')

        r = await bot.command_car('user1', 'tag 12-AAA-4 @harry')
        assert r == 'Added 12AAA4 to <@harry>'
        mock_car_owners.tag.assert_called_with('12AAA4', slackid='harry')

        r = await bot.command_car('@user1', 'tag 12-AAA-4 "Grote beer"')
        assert r == 'Added 12AAA4 to "Grote beer"'
        mock_car_owners.tag.assert_called_with('12AAA4', name='Grote beer')

        r = await bot.command_car('@user1', 'tag 12-AAA-4 "WhyTheseQoutes"')
        assert r == 'Added 12AAA4 to "WhyTheseQoutes"'
        mock_car_owners.tag.assert_called_with('12AAA4', name='WhyTheseQoutes')

    @mock.patch('slackbot.rdw.RdwOnlineClient')
    @mock.patch('slackbot.owners.CarOwners')
    async def test_slack_command_car_untag(self, mock_car_owners, mock_rdw_client):
        bot = Bot()
        bot.car_owners = mock_car_owners
        bot.rdw_client = mock_rdw_client

        assert await bot.command_car('user1', 'untag') == messages.command_tag_usage

        r = await bot.command_car('user1', 'untag 12-AAA-4')
        assert r == 'Removed the licence plate 12AAA4'
        mock_car_owners.untag.assert_called_with('user1', '12AAA4')

    def test_is_valid_owner(self):
        assert Bot._is_valid_owner("Owner of Who's") is True
        assert Bot._is_valid_owner("Some name with 'qoute") is True
