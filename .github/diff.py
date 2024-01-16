from ghapi.all import GhApi
import os
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--ref_name', help='GitHub ref name')
parser.add_argument('-s', '--commit-sha', required=False, help='Commit SHA. If not set, --pr is used')
args = parser.parse_args()

merge_queue_prefix = 'gh-readonly-queue/'
is_merge_queue = args.ref_name.startswith(merge_queue_prefix)
if not is_merge_queue:
    print("Not a merge queue event, exiting")
    exit(0)


gh_api = GhApi(owner="openvinotoolkit", repo="testrepo", token=os.getenv("GITHUB_TOKEN"))
target_branch = re.findall(f'^{merge_queue_prefix}(.*)/', args.ref_name)[0]
target_branch_head = gh_api.repos.get_branch(target_branch).commit.sha
diff = gh_api.repos.compare_commits(f'{target_branch_head}...{args.commit_sha}')
print("\n".join([file.filename for file in diff.files]))
