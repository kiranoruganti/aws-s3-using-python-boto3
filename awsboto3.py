from urllib import response
import boto3

#creating an object for s3 service

s3_client=boto3.client("s3",
                aws_access_key_id="AKIA4XCPHACSTJIZ7EW5",
                aws_secret_access_key="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",
                )

#the above code will connect you to awss3 run the code if you get error then we are not connected to s3 
# if no error you are connected to s3


#S3 bucket creation using boto3

response = s3_client.create_bucket(
                      Bucket='awsboto3-bucket-bykiran')

# print(response)
#commented the above code becuz it has already created the bucket
# if i dont comment above code anotger bucket with same name will be created again


# uploading a file in s3 bucket

response = s3_client.put_object(
    Body=open("hellokiran.py","r").read(),
    Bucket='awsboto3-bucket-bykiran',
    Key='code written by kiran')

# print(response)



#downloading s3 bucket file

response = s3_client.get_object(
    Bucket='awsboto3-bucket-bykiran',
    Key='code written by kiran',
)

data=response.get("Body").read().decode()#reading data we got from aws s3

file1=open("output_file.py","w")#creating a file

file1.writelines(data)#inserting the data we got from aws s3  into the output_file.py file 

file1.close()


#listing number of buckets

response=s3_client.list_buckets()
buckets=response.get("Buckets")

print(f"Total Buckets: {len(buckets)} ")
print(buckets)


# listing number of objects

response=s3_client.list_objects(
    Bucket="awsboto3-bucket-bykiran"
)
objects=response.get("Contents")#we have the objects in Contents of response
print(f"Total Buckets: {len(objects)} ")
print(objects)


#deleting s3 object or file

response=s3_client.delete_object(
    Bucket="awsboto3-bucket-bykiran",
    Key="to be deleted file"
)
print(response)

#deleting s3 bucket 
response=s3_client.delete_bucket(
    Bucket="awsboto3-bucket-bykiran"
)