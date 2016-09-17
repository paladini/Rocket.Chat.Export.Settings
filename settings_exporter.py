#!/usr/bin/python
import os
import sys
import argparse
from pymongo import MongoClient

options = None
from_db = None
to_db = None

configs_to_export = {
    "smtp": [
        "SMTP_Host", "SMTP_Port", "SMTP_Username", "SMTP_Password", "From_Email"
    ],
    "file_upload": [
        "FileUpload", "FileUpload_Enabled", "FileUpload_MaxFileSize", "FileUpload_MediaTypeWhiteList", 
        "FileUpload_ProtectFiles", "FileUpload_Storage_Type", "FileUpload_ProtectFiles", "FileUpload_Storage_Type",
        "FileUpload_S3_Bucket", "FileUpload_S3_Acl", "FileUpload_S3_Bucket", "FileUpload_S3_AWSAccessKeyId",
        "FileUpload_S3_AWSSecretAccessKey", "FileUpload_S3_CDN", "FileUpload_S3_Region", "FileUpload_S3_BucketURL",
        "FileUpload_S3_URLExpiryTimeSpan"
    ]
}

def get_opt():
    parser = argparse.ArgumentParser(description="Export settings from one Rocket.Chat instance to another.")
    parser.add_argument('-s', "--smtp", action='store_const', const=True, default=False)
    parser.add_argument('-u', "--file-upload", action='store_const', const=True, default=False)
    parser.add_argument("origin", help="The IP Address of the MongoDB database that you would like to export configs. Eg: 172.12.0.3:27017.", action='store')
    parser.add_argument("destiny", help="The IP Address of the MongoDB database that you would like to import configs. Eg: 172.12.0.5:27017", action='store')
    return parser.parse_args()

def check_configs_to_export():
    if (not options.smtp): configs_to_export.pop('smtp', None)
    if (not options.file_upload): configs_to_export.pop('file_upload', None)

def export_configs():
    settings = from_db['rocketchat_settings']
    configs = {}

    for key, values in configs_to_export.items():
        for value in values:
            configs[value] = settings.find_one({"_id": value})

    return configs

def import_configs(new_configs):
    settings = to_db['rocketchat_settings']

    for key, values in configs_to_export.items():
        for value in values:
            settings.replace_one({"_id": value}, new_configs[value])

            # Update "ts" and "_updatedAt" to current date.
            settings.update({"_id": value}, {"$currentDate": {"ts": { "$type": "date" }}})
            settings.update({"_id": value}, {"$currentDate": {"_updatedAt": { "$type": "date" }}})

if __name__ ==  "__main__":

    options = get_opt()
    check_configs_to_export()

    # Trying to access databases
    from_db = MongoClient('mongodb://{}/'.format(options.origin)).rocketchat
    to_db = MongoClient('mongodb://{}/'.format(options.destiny)).rocketchat

    # Import all configs from "origin" Rocket.Chat instance.
    configs = export_configs()

    # Exporting configs to "destiny" Rocket.Chat instance.
    import_configs(configs)

    print("\n=================================================================\n")
    print("Done!")
