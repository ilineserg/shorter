import os
from string import Template


DATABASE_URI = os.environ.get('DATABASE_URI', default='postgresql+asyncpg://postgres:postgres@localhost:5432/postgres')
SHORT_URL_TEMPLATE = Template(os.environ.get('SHORT_URL_TEMPLATE', default='https://example.com/$slug'))
