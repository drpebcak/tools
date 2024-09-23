from googleapiclient.errors import HttpError

from helpers import client, get_friendly_file_type


def main():
    service = client('drive', 'v3')
    try:
        query = ""
        page_token = None
        while True:
            results = service.files().list(q=query,
                                           pageSize=10,
                                           fields="nextPageToken, files(id, name, mimeType)",
                                           pageToken=page_token,
                                           ).execute()

            items = results.get('files', [])
            if not items:
                print('No files found.')
                break

            for item in items:
                friendly_type = get_friendly_file_type(item["mimeType"])
                print(f"{item['name']} Filetype: {friendly_type} (ID: {item['id']})")

            page_token = results.get('nextPageToken')
            if not page_token:
                break

    except HttpError as err:
        print(err)


if __name__ == "__main__":
    main()
