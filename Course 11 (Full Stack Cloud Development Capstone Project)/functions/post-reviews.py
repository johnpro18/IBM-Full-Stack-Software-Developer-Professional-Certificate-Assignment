#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
import sys
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
def main(dict):
    authenticator = IAMAuthenticator("tOic3maIRwOPCg6cAyGdTsiIHjleGzS0aQYnAW8Culls")
    service = CloudantV1(authenticator=authenticator)
    service.set_service_url("https://apikey-v2-j9cohsgelxe0eoyne00qrco737di8whwzq72sqkdkbi:3480f0797f7d7ed4114e60a671cd21d1@8f9167c7-0c70-4a05-bddc-6c47f38e80f7-bluemix.cloudantnosqldb.appdomain.cloud")
    response = service.post_document(db='reviews', document=dict["review"]).get_result()
    try:
    # result_by_filter=my_database.get_query_result(selector,raw_result=True)
        result= {
        'headers': {'Content-Type':'application/json'},
        'body': {'data':response}
        }
        return result
    except:
        return {
        'statusCode': 404,
        'message': 'Something went wrong'
        }