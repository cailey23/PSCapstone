"""
This is a backup to load a video to google drive, it requires some setup that isn't on the pi right now. Since this is
the backup, it'll be fixed if we need to use it
"""


from __future__ import print_function

import json
import os

from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/drive.file']


def login():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds


def create_folder():
    creds = login()
    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)
        file_metadata = {
            'name': 'VideoTest',
            'mimeType': 'application/vnd.google-apps.folder'
        }

        # pylint: disable=maybe-no-member
        file = service.files().create(body=file_metadata, fields='id'
                                      ).execute()
        print(F'Folder ID: "{file.get("id")}".')
        return file.get('id')
    except HttpError as error:
        print(F'An error occurred: {error}')
        return None


def read_data():
    with open("google_drive_data") as f:
        values = [[fff.strip() for fff in ff.split(":")] for ff in f.readlines()]
    data = {

    }
    for key, val in values:
        data[key] = val
    return data


def upload_file(folder_id):
    """Insert new file.
    Returns : Id's of the file uploaded

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """

    creds = login()
    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)

        file_metadata = {'name': 'Timelapse.mp4',
                         'parents': [folder_id]
                         }
        media = MediaFileUpload('static/Timelapse.mp4',
                                mimetype='video/mp4')
        # pylint: disable=maybe-no-member
        file = service.files().create(body=file_metadata, media_body=media,
                                      fields='id').execute()
        print(F'File ID: {file.get("id")}')

    except HttpError as error:
        print(F'An error occurred: {error}')
        file = None

    return file.get('id')


def update_file(file_id,folder_id):
    """Update an existing file's metadata and content.

    Args:
    service: Drive API service instance.
    file_id: ID of the file to update.
    new_title: New title for the file.
    new_description: New description for the file.
    new_mime_type: New MIME type for the file.
    new_filename: Filename of the new content to upload.
    new_revision: Whether or not to create a new revision for this file.
    Returns:
    Updated file metadata if successful, None otherwise.
    """
    creds = login()
    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)
        # First retrieve the file from the API.

        # File's new metadata.
        file_metadata = {'name': 'Timelapse.mp4',
                         }

        # File's new content.
        media = MediaFileUpload('static/Timelapse.mp4',
                                mimetype='video/mp4')

        # Send the request to the API.
        updated_file = service.files().update(
            fileId=file_id,
            body=file_metadata, media_body=media,
            fields='id',
            ).execute()
        return updated_file
    except HttpError as error:
        print(F'An error occurred: {error}')

def write_data(folder_id, file_id):
    with open("google_drive_data", "w") as f:
        f.write(f"Folder ID: {folder_id}\nFile ID: {file_id}")

def main():
    data = read_data()
    if 'Folder ID' not in data:
        folder_id = create_folder()
    else:
        folder_id = data["Folder ID"]
    if "File ID" not in data:
        file_id=upload_file(folder_id)
    else:
        file_id=data["File ID"]
        update_file(file_id,folder_id)
    if "Folder ID" not in data or "File ID" not in data:
        write_data(folder_id, file_id)


if __name__ == '__main__':
    main()
