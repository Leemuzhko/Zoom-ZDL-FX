# Maintaining the catalogue

[Русский](CATALOG.ru.md)

The root README is a project index. Distribution paths follow
`zdl/<type>/<project>/<effect>/`; every effect keeps its original ZDL, matching
JSON and image together. Types correspond to actual GID: Filter 2, Drive 3,
GuitarAmp 4, SFX 7, PedalOperated 11. Projects describe product families.

`catalog.json` owns membership and editorial EN/RU descriptions. Initial
descriptions were imported from the owner's READMEs at
`febcec184ed54e7653a28ffe88322007883066f9`, not older sidecars. ZDL bytes own
ID/version/GID; sidecars own the Manager image reference and display name.
Effect tables are sorted by numeric ID read from the ZDL, ascending; the name
breaks ties. EN and RU use the same order.

To add an effect, place its complete package in the project and add a manifest
entry. To add a project, add paired READMEs with catalogue markers. Human text
outside the markers is preserved.

For hardware-dependent effects, keep compatibility notes in the project and
packaged READMEs, the EN/RU catalogue descriptions and the ZEM JSON descriptions.
Distinguish tested, untested and unsupported models. Games use the
`pedal-operated/games` project; their package category remains the actual ZDL GID.

```text
python -m pip install -r scripts/requirements.txt
python scripts/update_catalog.py
python scripts/update_catalog.py --check
python -m unittest discover -s tests -v
python scripts/package_release.py --version preview
```

Packaging uses the validated manifest, retaining previous `<effect>.zip` names,
and adds `All_<PROJECT>.ZIP` for projects with archive enabled and
`All-ZDL-FX-<version>.zip`. All_SYNTHESIS.ZIP includes the effect, controller and instructions; all are
also included in the full collection.
EXE, guide and receipt are attached separately. LoopBe1 is external. `tests/package-baseline.json` records
pre-migration package hashes and approved additions. New effect files extend this
baseline without changing the hashes of existing packages.

Validate catalogue changes locally with the commands above, or start the workflow
manually on a branch to produce workflow artifacts. Pull requests and ordinary
branch pushes do not launch GitHub Actions automatically. Tags matching `v*`
automatically validate and package the collection and publish a Release.
Manual dispatch on a tag also runs the release job.
