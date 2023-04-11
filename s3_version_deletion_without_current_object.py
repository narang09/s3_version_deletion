import boto3

def delete_versions(bucket_name, prefix, aws_profile):
    session = boto3.Session(profile_name=aws_profile)
    s3 = session.resource('s3')
    bucket = s3.Bucket(bucket_name)

    # Delete old object versions for the given prefix
    versions = bucket.object_versions.filter(Prefix=prefix)
    for version in versions:
        if version.is_latest or version.version_id == 'null':
            continue

        version.delete()
        print(f"Deleted {version.object_key} version {version.version_id}")

    # Delete delete markers for the given prefix
    versions = bucket.object_versions.filter(Prefix=prefix)
    for version in versions:
        if not hasattr(version, 'is_latest') or version.is_latest:
            continue

        if hasattr(version, 'version_id') and version.version_id is not None:
            version.delete()
            print(f"Deleted delete marker for {version.object_key} version {version.version_id}")




# Call the function with arguments
delete_versions('testing1234554321','one/' ,'dev')
