import boto3

def list_ec2_with_unencrypted_volumes(region="us-east-1"):
    ec2 = boto3.client("ec2", region_name=region)
    reservations = ec2.describe_instances()["Reservations"]

    for reservation in reservations:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            print(f"Instance ID: {instance_id}")

            for mapping in instance.get("BlockDeviceMappings", []):
                volume_id = mapping["Ebs"]["VolumeId"]
                volume = ec2.describe_volumes(VolumeIds=[volume_id])["Volumes"][0]

                if volume["Encrypted"]:
                    print(f" Volume {volume_id} is encrypted")
                else:
                    print(f" Volume {volume_id} is NOT encrypted")

if _name_ == "_main_":
    list_ec2_with_unencrypted_volumes("us-east-1")
