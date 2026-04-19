import csv
import io
import logging
import os

from slackbot import licence_plate

log = logging.getLogger(__name__)

_FIELDNAMES = ["kenteken", "slackid", "name"]


class CarOwners:
    def __init__(self, csv_path: str = "/tmp/car-owners.csv") -> None:
        self.csv_path = csv_path
        self._blob_client = self._init_blob_client()
        self._data: dict[str, dict] = {}
        self.load()

    @staticmethod
    def _init_blob_client():
        conn_str = os.environ.get("AZURE_STORAGE_CONNECTION_STRING")
        if not conn_str:
            return None
        try:
            from azure.storage.blob import BlobServiceClient  # noqa: PLC0415
            container = os.environ.get("AZURE_STORAGE_CONTAINER", "slackbot")
            blob_name = os.environ.get("AZURE_STORAGE_BLOB_NAME", "car-owners.csv")
            blob = (
                BlobServiceClient.from_connection_string(conn_str)
                .get_container_client(container)
                .get_blob_client(blob_name)
            )
            log.info("Car owners backed by Azure Blob Storage (%s/%s)", container, blob_name)
            return blob
        except Exception as exc:
            log.warning("Azure Blob Storage init failed, falling back to local file: %s", exc)
            return None

    @staticmethod
    def _parse(text: str) -> dict:
        result = {}
        for row in csv.DictReader(io.StringIO(text)):
            plate = (row.get("kenteken") or "").strip()
            if plate:
                result[plate] = {
                    "slackid": row.get("slackid") or None,
                    "name": row.get("name") or None,
                }
        return result

    def _serialize(self) -> str:
        buf = io.StringIO()
        writer = csv.DictWriter(buf, fieldnames=_FIELDNAMES, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for plate, info in self._data.items():
            writer.writerow({
                "kenteken": plate,
                "slackid": info.get("slackid") or "",
                "name": info.get("name") or "",
            })
        return buf.getvalue()

    def load(self) -> None:
        if self._blob_client:
            try:
                text = self._blob_client.download_blob().readall().decode("utf-8")
                self._data = self._parse(text)
                return
            except Exception as exc:
                log.warning("Blob load failed, starting empty: %s", exc)
                self._data = {}
                return

        if os.path.exists(self.csv_path):
            with open(self.csv_path, newline="", encoding="utf-8") as f:
                self._data = self._parse(f.read())
        else:
            self._data = {}

    def save(self) -> None:
        text = self._serialize()
        if self._blob_client:
            try:
                self._blob_client.upload_blob(text, overwrite=True)
                return
            except Exception as exc:
                log.warning("Blob save failed: %s", exc)

        with open(self.csv_path, "w", newline="", encoding="utf-8") as f:
            f.write(text)

    def tag(self, plate: str, slackid: str | None = None, name: str | None = None) -> None:
        plate = licence_plate.normalize(plate)
        if len(plate) != 6:
            raise ValueError("Licence plate must be 6 characters (no dashes)")
        if slackid and slackid.startswith("@"):
            slackid = slackid[1:]
        self.load()
        self._data[plate] = {"slackid": slackid, "name": name}
        self.save()

    def untag(self, slackid: str, plate: str) -> None:
        plate = licence_plate.normalize(plate)
        self.load()
        self._data.pop(plate, None)
        self.save()

    async def lookup(self, plate: str) -> dict | None:
        plate = licence_plate.normalize(plate)
        if len(plate) != 6:
            raise ValueError("Licence plate must be 6 characters (no dashes)")
        self.load()
        result = self._data.get(plate)
        log.info("Owner lookup for %s: %s", plate, result)
        return result
