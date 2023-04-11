import boto3

def delete_markers(bucket_name, prefix, profile_name):
    session = boto3.Session(profile_name=profile_name)
    client = session.client('s3')
    Bucket = bucket_name
    Prefix = prefix
    IsTruncated = True
    MaxKeys = 1000
    
    while IsTruncated == True:
        version_list = client.list_object_versions(
            Bucket=Bucket,
            MaxKeys=MaxKeys,
            Prefix=Prefix
        )
        try:
            objects = []
            versions = version_list ['Versions']
            for v in versions:
                objects.append({'VersionId':v['VersionId'],'Key':v['Key']})
                response = client.delete_objects(Bucket=Bucket,Delete={'Objects':objects})
                print (response)
        except:
            pass
        try:
            objects = []
            delete_markers = version_list['DeleteMarkers']
            for d in delete_markers:
                objects.append({'VersionId':d['VersionId'],'Key': d['Key']})
                response = client.delete_objects(Bucket=Bucket,Delete={'Objects':objects})
                print (response)
        except:
            pass
        IsTruncated = version_list['IsTruncated']

delete_markers('testing1234554321','one/' ,'dev')

