import boto3
s3 = boto3.resource('s3')
# Get list of objects for indexing
images=[('venkat.jpg','Venkat Iyer'),
       ('jay.jpg','Jayashree Sundararajan'),
       ('rinna.jpg','Rinna Iyer'),
       ('aparna.jpg','Aparna Iyer')
      ]
# Iterate through list to upload objects to S3   
for image in images:
   file = open(image[0],'rb')
   object = s3.Object('rekognition4-images',image[0])
   ret = object.put(Body=file,
                   Metadata={'FullName':image[1]}
                   )
   #print(image[0])
   #print(image[1])