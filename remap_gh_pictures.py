"""
![image](https://user-images.githubusercontent.com/14041622/43388821-b5ec24da-941c-11e8-8488-e2c887aaa047.png)
"""

import os
import re
import boto3
import requests
from hashlib import md5
from glob import glob

from utils.common_utils import read_envfile


os.environ.update(**read_envfile('envfile-local'))
expr = r'.*(https://user-images.githubusercontent.com/\d+/.*.png)'
bucket_name = os.environ['PIC_BUCKET_NAME']


def main():
    __import__('pudb').set_trace()
    files = glob(os.path.expanduser('~/Downloads/issues_blog/*/*.md'))
    for path in files:
        markdown = open(path).read()
        for line in markdown.split():
            # if 'user-images.githubusercontent.com' not in line:
            #     continue
            result = re.match(expr, line)
            if not result:
                continue
            gh_url = result.groups()[0]
            resp = requests.get(gh_url)
            raw = resp.content
            sha = str(md5(raw).hexdigest())
            l1, l2, l3 = sha[:2], sha[2:4], sha[4:6]
            s3_path = f'pics/{l1}/{l2}/{l3}/{sha}.png'
            bucket = boto3.resource('s3').Bucket(bucket_name)
            if not list(bucket.objects.filter(Prefix=s3_path)):
                bucket.put_object(Key=s3_path, Body=raw, ContentType='image/png')
                print('\t Uploaded')
            new_url = f'https://{bucket_name}.s3.amazonaws.com/{s3_path}'
            print(f'Exchange: {gh_url} \n\t-> {new_url}')
            markdown = markdown.replace(gh_url, new_url)
        open(path, 'w').write(markdown)
        print(f'Finished on {path}')
        print('='*80)


if __name__ == '__main__':
    main()
    print('ok.')
