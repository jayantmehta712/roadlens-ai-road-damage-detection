"""Restore the exact audited source and trained model before a Render build."""
from pathlib import Path
import hashlib,json,zipfile
root=Path(__file__).resolve().parent
manifest=json.loads((root/'deployment-manifest.json').read_text())
archive=root/'roadlens-source.zip'
assert hashlib.sha256(archive.read_bytes()).hexdigest()==manifest['source_sha256'],'Source archive checksum mismatch'
service=root/'service';service.mkdir(exist_ok=True)
with zipfile.ZipFile(archive) as z:
    for name in z.namelist():
        target=(service/name).resolve()
        if not target.is_relative_to(service.resolve()):raise ValueError('Unsafe source member')
    z.extractall(service)
model=bytearray()
for part in manifest['parts']:
    data=(root/part['name']).read_bytes()
    assert hashlib.sha256(data).hexdigest()==part['sha256'],'Checkpoint part checksum mismatch'
    model.extend(data)
assert hashlib.sha256(model).hexdigest()==manifest['model_sha256'],'Model checksum mismatch'
(service/'models').mkdir(exist_ok=True)
(service/'models/road_damage_model.pth').write_bytes(model)
print('Source and genuine trained checkpoint restored and verified.')
