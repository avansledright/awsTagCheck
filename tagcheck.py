import boto3


ec2 = boto3.resource('ec2')
inst_describe = ec2.instances.all()

for instance in inst_describe:
    tag_to_check = 'Backup'
    if tag_to_check not in [t['Key'] for t in instance.tags]:
        print("This instance is not tagged: ", instance.instance_id)
        response = ec2.create_tags(
            Resources= [instance.instance_id],
            Tags = [
                {
                    'Key': 'Backup',
                    'Value': 'Yes'
                }
            ]
        )
# Double check that there are no other instances without tags
for instance in inst_describe:
    if tag_to_check not in [t['Key'] for t in instance.tags]:
        print("Failed to assign tag, or new instance: ", instance.instance_id)        