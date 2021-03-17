@echo off
curl -X POST "localhost:5000/videos/queries" -H "Content-Type: application/json" -d@"%~dp0get-query.json"
echo.


@REM {
@REM    "query" : {
@REM       "wildcard" : {
@REM          "watch_url.keyword" : "*7IS7gigunyI"
@REM       }
@REM    }
@REM }
@REM {
@REM    "query" : {
@REM       "term" : {
@REM          "watch_url_hash" : "41b4d30208f3c6fda70df2c95c5dd4d157dfbbe31f216cef0f475fa4cece214b"
@REM       }
@REM    }
@REM }
@REM {
@REM   "query": {
@REM     "query_string": {
@REM       "query": "(new york city) OR (big apple)",
@REM       "default_field": "content"
@REM     }
@REM   }
@REM }
@REM // full text queries
@REM // simple queries
@REM {
@REM 	"query": {
@REM 		"match": {
@REM 			"streams.default": "23"
@REM 		}
@REM 	}
@REM }
@REM {
@REM 	"query": {
@REM 		"match": {
@REM 			"streams.default": {
@REM 				"query": "23",
@REM 				"operator": "and/or"
@REM 			}
@REM 		}
@REM 	}
@REM }
@REM {
@REM 	"query": {
@REM 		"match": {
@REM 			"streams.default": {
@REM 				"query": "23",
@REM 				"type": "phrase"
@REM 			}
@REM 		}
@REM 	}
@REM }
@REM {
@REM 	"query": {
@REM 		"multi_match": {
@REM 			"query": "22",
@REM 			"fields": ["streams.default^5", "streams.default"]
@REM 		}
@REM 	}
@REM }
@REM // coumpound
@REM {
@REM 	"query": {
@REM 		"bool": {
@REM 			"must": [
@REM 				{"match": {"streams.default":"22"}},
@REM 				{"match": {"streams.default":"22"}},
@REM 				{"match": {"streams.default":"22"}}
@REM 			],
@REM 			"must_not": [
@REM 				{"match": {"streams.default":"23"}},
@REM 				{"match": {"streams.default":"23"}},
@REM 				{"match": {"streams.default":"23"}}
@REM 			],
@REM 			"should": [
@REM 				{"match": {"streams.default":"23"}}, //optional, but scores higher is there
@REM 			]
@REM 		}
@REM 	}
@REM }

@REM // filtered queries : faster , cacheable
@REM {
@REM 	"query": {
@REM 		"filtered": {
@REM 			"query": {
@REM 				{"match": {"streams.default":"22"}}
@REM 			},
@REM 			"filter": {
@REM 				"range": { {"streams.default":{"from":0}} }
@REM 			}
@REM 		}
@REM 	}
@REM }


@REM {
@REM 	"query": {
@REM 		"bool": {
@REM 			"must": [
@REM 				{"match": {"streams.default":"22"}},
@REM 				{"match": {"streams.default":"22"}},
@REM 				{"match": {"streams.default":"22"}}
@REM 			],
@REM 			"must_not": [
@REM 				{"match": {"streams.default":"23"}},
@REM 				{"match": {"streams.default":"23"}},
@REM 				{"match": {"streams.default":"23"}}
@REM 			],
@REM 			"should": [
@REM 				{"match": {"streams.default":"23"}},
@REM 				{"match": {"streams.default":"23"}},
@REM 				{"match": {"streams.default":"23"}}
@REM 			],
@REM 			"filter": [
@REM 				{ "term":  { "status": "0" }},
@REM 				{ "range": { "streams.default":{"gte":0}}}
@REM 			]
@REM 		}
@REM 	}
@REM }

