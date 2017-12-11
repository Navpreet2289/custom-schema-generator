# CUstom Schema Generator

> Provides a way to specify extra query parameters in generated schema documentation

## How to use

``` python
class YourView(APIView):
    schema = QuerySchema()
    query_params = ('your', 'parameters', 'here')
