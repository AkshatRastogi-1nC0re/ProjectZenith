import wolframalpha
def calculate(query):
    client = wolframalpha.Client('5KUK33-JGTE9PP7T8')
    res = client.query(query)
    output = next(res.results).text
    return(output)
