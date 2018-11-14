import os
import sys
import boto3
from botocore.exceptions import ClientError
import json
import sys
import argparse
import time


def main():
    
    client = boto3.client('guardduty', region_name=os.getenv('AWS_REGION')) 

    #Find out if GuardDuty already enabled:
    detectors_list = client.list_detectors()

    if not detectors_list["DetectorIds"]:
        print ("GuardDuty is not enabled ... enabling GuardDuty on master account")
        response = client.create_detector(Enable=True)
        # Save DetectorID handler
        DetectorId = response["DetectorId"]
    else:
        print("GuardDuty already enabled on account")
        DetectorId = detectors_list['DetectorIds'][0]

    # Do error handling here

    # print all Detectorts
    detectors_list = client.list_detectors()
    print ("Detector lists: ")
    
    for x in detectors_list["DetectorIds"]:
        print(x, " ")

if __name__ == "__main__":
    main()

