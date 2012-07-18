from evelink import api

class Map(object):
    """Wrapper around /map/ of the EVE API."""

    @api.auto_api
    def __init__(self, api=None):
        self.api = api

    def jumps_by_system(self):
        """Get jump counts for systems in the last hour.

        Returns a tuple of ({system:jumps...}, timestamp).

        NOTE: Systems with 0 jumps in the last hour are not included!
        """

        api_result = self.api.get('map/Jumps')

        rowset = api_result.find('rowset')
        results = {}
        for row in rowset.findall('row'):
            system = int(row.attrib['solarSystemID'])
            jumps = int(row.attrib['shipJumps'])
            results[system] = jumps

        data_time = api.parse_ts(api_result.find('dataTime').text)

        return results, data_time

    def kills_by_system(self):
        """Get kill counts for systems in the last hour.

        Returns a tuple of ({system:{killdata}, timestamp).

        Each {killdata} is {'faction':count, 'ship':count, 'pod':count}.
        """

        api_result = self.api.get('map/Kills')

        rowset = api_result.find('rowset')
        results = {}
        for row in rowset.findall('row'):
            system = int(row.attrib['solarSystemID'])
            faction_kills = int(row.attrib['factionKills'])
            ship_kills = int(row.attrib['shipKills'])
            pod_kills = int(row.attrib['podKills'])

            results[system] = {
                'id': system,
                'faction': faction_kills,
                'ship': ship_kills,
                'pod': pod_kills,
            }

        data_time = api.parse_ts(api_result.find('dataTime').text)

        return results, data_time