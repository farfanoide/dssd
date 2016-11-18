from __future__ import unicode_literals

from django.db import models
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from oauth2client.service_account import ServiceAccountCredentials
import httplib2
from django.conf import settings
import os


__all__ = (
    'GdriveRepository',
)

class GdriveRepository(object):

    def __init__(self):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            os.path.join(settings.BASE_DIR, 'gdrive', 'credentials.json'),
            'https://www.googleapis.com/auth/drive'
        )
        http = credentials.authorize(httplib2.Http())

        self.service = build('drive', 'v3', http=http)

    def list(self):
        return self.service.files().list(fields='files(id,name,shared,webViewLink)').execute().get('files')

    def get(self, id):
        response = self.service.files().get(fileId=id, fields='id,name,webViewLink').execute()
        response['content'] = self.get_content(id)
        return response

    # def export(self, id, as='plain/txt'):
    #     return self.service.

    def delete(self, id):
        self.service.files().delete(fileId=id).execute()

    def create_and_share(self, title, email):
        file_data = self.create(title)
        share_data = self.share(file_data['id'], email)
        return self.get(file_data['id'])

    def create(self, name):
        file_metadata = {
            'name': name,
            'mimeType': 'application/vnd.google-apps.document',
        }
        response = self.service.files().create(body=file_metadata, fields='id')
        return response.execute()

    def share(self, file_id, user_email):

        user_permission = {
            'type': 'user',
            'role': 'writer',
            'emailAddress': user_email,
        }

        response = self.service.permissions().create(
            fileId=file_id,
            body=user_permission,
            fields='id',
            sendNotificationEmail=False,
        )

        return response.execute()

    def unshare(self, file_id):
        batch = self.service.new_batch_http_request()

        permissions = self.service.permissions().list(fileId=file_id).execute()

        for permission in permissions.get('permissions'):
            if permission['role'] != 'owner':
                batch.add(self.service.permissions().delete(
                    fileId=file_id,
                    permissionId=permission['id'],
                    fields='id',
                ))

        batch.execute()
    def get_content(self, id, as_format='text/plain'):
        return self.service.files().export(fileId=id, mimeType=as_format).execute()

    def update(self, file_id, file_descriptor):
        upload = MediaIoBaseUpload(file_descriptor, 'application/rtf')
        return self.service.files().update(fileId=file_id, media_body=upload).execute()
