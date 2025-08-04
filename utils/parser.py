import zipfile
import os
import json

async def parse_uploaded_file(path):
    records = []

    if path.endswith(".zip"):
        with zipfile.ZipFile(path, 'r') as zip_ref:
            extract_dir = path.replace(".zip", "_extracted")
            zip_ref.extractall(extract_dir)

            for root, dirs, files in os.walk(extract_dir):
                for file in files:
                    full_path = os.path.join(root, file)
                    ext = file.lower().split(".")[-1]
                    if ext in ["txt", "json"]:
                        records.extend(await _parse_file(full_path))

            # Clean extracted folder
            try:
                for root, dirs, files in os.walk(extract_dir, topdown=False):
                    for name in files:
                        os.remove(os.path.join(root, name))
                    for name in dirs:
                        os.rmdir(os.path.join(root, name))
                os.rmdir(extract_dir)
            except Exception:
                pass

    elif path.endswith(".json") or path.endswith(".txt"):
        records = await _parse_file(path)

    return records


async def _parse_file(filepath):
    parsed = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # JSON line or key:value
            try:
                parsed.append(json.loads(line))
            except json.JSONDecodeError:
                if ":" in line:
                    parts = line.split(":")
                    parsed.append({"key": parts[0].strip(), "value": ":".join(parts[1:]).strip()})
                else:
                    parsed.append({"value": line})

    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return parsed