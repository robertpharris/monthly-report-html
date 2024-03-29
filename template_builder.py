table_list = {'Table':{1.1:'KPI Summary',2.1:'Key Initiatives', 3.1: 'Safety Summary',
                       4.1: 'MTD Financial Performance',
              4.2:'YTD Financial Performance', 4.3:'REC Summary', 5.1:'Site Summary', 5.2: 'Lost Energy',
                       6.1: 'Turbine Performance', 6.2: 'Offline and Curtailed (current month over 7 days)',
                       6.3:'top Turbine Fault and Event States', 7.1: 'Grid Operator Curtailment Summary',
                       7.2: 'Balance of Plant Outages', 8.1: 'Maintenance Summary', 9.1: 'Compliance Log',
                       10.1:'Definitions'},
              'Figure': {5.1:'Monthly Energy Production', 5.2:'Daily Wind Speed and Project Availability',
                         },
              'Section': {1: 'Executive Summary', 2: 'Operations Management', 3: 'Safety',
                          4: 'Financial Performance', 5: 'Site Performance', 6: 'Turbine Performance',
                          7: 'Balance of Plant', 8: 'Planned Maintenance', 9:'Compliance', 10: 'Definitions'}

}
import boto3
import re
import json
s3 = boto3.client('s3')
BUCKET = 'lre-report-api'#/templates/wind_template/
file_list = s3.list_objects(Bucket=BUCKET)['Contents']

# read in template



#keys = []
#for d in file_list:
#    mtch = re.match('.*temp_nw_transfer/project_number=.*',  d['Key'])
#    if mtch:
#        keys.append(mtch.group(0))
 #       project = re.match('.*temp_nw_transfer/project_number=(.*)/',  d['Key']).group(1)
 #       prefix = re.match('.*temp_nw_transfer/project_number=.*/([0-9]*_[0-9]*_[0-9]*).*',  d['Key']).group(1)
 #       name = 'C:\\Users\\robert.pharris\downloads\\' + prefix + "_" + project + '.gz'
 #       s3.download_file(BUCKET, mtch.group(0), name)
