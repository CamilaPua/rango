from serpapi import GoogleSearch
import json

def read_serpapi_key():
    """
    reads the SERPAPI key from a file called 'serpapi.key'
    returns: a string which is either None, i.e. no key found, or with a key
    remember to put serpapi.key in your .gitignore file to avoid committing it.
    Below we use the "with" command when opening documents
    As recommended by the Python Anti-Patterns site, see
    http://bit.ly/twd-antipattern-open-files
    it is a really neat site for showing you how to avoid writing poor python code.
    """

    serp_api_key = None
    try:
        with open('serpapi.key', 'r') as f:
            serp_api_key = f.readline().strip()
    except:
        raise IOError('serpapi.key file not found')

    if not serp_api_key:
        raise KeyError('SerpApi key not found')


def run_search(params):
    search = GoogleSearch(params)
    response = search.get_dict()
    return response


def read_serpapi_key():
    serp_api_key = None
    try:
        with open('serpapi.key', 'r') as f:
            serp_api_key = f.readline().strip()
    except:
        raise IOError('serpapi.key file not found')
    
    if not serp_api_key:
        raise KeyError('SerApi Key not found')

    return serp_api_key


def run_query(search_terms):
    key = read_serpapi_key()
    params = {
        "engine": "duckduckgo",
        "q": search_terms,
        "cc": "US",
        "api_key": key
    }

    search = GoogleSearch(params)
    response = search.get_dict()
    results = None

    if 'organic _results' in response:
        results = response['organic_results']

    return results


def main():
    params = {
        "engine": "duckduckgo",
        "q": "Tango With Django",
        "cc": "US",
        "api_key": "API_KEY"
        }
    response = run_search(params)
    #print(response)
    #print('-------------')
    result_list = response['organic_results']
    for r in result_list:
        title = r['title']
        link = r['link']
        snippet = r['snippet']
        print(title)
        print(snippet)
        print(link)
        print('-----------------------')

    for k,v in response.items():
        print(k)

    with open('search.json','w') as f:
        json.dump(response, f)

if __name__ == '__main__':
    main()
