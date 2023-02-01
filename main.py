from googleapiclient import discovery
import iso8601
import pytz
import datetime

project = 'Enter your Project ID here' # Enter your Project Name here
service = discovery.build('compute', 'v1')

def hello_world(request):
    snapshots = service.snapshots().list(project=project).execute()
    if(snapshots.get('items')):
        for snapshot in snapshots['items']:
            id=snapshot['name']
            snapshot_creation_timestamp=snapshot['creationTimestamp']
            print("snapshot name",id)

            date_obj=iso8601.parse_date(snapshot_creation_timestamp)
            instance_creation_timestamp=date_obj.astimezone(pytz.utc).strftime('%Y-%m-%d %H:%M:%S')
            print(instance_creation_timestamp,"Instance-Creation-Time-utc")
            snapshot_date_list=instance_creation_timestamp[:10].split("-")
            y,m,d=int(snapshot_date_list[0]),int(snapshot_date_list[1]),int(snapshot_date_list[2])
            instance_creation_date = datetime.date(y,m,d)

            utc_time_now=datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            print(utc_time_now,"utc-time-now")
            today_date_list=utc_time_now[:10].split("-")
            y,m,d=int(today_date_list[0]),int(today_date_list[1]),int(today_date_list[2])
            today_date = datetime.date(y,m,d)

            snapshot_age=today_date-instance_creation_date
            snapshot_age=int(snapshot_age.days)
            print("Snapshot age=",snapshot_age)

            if(snapshot_age==0):
                request = service.snapshots().delete(project=project, snapshot=id).execute()
            else:
                pass
            print("\n")
    return "Execution Succesfull"