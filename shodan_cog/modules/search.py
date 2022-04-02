import discord
import shodan
import sys

def get_result(*args, **kwargs):
    return shodan_search(*args, **kwargs)

def shodan_search(*args, **kwargs):
    API_KEY = args[1].get("api_key")
    QUERY = args[0]

    # The list of properties we want summary information on
    FACETS = [
        'org',
        'domain',
        'port',
        'asn',

        # We only care about the top 3 countries, this is how we let Shodan know to return 3 instead of the
        # default 5 for a facet. If you want to see more than 5, you could do ('country', 1000) for example
        # to see the top 1,000 countries for a search query.
        ('country', 3),
    ]

    FACET_TITLES = {
        'org': 'Top 5 Organizations',
        'domain': 'Top 5 Domains',
        'port': 'Top 5 Ports',
        'asn': 'Top 5 Autonomous Systems',
        'country': 'Top 3 Countries',
    }
        
    try:
        # Setup the api
        api = shodan.Shodan(API_KEY)

        # Generate a query string out of the command-line arguments
        query = QUERY

        # Use the count() method because it doesn't return results and doesn't require a paid API plan
        # And it also runs faster than doing a search().
        result = api.count(query, facets=FACETS)

        embed=discord.Embed(title="Shodan Summary Information", url="https://www.shodan.io", description="Query: {}".format(query))

        # Print the summary info from the facets
        for facet in result['facets']:
            title = FACET_TITLES[facet]
            data = ""

            for term in result['facets'][facet]:
                data += ('%s: %s' % (term['value'], term['count']))
                data += "\n"

            embed.add_field(name=title, value=data, inline=False)
        embed.set_footer(text="Total Results Found: {}".format(result['total']))

        return embed

    except Exception as e:
        embed=discord.Embed(title="Error", url="https://www.shodan.io", description="('Error: {}".format(e))

