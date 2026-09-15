from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import base64
import urllib.request
import urllib.error

# ==============================
# NEOCITIES SETTINGS
# ==============================

NEOCITIES_USERNAME = "YOUR_NEOCITIES_USERNAME_HERE"
NEOCITIES_PASSWORD = "YOUR_NEOCITIES_PASSWORD_HERE"

# ==============================
# PROGRESS SERVER
# ==============================

class ProgressHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        if self.path != "/progress":
            self.send_response(404)
            self.end_headers()
            return

        length = int(self.headers.get("Content-Length", 0))
        data = self.rfile.read(length)

        try:
            progress = json.loads(data)

            rooms = progress["rooms"]
            total = progress["total"]
            percent = progress["percent"]

            print()
            print("===== PROGRESS RECEIVED =====")
            print("ROOMS:", rooms)
            print("TOTAL:", total)
            print("PERCENT:", percent)
            print("=============================")

            # Create progress.json
            progress_json = {
                "rooms": rooms,
                "total": total,
                "percent": percent
            }

            with open("progress.json", "w", encoding="utf-8") as file:
                json.dump(progress_json, file, indent=2)

            print("progress.json updated.")

            # Upload progress.json to Neocities
            upload_file()

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")

        except Exception as error:
            print("ERROR:", error)

            self.send_response(500)
            self.end_headers()


def upload_file():

    url = "https://neocities.org/api/upload"

    credentials = (
        NEOCITIES_USERNAME + ":" + NEOCITIES_PASSWORD
    ).encode("utf-8")

    auth = base64.b64encode(credentials).decode("ascii")

    boundary = "----RoomsProgressBoundary"

    with open("progress.json", "rb") as file:
        file_data = file.read()

    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="progress.json"; filename="progress.json"\r\n'
        f"Content-Type: application/json\r\n"
        f"\r\n"
    ).encode("utf-8")

    body += file_data

    body += (
        f"\r\n--{boundary}--\r\n"
    ).encode("utf-8")

    request = urllib.request.Request(
        url,
        data=body,
        method="POST"
    )

    request.add_header(
        "Authorization",
        "Basic " + auth
    )

    request.add_header(
        "Content-Type",
        "multipart/form-data; boundary=" + boundary
    )

    try:
        with urllib.request.urlopen(request) as response:
            result = response.read().decode("utf-8")

            print("===== NEOCITIES RESPONSE =====")
            print(result)
            print("==============================")

    except urllib.error.HTTPError as error:
        print("NEOCITIES ERROR:", error.code)
        print(error.read().decode("utf-8"))


server = HTTPServer(("127.0.0.1", 8000), ProgressHandler)

print("SERVER STARTED")
print("Listening on 127.0.0.1:8000")

server.serve_forever()