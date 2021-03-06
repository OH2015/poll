from .base import *
import environ

env = environ.Env()
env.read_env(BASE_DIR / '.env')

DEBUG = False
ALLOWED_HOSTS = ['votify.jp','localhost']

DATABASES = {
    'default': {
        # AWS料金節約のため一旦ローカルDBに戻す
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'poll_db',
        # 'USER': 'admin',
        # 'PASSWORD': 'Fp5LAgMBbaFH9D7',
        # 'HOST': 'database-1.c1ch7jqm7tvt.us-east-1.rds.amazonaws.com',
        # 'PORT': 3306,
    }
}


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_STORAGE_BUCKET_NAME = 'plbucket'
AWS_S3_REGION_NAME = 'us-east-1'
AWS_ACCESS_KEY_ID = env.get_value('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env.get_value('AWS_SECRET_ACCESS_KEY')