# Maintaining the catalogue

[Русский](CATALOG.ru.md)

The root README is a project index. Distribution paths follow
`zdl/<type>/<project>/<effect>/`; every effect keeps its original ZDL, matching
JSON and image together. Types correspond to actual GID: Filter 2, Drive 3,
GuitarAmp 4, SFX 7. Projects describe product families.

`catalog.json` owns membership and editorial EN/RU descriptions. Initial
descriptions were imported from the owner's READMEs at
`febcec184ed54e7653a28ffe88322007883066f9`, not older sidecars. ZDL bytes own
ID/version/GID; sidecars own the Manager image reference and display name.

To add an effect, place its complete package in the project and add a manifest
entry. To add a project, add paired READMEs with catalogue markers. Human text
outside the markers is preserved.

```text
python -m pip install -r scripts/requirements.txt
python scripts/update_catalog.py
python scripts/update_catalog.py --check
python -m unittest discover -s tests -v
python scripts/package_release.py --version preview
```

Packaging uses the validated manifest, retaining previous `<effect>.zip` names,
and adds `<project>-project.zip` and `All-ZDL-FX-<version>.zip`. SYNTHESIS project
and full collection include the controller; EXE, guide and receipt are also
attached separately. LoopBe1 is external. `tests/package-baseline.json` records
pre-migration package hashes.

PRs validate catalogues, hashes and archives and produce workflow artifacts.
Only a `v*` tag publishes a Release. This PR does not merge main or publish a new
release; existing tags and release assets remain unchanged.
