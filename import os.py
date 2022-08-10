pip install looker_sdk
import os
import looker_sdk
os.environ["LOOKERSDK_BASE_URL"] = "https://propellantdigital.cloud.looker.com"
os.environ["LOOKERSDK_CLIENT_ID"] = "vxnbWYrhnNthXtDdtRfr"
os.environ["LOOKERSDK_CLIENT_SECRET"] = "y4J9S9yTkmKj3C2FjxgF9NCs"
sdk = looker_sdk.init40()
# posttrade rts2
explore_id = "NyUYQjg3lkLyv0c0l1W91A"
explore_query = sdk.query_for_slug(slug=explore_id)
print("Query: " + str(explore_query))
result = sdk.run_query(
 explore_query.id,
 result_format="csv",
 limit= 50)
print(result)