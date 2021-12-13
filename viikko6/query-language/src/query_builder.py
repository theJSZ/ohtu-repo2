from matchers import And, HasAtLeast, PlaysIn, HasFewerThan, Not, Or

class QueryBuilder:
    def __init__(self, matcher):
        self._query_object = matcher()

    def playsIn(self, team):
        return QueryBuilder(PlaysIn(self._query_object, team))

    def build(self):
        return self._query_object