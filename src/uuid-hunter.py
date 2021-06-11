from blackduck import Client
import logging
import argparse
import pandas as pd
from pprint import pprint

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] {%(module)s:%(lineno)d} %(levelname)s - %(message)s"
)

allComponentName = []
allComponentVerName = []
allComponentCompUUID = []
allComponentVersionUUID = []
allComponentOriginUUID = []

parser = argparse.ArgumentParser("Get components and UUIDs from specific project version BOM")
parser.add_argument("--base-url", required=True, help="Hub server URL e.g. https://your.blackduck.url")
parser.add_argument("--api-key", dest='api_key', required=True, help="containing access token")
parser.add_argument("--project", dest='project_name', required=True, help="Project that contains the BOM components")
parser.add_argument("--version", dest='version_name', required=True, help="Version that contains the BOM components")
parser.add_argument("--no-csv", dest='csv_file', action='store_false', help="Don't create a CSV and print results to screen only")
parser.add_argument("--no-verify", dest='verify', action='store_false', help="disable TLS certificate verification")
args = parser.parse_args()

# with open(args.token_file, 'r') as tf:
#     access_token = tf.readline().strip()

bd = Client(base_url=args.base_url, token=args.api_key, verify=args.verify)
    
params = {
    'q': [f"name:{args.project_name}"]
}
    
projects = [p for p in bd.get_resource('projects', params=params) if p['name'] == args.project_name]
assert len(projects) == 1, f"There should be one, and only one project named {args.project_name}. We found {len(projects)}"
project = projects[0]

params = {
    'q': [f"name:{args.version_name}"]
}

versions = [v for v in bd.get_resource('versions', project, params=params) if v['versionName'] == args.version_name]
assert len(versions) == 1, f"There should be one, and only one version named {args.version_name}. We found {len(versions)}"
version = versions[0]

for components in bd.get_resource('components', version):
    originURL = components['origins'][0]['origin']
    allComponentName.append(components['componentName'])
    allComponentVerName.append(components['componentVersionName'])
    allComponentCompUUID.append(originURL.split('/')[-5])
    allComponentVersionUUID.append(originURL.split('/')[-3])
    allComponentOriginUUID.append(originURL.split('/')[-1])
    

if args.csv_file:
    df = pd.DataFrame(list(zip(allComponentName, allComponentVerName, allComponentCompUUID, allComponentVersionUUID, allComponentOriginUUID)))
    df.columns = ['Component Name', 'Component Version Name', 'Component ID', 'Version ID', 'Origin ID']
    df.to_csv('/output/' + args.project_name + '_' + args.version_name + '_uuids.csv', index=False)
else:
    pprint(list(zip(allComponentName, allComponentVerName, allComponentCompUUID, allComponentVersionUUID, allComponentOriginUUID)))
